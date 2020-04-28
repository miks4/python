
def Max_num(num1,num2,num3):
    if num1 >= num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3


print("the bigest number",Max_num(3,4,5))

num1 = float(input("enter the first number:"))

num2 = float(input("enter the second number:"))
op = 0

print("1. +")
print("2. -")
print("3. /")
print("4. *")
op = input("enter operator:")

if op == 1:
    print(num1 + num2)
elif op == 2:
    print(num1 - num2)
elif op == 3:
    print(num1 / num2)
elif op == 4:
    print(num1 * num2)
else:
    print("invalid operator") 
    
monthConversitions = {
    "Jan" : "January",
    "feb" : "february",
    "mar" : "march",
    "apr" : "april",
    "may" : "may",
    "jun" : "jun",
    "jul" : "july",
    "aug" : "august",
    "sep" : "september",
    "oct" : "october",
    "nov" : "november",
    "dec" : "december"
    }

print(monthConversitions["nov"])
print(monthConversitions.get("jan","not a valid key"))
 
i = 1
while  i <=10:
    print(i)
    i += 1

secret_word = "giraffe"
guess = ""
tries = 0
triesLimit = 3
outOfGuess = False
while guess != secret_word and not(outOfGuess):
    if tries < triesLimit:
        guess = input("enter guess:")
        tries += 1
    else:
        outOfGuess = True
if outOfGuess:
    print("you lose")
else:
    print("you win")

friends = ["jim","karen"]
len(friends)
for friend in friends:
    print(friend)
for letter in "academy":
    print(letter)
for num in range(3,10):
    print(num)
for index in range(len(friends)): 
    print(friends[index])
