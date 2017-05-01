

import sys
import xml.etree.ElementTree
import os
import re

def processing(inputFilename, topic, fout_train, fout_test):
    print("%15s %s" %(topic, inputFilename))
    root = xml.etree.ElementTree.parse(inputFilename).getroot()
    n = 0
    for c1 in root:
        if c1.get('PostTypeId') == "1":
            n += 1
            try:
                if n % 100 == 0:
                    fout_test.write('"%s"\t"%s"\t"%s"\n' % (c1.get('Id'), topic, re.sub('"', "", c1.get('Title').encode('ascii','ignore').decode('ascii'))))
                else:
                    fout_train.write('"%s"\t"%s"\t"%s"\n' % (c1.get('Id'), topic, re.sub('"', "", c1.get('Title').encode('ascii','ignore').decode('ascii'))))
            except:
                print c1.get('Id'), topic, c1.get('Title')


if __name__ == '__main__':
    rootdir='/Users/hongyusu/Codes/chatbot/data/'
    fout_train = open(rootdir + "/processed/stackexchange/train.dat", "w")
    fout_test  = open(rootdir + "/processed/stackexchange/test.dat",  "w")
    fout_train.write("id\tintent\tsentence\n")
    fout_test.write("id\tintent\tsentence\n")
    for root,dirs,filenames in os.walk(rootdir + "/raw/stackexchange/"):
        for dir in dirs:
            inputFilename = root+dir+"/Posts.xml"
            processing(inputFilename, dir, fout_train, fout_test)
    fout_train.close()
    fout_test.close()


