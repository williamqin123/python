

from __future__ import division
import random

totalMoney = 0

def round(bet):


    global totalMoney

    money = 0

    slot1 = random.randint(0, 1)
    slot2 = random.randint(0, 1)
    slot3 = random.randint(0, 1)
    slot4 = random.randint(0, 1)

    if slot1 == 1 and slot2 == 1:
        money += 1

    if slot1 == 1:
        money += 1

    if slot2 == 0:
        money -= 1

    if (slot2 == 0 and slot3 == 0) or (slot3 == 0 and slot4 == 0):
        money -= 4

    if slot3 == 0:
        money -= 1

    if slot2 == 1:
        money += 1

    if slot2 == 1 and slot4 == 1:
        money += 2


    willDoMagicFlip = random.randint(0, 1)

    if willDoMagicFlip:

        magicFlip = random.randint(0, 1)
        if magicFlip == 1:
            money = money + bet

        elif magicFlip == 0:
            money = money - bet

    totalMoney += money

for x in range(0, 10000):
    round(10)

print("YOUR AVERAGE MONEY:" + str(totalMoney / 10000))