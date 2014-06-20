#!/python

import os
import operator
import sys
import json

word_frequency = dict()

count_of_files = 0
for filename in os.listdir('/dev/in'):
    count_of_files = count_of_files + 1
    with open(os.path.join('/dev/in', filename), 'r') as f:
        line = json.load(f)
        #sys.stdout.write('%s\n' % line)
        for word_cnt_pair in line:
            key = word_cnt_pair[0]
            count = word_cnt_pair[1]
            #print "Key:%s" % key
            #print "Count:%s" % count
            if key in word_frequency:
                word_frequency[key] += int(count)
            else:
                word_frequency[key] = int(count)


sorted_result = sorted(word_frequency.iteritems(), key=operator.itemgetter(1), reverse=True)

print "Number of files processed:%s" % count_of_files
#print "-------"
#print sorted_result
#print "Done"

for result in sorted_result:
    #sys.stdout.write('%s\n' % result)
    print result
