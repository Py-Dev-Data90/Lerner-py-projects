#Ask the user what today's weather is, and then if it's rain or snow, print something negative. If it's sun, print something positive. If it's neither, print that you do not know what it is.
#My notes: Remember with our true/false condition, you need to state the surrounding variables weather, and weather, twice, otherwise, the program won't throw an error, but it won't give you the result that you want!
weather = input('What is the weather today? : \n')
if weather == 'rainy' or weather =='snowy':
    print('Good grief is it falling again? I really dislike it!')
elif weather == 'sunny':
    print('Sweet! Let us go for a walk around the neighborhood today then!')
else:
    print('Uhh... Not sure what ' + weather + ' is. Is it raining meatballs or something?')