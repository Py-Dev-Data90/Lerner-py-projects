# Guidelines:
# (1) If the first letter is a vowel -- a, e, i, o, u -- then add 'way' to the end
# (2) If the first letter is *not* a vowel, move the first letter to the end and add 'ay'
# (3) Ask the user to enter one word in English, with importance placed on capital letters
# (4) Print the translation into Pig Latin

def pig_lator():
    vowels = 'aeiouAEIOU'
    user_input = input('Enter thy piggy phrase, with capital letters and proper punctuation please: ')
    
    first_letter = user_input[0]
    
    if first_letter in vowels:
        print(user_input + 'way')
    else:
        print(user_input[1:] + first_letter + 'ay')
