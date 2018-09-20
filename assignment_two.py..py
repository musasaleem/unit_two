# Name: Musa Saleem
# Date: September, 20, 2018
# Last Modified: September, 20, 2018
# Description: ChatBot talks to a user & gets info about users car, price, rate & how long they are planning out a loan.
# Then using that information to find the monthly payment and total price for buying the car.
name = input("What's your name")
print("Hello there", name, "I am ChatBot")
located = input("Where are you located")
print(located, "! What a cool place to be from")
number = float(input("what is your favorite number"))
my_favorite_number = 3
print(number, "that is", number/my_favorite_number, "more than my favorite number")
car = input("What is your dream car")
print("I love that", car,)
price = float(input("What is the price on that bad boy?"))
print("Yikes", price, "dollars,that sure is expensive")
loan = float(input("So, how many years are you taking a loan out to pay for your car?"))
rate = float(input("What is the annual interest rate you expect to get the car for?"))
rate = rate/100/12
# Usually the rate is a whole number, dividing by 100 makes it a decimal,and dividing by 12 makes it a monthly payment
Monthly_Payment = (rate * price) / (1-(1+rate)**(-loan * 12))
print("your total expected monthly payment and total amount of money you would pay for is,", Monthly_Payment,
      "I Hope this is affordable for you, however, your total payment would be,", Monthly_Payment*12*loan)
