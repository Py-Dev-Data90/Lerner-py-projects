# x = None
# #here we don't have to use == here, or 'if x is' (remember is and if are part of the language), we can just do the basic check
# if x:
#     print('x is None')
# else:
#     print('x is not None')

#this won't work because None == True is false, so it will return "False"
#Everything in Python, in a boolean context, is True unless specifically negating, like empty, 0 , None, False

#name is a string...non-empty strings are True in a boolean context, thus we can do:

# name = input('Enter your name: ')
# if name:
#     print('Hello, ' + name)
# else:
#     print('Hey! You did not enter a name!')

#Now say we want to check if something is true, if we set it to true beforehand, then there is not need to say it again

x = True

if x:
    print('Yes, it is True!')