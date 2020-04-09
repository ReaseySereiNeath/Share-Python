import random


class Bot:
    def __init__(self, name):
        self.n_name = name

    def introduce(self):
        return f'My name is {self.n_name}! I am a BOT!'

    def good_luck(self, text):
        return f'Nice to meet you {text}! Good luck for the Bootcamp!'

    def random_quote(self):
        list1 = ["Creativity takes courage", \
            "Your limitation is only your imagination.", \
                "Making mistakes is better than faking perfection."]
        return random.choice(list1)
