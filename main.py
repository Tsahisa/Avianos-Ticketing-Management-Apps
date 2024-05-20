import random
import string


print("==============AVIANOS================")
print("Welcome to our very narcistic Ticketing Apps, heh. You can choose just two departs from here, bozzo~")

depart = input("So... Where are you going too? : [Choose with number 1,2]")
print("1. Domestic Departure")
print("2. National Departure")

def passport():
    letters = string.ascii_uppercase
    digits = string.digits
    idPass = random.choice(letters) + "".join(random.choices(digits, k=9))
    return idPass

if depart == "1":
    country = input("What's country? : [You can go to anywhere. Feel free to input any country]")
    bioName = input("Complete Name? : ")
    bioDom = input("Your fellow city : ")
    bioPass = passport

if depart == "2":
    country = input("What's country? : [You can go to anywhere. Feel free to input any country]")
    bioName = input("Complete Name? : ")
    bioDom = input("Your fellow city : ")
    

print("==============TOTAL ORDER================")
print("So... You wanna go to : ", country)
print("Your name is : ", bioName)
print("You're from : ", bioDom)
print("And your passport is : ", bioPass)