# this infinite loop will crash the IDE - seems like PyCharm associates its own process with the code process

while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
