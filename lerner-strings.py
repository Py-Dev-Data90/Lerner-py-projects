
test_str = 'abcdefghijklmnopqrstuvwxyz'
def halver(alphabet):

    print(alphabet)

    length = len(alphabet)
    print(length)
    #length//2 calculates the midpoint of the string
    #alphabet[:length // 2] slices from the start up to (but not including) the midpoint
    half_alphabet= alphabet[:length//2]
    print(half_alphabet)
halver(test_str)
halver('a')
#program returns an empty string because it floors(rounds it down) 0.5 to 0, up to but not including a? nothing, so an empty string.
#index is the position of characters, indices is the plural form
#remember that the indices/index of characters start at zero in almost all computer languages
halver('abcd')

print(test_str[0])
print(test_str[-1]) #return the final element of the string
#returns the character that is at the 0 mark in the string
#You can not change a string!!!!! SUPER IMPORTANT