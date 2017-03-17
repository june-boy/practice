import random

def helloworld():
	helloworld = "Hello World"
	heynow = "Hey Now"
	wassup = "Wassup!"
	howdydo = "Howdy do!"

	greetings = [helloworld, heynow, wassup, howdydo]
	result = random.choice(greetings)
	return result

def main():
	print( helloworld() )

main()
