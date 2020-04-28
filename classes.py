class Student:
    def __init__(self, name, major, gpa, is_on_Probatoion):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_Probatoion = is_on_Probatoion
    def onHonorRoll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
            
student1 = Student("Jim", "business", 3.1, False)
student2 = Student("karen", "art", 4.5, True)
print(student1.name)

class Questions:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    
questionsPrompts = [
    "what color are apples?\n(a) red/green\n(b) purple\n(c) orange\n\n",
    "what color are bananas?\n(a) red \n(b) yellow\n(c) blue\n\n",
    "what color are strawberries?\n(a) yellow\n(a) orange\n(c) purple/red\n\n"
]
questions = [
    Questions(questionsPrompts[0], "a"),
    Questions(questionsPrompts[1], "b"),
    Questions(questionsPrompts[2], "c"),
]

def test(questions):
    score = 0
    for quest in questions:
        answer = input(quest.prompt)
        if answer == quest.answer:
            score += 1
        
    print("you got " + str(score) + "/" + str(len(questions)) + " correct")

test(questions)


class Chef:

    def makeChicken(self):
        print("the chef makes a chicken")
    def makeSalad(self):
        print("the chef make a salad")
    def makeSpecialDish(self):
        print("the chef makes a special dish")

class ChineseChef(Chef):
    def makeRIce(self):
        print("the chinese chef makes a rice")



myChef = Chef()
myChef.makeChicken()

myChineseChef = ChineseChef()
myChineseChef.makeRIce()

for i in range(3):
    print("a")
print("b")
    