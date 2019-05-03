# -*- coding: utf-8 -*-

import fileinput
import sys
import codecs
import datetime

metadata_fname = sys.argv[1]


speakers = {}

f = codecs.open(metadata_fname, 'r', encoding='iso-8859-1')
for line in f.readlines(): # fileinput.input(metadata_fname):
    line = line.strip('\n\r').split(',')
    print line
    # print len(line)
    speaker, start, end = line[:3]
    fname = line[-1]
    #_, start = start.split(' ')
    #_, end = end.split(' ')
    #print start, end
    start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')

    duration = end - start

    if speaker not in speakers:
        speakers[speaker] = [duration, 1, [fname]]
    else:
        speakers[speaker][0] += duration
        speakers[speaker][1] += 1
        speakers[speaker][2].append( fname )




# for s in  speakers:
#     print s 
#     print speakers[s]


speaker_info = [[speakers[speaker][0], speakers[speaker][1], speaker] for speaker in speakers]
speaker_info.sort()

for (dur, num, sp) in speaker_info:
    print '%s %s %s'%(sp, dur, num)

    #print [sp]

if 0:
    print 
    print 
    for base in speakers[u'J\xf3hanna Sigur\xf0ard\xf3ttir'][2]:
        print base

