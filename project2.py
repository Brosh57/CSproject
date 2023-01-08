#random number
import random

for num in range(3):
    print(random.randint(50, 100))
    print(random.random())


#random name
import random

members = ['sam','chuck','ben','bharath']
leader = random.choice(members)

print(leader)

#two random value
import random

class Dice:

    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second

dice = Dice()
print(dice.roll())