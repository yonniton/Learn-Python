x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x # string inside a string
print "I also said: '%s'" % y # string inside a string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # string inside a string

print joke_evaluation % hilarious # string inside a string

w = "This is the left side of..."
e = "a string with a right side."

print w + e

