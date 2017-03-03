name = 'Zed A.Shaw'
age = 35 # not a lie
height_inches = 74 # inches
weight_pounds = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_cm = height_inches * 2.54
weight_kg = weight_pounds * 0.45359237

print "Let's talk about %s." % name
print "He's %d inches tall." % height_inches
print "He's %d cm tall." % height_cm
print "He's %d pounds heavy." % weight_pounds
print "He's %d kg heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height_inches, weight_pounds, age + height_inches + weight_pounds)
