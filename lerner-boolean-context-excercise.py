x = None
#here we don't have to use == here, or 'if x is' (remember is and if are part of the language), we can just do the basic check
if x:
    print('x is None')
else:
    print('x is not None')

#this won't work because None == True is false, so it will return "False"
#Everything in Python, in a boolean context, is True unless specifically negating, like empty, 0 , None, False