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
        "name": ["Lloyd"],
        "homework":[],
        "quizzes":[],
        "tests":[],
        }
alice = {
        "name": ["Alice"],
        "homework":[],
        "quizzes":[],
        "tests":[],
        }
tyler = {
        "name": ["Tyler"],
        "homework":[],
        "quizzes":[],
        "tests":[],
        }


print (lloyd["name"])
