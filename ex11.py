age = int(raw_input("How old are you? (years) "))
height = float(raw_input("How tall are you? (cm) "))
weight = float(raw_input("How much do you weigh? (kg) "))

print "So you are %d years old, %d cm tall and %.1f kg heavy." % (
    age, height, weight
)
