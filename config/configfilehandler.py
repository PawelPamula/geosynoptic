import os
from lxml import etree


class InvalidPathException(Exception):
    pass


class ConfigFileHandler(object):
    def __init__(self, configFilePath='config.xml'):
        """
        Creates configFile under specified path if one does not exist
        Creates lxml.etree structure for handling config info
        """
        self.configFilePath = configFilePath
        self.configFileName = os.path.basename(self.configFilePath)

        if not os.path.isfile(self.configFilePath):
            try:
                print "config.xml was not found and it's being created..."
                #creates new default config
                self.root = etree.Element("config")
                defaultIconPath = etree.SubElement(self.root, "defaultIconPath")
                defaultIconPath.text =  os.path.join(os.path.dirname(__file__), 'resource/icons/default.png')
                self.root.append(etree.Element("groups"))
                self._saveConfigToFile()
            
            except OSError:
                print 'Error: Config file was not created'

        else:
            print "config.xml was found!"
            try:
                self.root = etree.parse(self.configFilePath).getroot()
                
            except etree.XMLSyntaxError:
                print "%s is not valid xml file" % self.configFileName
                raise Exception("Invalid XML File")


    def getDefaultIconPath(self):
        for element in self.root.iter():
            if element.tag == 'defaultIconPath':
                return element.text

    def printConfig(self):
        print etree.tostring(self.root, pretty_print=True)


    def _saveConfigToFile(self):
        """
        Writes the xml structure of xml tree to configFilePath
        """
        with open(self.configFileName, 'w') as configFile:
            #print etree.tostring(self.root, pretty_print=True)
            #configFile.write(etree.tostring(self.root, pretty_print=True))
            doc = etree.ElementTree(self.root)
            doc.write(configFile, pretty_print=True)
        configFile.close()

    def editGroupName(self, old_name, new_name, new_path):
        element = self.root.xpath("//groups/group[@name='%s']" % old_name)
        if element:
            print  element[0].attrib['name']
            element[0].attrib['name'] = new_name
            if new_path != '':
                element[0].attrib['icon_path'] = new_path
            self._saveConfigToFile()
        else:
            'NOT FOUND'

    def addGroup(self, group_name, icon_path):
        newGroup = etree.Element("group")
        newGroup.attrib['name'] = group_name
        newGroup.attrib['icon_path'] = icon_path

        if not self.root.xpath("//groups/group[@name='%s']" % group_name):
            self.root.xpath('//groups')[0].insert(0, newGroup)
        self._saveConfigToFile()

    def addDevice(self, device_name, group_name):
        """
        Returns True if adding device was successfull
        """
        self.addGroup(group_name=group_name)
        element = self.root.xpath("//groups/group[@name='%s']" % group_name)

        for dev in element[0]:
            if dev.text == device_name:
                return False
        else:
            newDevice = etree.Element("device")
            newDevice.text = device_name
            element[0].insert(-1, newDevice)
        self._saveConfigToFile()
        return True

    def groupExists(self, group_name):
        element = self.root.xpath("//groups/group[@name='%s']" % group_name)
        if element:
            return True
        return False

    def getGroups(self):
        groups = self.root.xpath("//groups/group")
        return [g.attrib['name'] for g in groups]

    def getGroupsWithIcons(self):
        groups = self.root.xpath("//groups/group")
        return [(g.attrib['name'], g.attrib['icon_path']) for g in groups]


if __name__ == '__main__':
    c = ConfigFileHandler()
    c.printConfig()