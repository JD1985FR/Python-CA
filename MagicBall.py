import random

name = "David"
question = "I am an animal"
answer = ""

random_number = random.randint(1, 9)

  #print(random_number)

if random_number == 1:
  answer = "Yes"
elif random_number == 2:
  answer = "Yes - definitely"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Out look not so good"
elif random_number == 9:
  answer = "It is decidedly so"
else:
  answer = "Error"

print(name + " asks : " + question)
print("Magic 8-Ball's answer : " + answer)