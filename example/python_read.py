# from sys module import a member called 'argv'
from sys import argv
#unpack
# test 3
script, filename = argv
fp = open(filename)
print "Reading file %r " % fp
print fp.read()
fp.close()

# gui stream test
# gui test for seq no
# yet another stream test 
# another stream test 
