# from sys module import a member called 'argv'
from sys import argv
#unpack
# test 4 - test when a commit closes the issue
script, filename = argv
fp = open(filename)
print "Reading file %r " % fp
print fp.read()
fp.close()
