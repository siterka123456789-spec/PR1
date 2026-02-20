from prompt import string
import random

def main():
	print("Welcome to the VD-games!")
	name = string("May I have your name? ")
	print(f"Hello, {name}!")
	print('Answer "yes" if the number is even, otherwise answer "no".')
	for _ in range(3):
		number = random.randint(1, 100)
		print(f"Question: {number}")
		answer = string("Your answer: ")
		correct = "yes" if number % 2 == 0 else "no"
		
		if answer != correct:
			print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'")
			print(f"Let's try again, {name}")
			return
		print("Correct!")
	print(f"Congratulations. {name}")
