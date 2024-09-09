import sys 
import lxml.etree as etree
from xmlCompressor import XMLCompressor

def main():
    sys.stdout = open('bin/output.txt', 'w')
    tree = etree.parse('example.xml')
    root = tree.getroot()
    compressedXML = XMLCompressor(root)
    print(compressedXML.pathCodes)
    query = 'book/section/title'
    print(compressedXML.XPathQueryEncoding(query))
    print(compressedXML.get(query))

if __name__ == '__main__':
    main()
