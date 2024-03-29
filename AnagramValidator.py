#!/usr/bin/env python
import re
import sys
from collections import defaultdict

class AnagramValidator(object):

  def __init__(self):
    self.__dict = defaultdict(lambda : set()) # key,value == sorted(word), set(agrams that are valid english words)
    fileHandle = open('words.txt')
    for line in fileHandle:
      m = re.search('[a-z]+',line.lower())	# parse each line for the word
      if m is not None: # this might be None, convention of re.search
        key = ''.join(sorted(m.group())) # sort the word and use as key
        self.__dict[key].add(m.group()) # defaultdict lets us get away without initializing set()
    fileHandle.close()

  def validAnagrams(self,w):
    key = ''.join(sorted(w.lower())) # the key is a sorted sequence of characters, so sort the sequence
    results = self.__dict[key] # return valid anagrams from pre-processor method
    return results

if __name__ == '__main__':
	v = AnagramValidator()
	print v.validAnagrams('free') if len(sys.argv) < 2 else v.validAnagrams(sys.argv[1])
