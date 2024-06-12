number=['4','44','63','42']

import utils
print(utils.find_max(number))

from utils import find_min
print(find_min(number))

import random

for i in range(3):
    print(random.random())
    print(random.randint(10,20))

member=['praneeth','vicly','sv']
leader=random.choice(member)
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice=Dice()
print(dice.roll())

from pathlib import Path

path=Path()
for file in path.glob("*"):
    print(file)