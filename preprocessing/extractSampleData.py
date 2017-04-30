

import sys
import xml.etree.ElementTree
import os

def processing(inputFilename, topic, fout):
    root = xml.etree.ElementTree.parse(inputFilename).getroot()
    for c1 in root:
        if c1.get('PostTypeId') == "1":
            try:
                fout.write("%s, %s\n" % (topic, c1.get('Title')))
            except:
                print c1.get('Title')


if __name__ == '__main__':
    rootdir='/Users/hongyusu/Codes/chatbot/data/stackoverflowdata/'
    fout = open(rootdir + "sample", "w")
    for root,dirs,filenames in os.walk(rootdir):
        for dir in dirs:
            inputFilename = root+dir+"/Posts.xml"
            processing(inputFilename, dir, fout)
    fout.close()


