import random2
from random2 import choice


class Toss:
    @staticmethod
    def coin_toss():
        # coin = random2.choice(["Heads", "Tails"])
        coin = choice(["Heads", "Tails"])
        print(coin)


coin1 = Toss()
coin1.coin_toss()
