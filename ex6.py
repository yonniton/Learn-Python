x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)  # 2 `string` arguments

print x
print y

print "I said: %r." % x                                       # 1 `raw` argument
print "I also said: '%s'." % y                                # 1 `raw` argument

hilarous = False
joke_evaluation = "Isn't the joke so funny?! %r"              # 1 `raw` argument

print joke_evaluation % hilarous

w = "This is the left side of..."
e = "a string with a right side."

print w + e
