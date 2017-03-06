from sys import argv

script, src_name, dest_name = argv

print "Copying from %r to %r" % (src_name, dest_name)

src_data = open(src_name).read()
print "The input file is %d bytes long" % len(src_data)

open(dest_name, 'w').write(src_data)

print "Alright, all done."
