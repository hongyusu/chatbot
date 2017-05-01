

import sys
import xml.etree.ElementTree
import os
import re

def processing(inputFilename, topic, fout):
    root = xml.etree.ElementTree.parse(inputFilename).getroot()
    for c1 in root:
        if c1.get('PostTypeId') == "1":
            print re.sub('"', "", c1.get('Title'))
            try:
                fout.write('"1"\t"%s"\t"%s"\n' % (topic, re.sub('"', "", c1.get('Title'))))
            except:
                print c1.get('Title')


if __name__ == '__main__':
    rootdir='/Users/hongyusu/Codes/chatbot/data/stackoverflowdata/'
    fout = open(rootdir + "sample", "w")
    fout.write("id\tintent\tsentence\n")
    for root,dirs,filenames in os.walk(rootdir):
        for dir in dirs:
            inputFilename = root+dir+"/Posts.xml"
            processing(inputFilename, dir, fout)
    fout.close()


