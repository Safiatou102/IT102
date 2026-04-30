#!/usr/bin/env python3
# Sample script that writes to a file
# By Safiatou t - instructings
# Script 1 - collect info and save to hackme.txt

'''
Write ascript that saves user input into a file, that data about the user
'''

#These variables are questions that need to be answered
name = input("What is your name? ")
color = input("What is your favorite color? ")
pet = input("What is your first pets pet? ")
maiden = input("What is your mother maiden name? ")
school = input("What elementary school did you intend? ")

with open("hackme.txt", "w") as file:
     file.write(f"Name: {name}\n")
     file.write(f"Favorite Color: {color}\n")
     file.write(f"First Pet: {pet}\n")
     file.write(f"Mothers maiden Name: {maiden}\n")
     file.write(f"Elementary School: {school}\n")

print("Saved to hakme.txt great work!")
