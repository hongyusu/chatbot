

import sys
import xml.etree.ElementTree
import os
import re
import codecs

def processing(inputFilename, topic, fout):
    root = xml.etree.ElementTree.parse(inputFilename).getroot()
    for c1 in root:
        if c1.get('PostTypeId') == "1":
            try:
                fout.write('""\t"%s"\t"%s"\n' % ("1", topic, re.sub('"', "", c1.get('Title'))))
            except:
                print c1.get('Title')


if __name__ == '__main__':
    rootdir='/Users/hongyusu/Codes/chatbot/data/stackoverflowdata/'
    fout = codecs.open(rootdir + "sample", "w", encoding="utf-8")
    for root,dirs,filenames in os.walk(rootdir):
        for dir in dirs:
            inputFilename = root+dir+"/Posts.xml"
            processing(inputFilename, dir, fout)
    fout.close()


