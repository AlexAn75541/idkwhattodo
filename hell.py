import re

nigga = open('mbox-short.txt')
numlist = list()
for line in nigga:
    line = line.rstrip()
    #if re.search('From:', line):
       # print(line)
    #if re.findall('From:(\\S+@[^ ]*\\S)', line):
        #print(line)
    stuff = re.findall('X-DSPAM-Confidence: $([0-9.]+)', line)
    if len(stuff) > 0:
       numlist.append(float(stuff[0]))
print('Maximum:', (numlist)) # min