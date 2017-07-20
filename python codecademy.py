# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:06:04 2017

@author: elot1z6
"""

#%% Dictionaries, lists, functions and str.format()

prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
        }

stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
        }

total = 0

print('Before shopping the stock is {}' .format(stock))


for key in prices:
    print (key)
    print ('price: {}' .format(prices[key]))
    print ('stock: {}' .format(stock[key]))
    
    total = total + (prices[key] * stock[key])
    
print (total)


shopping_list = ["banana","orange","apple"]

    
def compute_bill(food):
     total = 0
     for x in food:
         if stock[x] > 0: 
             total += prices[x]
             stock[x] = stock[x] - 1
     return total
 
compute_bill(shopping_list)
print('After shopping the stock is {}' .format(stock))

#list inside a dictionary
animal_sounds = {
    "cat": ["meow", "purr"],
    "dog": ["woof", "bark"],
    "fox": [],
}
print (animal_sounds["cat"])

#%% Lesson Number One

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

for x in students:
        print ("Student name is {}" .format(x["name"]), "and their Homework scores are {}" .format(x["homework"]))
        print ("Homework scores are {}" .format(x["homework"]))
        print ("Quiz scores are {}" .format(x["quizzes"]))
        print ("Test scores are {}" .format(x["tests"]))


def average(numbers):
    total = sum(numbers)
    total = float(total)
    total = total / len(numbers)
    return total

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    weighted_avg = 0.10*homework + 0.30*quizzes + 0.6*tests
    return weighted_avg

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "F"
get_letter_grade(get_average(lloyd))
#print (get_letter_grade(get_average(lloyd)))


#print (lloyd["name"])
