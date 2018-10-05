import random 

ask = input("Ask me any Yes or No question -- ")

for chance in range (1):

	chance = random.randint(1,2)

fiftyfifty =["Yes", "No"]

if chance == 1: 
	print(fiftyfifty[0])

elif chance == 2:
	print(fiftyfifty[1])

else:
	print("error - please try again")