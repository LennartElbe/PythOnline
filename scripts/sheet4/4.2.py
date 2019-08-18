#!/usr/bin/env python3
# -*- coding: utf-8 -*-

recipes = [("Sushi", ["Fisch", "Reis", "Nori"]),
           ("Sashimi", ["Fisch", "Reis"]),
           ("Pfannkuchen", ["Mehl", "Ei", "Milch"]),
           ("Burger", ["Broetchen", "Rind"]),
           ("Burger TS", ["Broetchen", "Rind", "Tomate", "Salat"]),
           ("Cheese Burger", ["Broetchen", "Rind", "Tomate", "Kaese"]),
           ("Gemischter Salat", ["Salat", "Tomate", "Gurke"])]


def cookable(xs):
    possibleDinner = []
    for i in recipes:
        food = i[0]
        ing = i[1]
        # check if all elements of ing are in xs
        allIn = True
        for x in ing:
            if x not in xs:
                allIn = False
        if allIn:
            possibleDinner.append(food)
    #print(possibleDinner)
    return possibleDinner


print(cookable(["Fisch", "Reis", "Tomate"]))
print(cookable(["Broetchen", "Tomate", "Gurke", "Salat", "Rind", "Broetchen"]))
