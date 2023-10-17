# EXERCIES 1
#Accept two user ages as inputs and give us the difference between them. 
#(The Answer should always be a positive output

user1 = int(input("what is your age user_one? "))
user2 = int(input("what is your age user_two? "))

age = user1 - user2
print("The difference in your age is: ",(abs(age)))

# Exercise #2 
# Accept 3 user inputs for variables named noun, verb and adjective. 
# Print out a formatted string using the outputs

noun = input("Please type in a 'noun'")
verb = input("Please type in a 'verb'")
adjective = input("Please type in a 'adjective'")

word_smash = f"{noun},{verb},{adjective}"
print(word_smash)

word_smash ="The {} {} {}! ".format(noun, verb, adjective)
print(word_smash)

#Edxercise #3
# Take in a users input for their age, 
# if they are younger than 18 print kids, 
# if they're 18 to 65 print adults, else print seniors

age = int(input("What is your age? "))

if age <= 18:
    print("kids")
elif age > 19 and age < 65:
    print("adults")
else:
    print("seniors")

# Exercise 4
# Take in a number from a user input, output the number squared.

user_num = int(input("give me a number "))
int = user_num ** 2

print(int)

#Exercise 5
#Check the below variables' length. 
# If the length of the word is greater than 5 output True, 
# if it is less than 5, output False

word1 = "panini"
word2 = "bulbasaur"
word3 = "pie"
word4 = "dolphin"
word5 = "dog"

length_of_word = len(word1)
print(word1, length_of_word)
if length_of_word > 5:
    print(True)
else:
    print(False)
    
length_of_word = len(word2)
print(word2, length_of_word)
if length_of_word > 5:
    print(True)
else:
    print(False)
    
length_of_word = len(word3)
print(word3, length_of_word)
if length_of_word > 5:
    print(True)
else:
    print(False)
    
length_of_word = len(word4)
print(word4, length_of_word)
if length_of_word > 5:
    print(True)
else:
    print(False)
    
length_of_word = len(word5)
print(word5, length_of_word)
if length_of_word > 5:
    print(True)
else:
    print(False)
    


