#Ask the user what today's weather is, and then if it's rain or snow, print something negative. If it's sun, print something positive. If it's neither, print that you do not know what it is.
weather = input('What is the weather today? : \n')
if weather == 'rainy' or weather =='snowy':
    print('Good grief is it falling again? I really dislike it!')
elif weather == 'sunny':
    print('Sweet! Let us go for a walk around the neighborhood today then!')
else:
    print('Uhh... Not sure what that is. Is it raining meatballs or something?')