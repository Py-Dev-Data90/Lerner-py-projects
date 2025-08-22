#Strip returns something without spaces, remember, it does not affect name since strings are immutable, it returns a new string
#if we want to change a string, we have to reassign it a new value, such as x = 'potato'
#This is called method chaining, where you use more than one string method in a row!
name = input('Enter your name:').strip().capitalize()
print('Hello,' + name + '!')
