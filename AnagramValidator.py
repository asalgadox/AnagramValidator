#!/usr/bin/env python
import re
import sys

class AnagramValidator(object):

  def __init__(self):
    self.__dict = {}
    fileHandle = open('words.txt')
    for line in fileHandle:
      m = re.search('\w+',line)
      if m is not None:
        key = ''.join(sorted(m.group()))
        if key in self.__dict: self.__dict[key].add(m.group())
        else: self.__dict[key] = set([m.group()])
    fileHandle.close()

  def validAnagrams(self,w):
    key = ''.join(sorted(w))
    return self.__dict.get(key)

if __name__ == '__main__':
	v = AnagramValidator()
	print v.validAnagrams('freesib') if len(sys.argv) < 2 else v.validAnagrams(sys.argv[1])
