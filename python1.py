
from math import*


name = "milos"
age = 35
print("my name is"+name+",")
print("age:",age)
isMale = False
phrase = "academy"
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase[5])
print(len(phrase))
print("[",phrase.index("c"),"]")
print(phrase.replace("academy","school"))

print("math operations")
number = 5
print(str(number) + "my lucky number")
number2 = -4
number3 = 3
print(abs(number2))
print(pow(number,number3))
print(max(number3,number2))
print(round(3.4))
print(floor(3.7))
print(ceil(3.1))
print(sqrt(25))

NAME = input("enter you name: ")
AGE = input("enter you age: ")
print("hello" , NAME, "you are",AGE)

num1 = input("enter the fisrt number")
num2 = input("emter another number: ")
result = float(num1) + float(num2)
print(result)

print("game")
color = input("enter a color")
plural_noun = input("enter aplural noun")
celebrity = input("enter a celebrity")
print("roses are", color)
print(plural_noun , "are blue")
print("i love", celebrity)

print("lsite")
friends = ["kevin","karen","jim"]
lucky_number = [1,2,3]
friends[2] = "tom"
friends.extend(lucky_number)
print(friends.index(2))
friends.append("mike")
friends.insert(1,"kate")
friends.remove("jim")
print(friends.count("jim"))
lucky_number.sort()
lucky_number.reverse()
friends2 = friends.copy
print(friends2)
friends.pop()
friends.clear()

print("strukture")
coordinates = [(4,5),(6,7),(80,50)]
print(coordinates[0])

print("finkcije")
def SayHi(ime,god):
    print("hello" , ime,str(god))

SayHi("mike",5)

def cube(num):
    return pow(num,3)
print(cube(3))

is_male = False
is_tall = True
if is_male and is_tall:
    print("you are male or tall")
elif is_male and not(is_tall):
    print("you are short male")
elif is_tall and not(is_male):
    print("you are not male, bur are tall")
else:
    print("you are not male not tall")