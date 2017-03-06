from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "The first variable is:", first
print "The second variable is:", second
print "The third variable is:", third

str_args = raw_input("Whitespace-delimited args? ")
print "The remaining variables are: %s" % str_args.split()
