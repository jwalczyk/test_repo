# from sys module import a member called 'argv'
from sys import argv
#unpack
# test 5 - test PR title
script, filename = argv
fp = open(filename)
print "Reading file %r " % fp
print fp.read()
fp.close()
