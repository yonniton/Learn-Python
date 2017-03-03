# a variable named formatter made up of 4 raw strings
formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % ('one', 'two', 'three', 'four')
print formatter % (True, False, False, True) # True and False are built-in Constants
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
