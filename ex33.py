from sys import argv

numbers = []


def append_inc_nums_till(top, step=1):
    for i in range(0, top, step):
        print "At the top i is %d" % i
        numbers.append(i)

        i += step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

script, upper_limit, inc = argv

append_inc_nums_till(
    int(upper_limit),
    int(inc)
)

print "The numbers: "
for num in numbers:
    print num
