alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet)

length = len(alphabet)
print(length)
#length//2 calculates the midpoint of the string
#alphabet[:length // 2] slices from the start up to (but not including) the midpoint
half_alphabet= alphabet[:length//2]
print(half_alphabet)