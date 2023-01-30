#!/usr/bin/env python3

import rospy
import sys
from basics.srv import WordCount, WordCountRequest

rospy.init_node('service_client')

rospy.wait_for_service('word_count')

word_counter = rospy.ServiceProxy('word_count', WordCount)
words = ' '.join(sys.argv[1:])
word_count = word_counter(words)

print("There are {} words in '{}'".format(word_count.count, words))