n = input()
vowels = 'aeiou'
numbers = '1234567890!@#$%^&*'
for char in n:  # checks each character in the string 
#  if the character is a space or a non letter, the loop stops
  if char == " " or char in numbers:
    break
# if the character is a vowel, the string 'vowel' will print
  if char in vowels:
    print('vowel')
# if the character is a consonant, the string 'consonant' will print out
  else:
    print('consonant')
  
  
