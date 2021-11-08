import json
import random
import random as rand
from typing import Sequence
from datetime import datetime
from colors import Colors
import numpy as np
import pandas as pd


class Item:
    def __init__(self, name: str, star: int, item_type: str):
        self.name = name
        self.star = star
        self.item_type = item_type

    @staticmethod
    def from_json(json_data: Sequence):
        if isinstance(json_data, list):
            json_data: dict = rand.choice(json_data)
        name = json_data['name']
        star = json_data['star']
        item_type = json_data['type']
        return Item(name, star, item_type)

    def __str__(self):
        return self.name


def to_weapon(name: str, star: int):
    return Item(name, star, "weapon")


def to_character(name, star: int):
    if name is isinstance(name, tuple):
        return Item(rand.choice(name), star, "character")
    return Item(name, star, "character")


def fifty_fifty():
    return True if rand.randint(0, 1) == 1 else False


class Wish:
    # Declare the different items one can get from the event banner
    THREE_STAR_WEAPONS = ("Amber Catalyst", "Black Tassel", "Bloodtainted "
                                                            "Greatsword",
                          "Cool Steel", "Dark Iron Sword", "Debate Club",
                          "Ebony Bow", "Emerald Orb", "Ferrous Shadow",
                          "Fillet Blade", "Halberd", "Harbinger of Dawn",
                          "Magic Guide", "Messenger", "Otherworldly Story",
                          "Quartz", "Raven Bow", "Recurve Bow",
                          "Sharpshooter's Oath", "Skyrider Greatsword",
                          "Skyrider Sword", "Slingshot", "Thrilling Tales of "
                                                         "Dragon Slayers",
                          "Traveler's Handy Sword", "Twin Nephrite", "White "
                                                                     "Iron "
                                                                     "Greatsword",
                          "White Tassel")

    FOUR_STAR_WEAPONS = ("Dragon's Bane", "Eye of Perception", "Favonius "
                                                               "Codex",
                         "Favonius Greatsword", "Favonius Lance",
                         "Favonius Sword", "Favonius Warbow", "Lion's Roar",
                         "Rainslasher", "Rust", "Sacrificial Bow",
                         "Sacrificial Fragments", "Sacrificial Greatsword",
                         "Sacrificial Sword", "The Bell", "The Flute",
                         "The Stringless", "The Widsith")
    FOUR_STAR_CHARACTERS = ("Fischl", "Diona", "Chongyun")
    FIVE_STAR_WEAPONS = ("IDK LOL", "Wolf's Gravestone")
    FIVE_STAR_CHARACTERS = ("Diluc", "Mona", "Keqing", "Qiqi")
    # This assumes the user is purchasing the most expensive
    # Genesis Crystals pack (w/o the first-time bonus), which is 6,480 crystals
    # for $99.99, which provides 80.81 crystals per dollar according to the
    # Genshin Impact Fandom wiki, or, rounding up, $1.98 per wish
    PRICE_PER_WISH = 1.98

    def __init__(self):
        pass
        # self.five_stars_ = self.five_stars
        # with open("items.json", "r") as file:
        #     json_obj = json.load(file)
        #     choices = json_obj['five_stars']['characters']
        #     result = Item.from_json(choices)
        #     print(result)

    @staticmethod
    def char_or_weapon():
        return

    @staticmethod
    def random_weighted(items, rates, size=1):
        return int(rand.choices(list(items), rates, k=size)[0])

    @property  # Getter for 3 star
    def three_stars(self):
        # json_dict = {}
        # json_dict['three_stars']['weapons'] = []

        return [Item(name, 3, "weapon") for name in self.THREE_STAR_WEAPONS]

    @property  # Getter for 4 star
    def four_stars(self):
        _four_stars = [Item(name, 4, "weapon") for name in
                       self.FOUR_STAR_WEAPONS] + \
                      [Item(name, 4, "character") for name in
                       self.FOUR_STAR_CHARACTERS]
        return _four_stars

    @property  # Getter for 5 star
    def five_stars(self):
        _five_stars = [Item(name, 5, "weapon") for name in
                       self.FIVE_STAR_WEAPONS] + \
                      [Item(name, 5, "character") for name in
                       self.FIVE_STAR_CHARACTERS]
        return _five_stars

    def rand_three_star(self):
        # Will always return a weapon
        return rand.choice(self.three_stars)

    def rand_four_star(self):
        return rand.choice(self.four_stars)

    def rand_five_star(self):
        return rand.choice(self.five_stars)


class BannerWish(Wish):
    FOUR_STAR_CHARACTERS_EVENT = "Kujou Sara", "Sucrose", "Xinyan"
    FIVE_STAR_CHARACTER_EVENT = "Raiden Shogun"

    BASE_RATES = {
        3: 94.3,
        4: 5.1,
        5: 0.6
    }

    SOFT_PITY_RATES = {1: 0.600, 2: 0.596, 3: 0.592, 4: 0.591, 5: 0.586,
                       6: 0.582, 7: 0.579, 8: 0.575, 9: 0.571, 10: 0.568,
                       11: 0.565, 12: 0.561, 13: 0.558, 14: 0.554, 15: 0.552,
                       16: 0.549, 17: 0.545, 18: 0.541, 19: 0.539, 20: 0.536,
                       21: 0.531, 22: 0.528, 23: 0.525, 24: 0.523, 25: 0.519,
                       26: 0.517, 27: 0.513, 28: 0.511, 29: 0.507, 30: 0.503,
                       31: 0.501, 32: 0.498, 33: 0.495, 34: 0.491, 35: 0.489,
                       36: 0.486, 37: 0.483, 38: 0.480, 39: 0.477, 40: 0.475,
                       41: 0.471, 42: 0.469, 43: 0.467, 44: 0.464, 45: 0.461,
                       46: 0.457, 47: 0.456, 48: 0.453, 49: 0.448, 50: 0.447,
                       51: 0.445, 52: 0.442, 53: 0.439, 54: 0.437, 55: 0.434,
                       56: 0.430, 57: 0.428, 58: 0.426, 59: 0.423, 60: 0.420,
                       61: 0.418, 62: 0.416, 63: 0.413, 64: 0.410, 65: 0.408,
                       66: 0.406, 67: 0.404, 68: 0.401, 69: 0.399, 70: 0.396,
                       71: 0.393, 72: 0.392, 73: 0.388, 74: 0.387, 75: 0.384,
                       76: 20.627, 77: 13.946, 78: 9.429, 79: 6.375,
                       80: 4.306, 81: 2.914, 82: 1.970, 83: 1.332, 84: 0.901,
                       85: 0.608, 86: 0.411, 87: 0.278, 88: 0.187, 89: 0.126,
                       90: 0.265}

    def __init__(self):
        super().__init__()
        self.wish = super()
        self.five_star_pity = 0
        self.four_star_pity = 0
        self.guarantee_four_star = False
        self.guarantee_five_star = False
        self.guarantee_four_star_event = False
        self.guarantee_five_star_event = False
        self.money_spent = 0.0
        self.three_stars_earned = []
        self.four_stars_earned = []
        self.five_stars_earned = []
        self.history = pd.DataFrame(
            columns=['Item Type', 'Item Name', 'Time Received'])
        # TODO INIT PANDAS

    def get_rates(self) -> dict:
        dynamic_rates = self.BASE_RATES.copy()
        dynamic_rates[5] = self.SOFT_PITY_RATES[self.five_star_pity + 1]
        print(f'{self.five_star_pity+1=} and'
              f' {self.SOFT_PITY_RATES[self.five_star_pity+1]=}')
        return dynamic_rates

    # @classmethod
    # def nth_pull_5_star_prob(cls, probability_percent: float):
    #     if 0.0 < probability_percent > 1.0:
    #         return False
    #     return random.random() < (probability_percent / 100)

    # @classmethod
    # def five_star_nth_pull(cls, n):
    #     return chance(SOFT_PITY_RATES[n])

    @classmethod
    def rand_four_star_character_event(cls):
        return to_character(rand.choice(cls.FOUR_STAR_CHARACTERS_EVENT), 4)

    @classmethod
    def five_star_character_event(cls):
        return to_character(cls.FIVE_STAR_CHARACTER_EVENT, 5)

    @staticmethod
    def display_wish(item: Item):
        if item.star == 5:
            print(Colors.fg.yellow + str(item) + Colors.reset)
            return
        if item.star == 4:
            print(Colors.fg.purple + str(item) + Colors.reset)
            return
        if item.star == 3:
            print(Colors.fg.lightblue + str(item) + Colors.reset)
            return
        print(Colors.fg.red + item + Colors.reset)

    # def check_pity(self):
    #     if self.four_star_pity >= 9:
    #         self.guarantee_four_star = True
    #     if self.five_star_pity >= 90:
    #         self.guarantee_five_star = True

    def get_rarity(self):
        # Check pity
        if self.four_star_pity + 1 == 9:
            self.guarantee_four_star = False
            return 4
        if self.five_star_pity + 1 == 90:
            self.guarantee_five_star = False
            return 5

        # TODO: Test for this
        if self.four_star_pity + 1 > 9:
            Exception('LOLL HELP')
        if self.five_star_pity + 1 > 90:
            Exception("BRO THIS IS BAD")

        # If no pity, randomize as normal
        RATES = self.get_rates()
        RARITIES = RATES.keys()
        PROBABILITY = RATES.values()

        return self.wish.random_weighted(RARITIES, PROBABILITY)

    def return_wish(self):
        self.money_spent += self.wish.PRICE_PER_WISH
        # Check pity
        rarity = self.get_rarity()

        # Deliver guarantees or wish based on rarity
        if rarity == 5:
            # Increase 4 star pity and reset 5 star pity
            self.four_star_pity += 1
            self.five_star_pity = 0

            # 50% chance to get a rate-up character
            if fifty_fifty() or self.guarantee_five_star_event:
                self.guarantee_five_star_event = False  # Pity is used
                return self.five_star_character_event()
            else:
                # If no rate-up character, guarantee rate-up and return standard
                # 5 star
                self.guarantee_five_star_event = True
                return self.wish.rand_five_star()

        if rarity == 4:
            # Reset 4 star pity and increase 5 star pity
            self.four_star_pity = 0
            self.five_star_pity += 1

            # 50% chance to get a rate-up character
            if fifty_fifty() or self.guarantee_four_star_event:
                self.guarantee_four_star_event = False  # Pity is reset
                return self.rand_four_star_character_event()
            else:
                # If no rate-up character, guarantee rate-up and wish as normal
                self.guarantee_four_star_event = True
                return self.wish.rand_four_star()

        # If above failed, give a 3 star
        if rarity == 3:
            # Increase 4 star and 5 star pity
            self.four_star_pity += 1
            self.five_star_pity += 1

            # Return a 3 star weapon
            three_star = self.wish.rand_three_star()
            self.number_of_three_stars_wished += 1

            return three_star

    def wish_1(self):
        self.display_wish(self.return_wish())

    def wish_10(self):
        wishes: list[Item] = []
        for i in range(11):
            wishes.append(self.return_wish())
        wishes.sort(key=lambda x: x.star, reverse=True)
        for wish in wishes:
            self.display_wish(wish)

    def log_wish(self, item: Item):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history = self.history.append({'Item Type': item.item_type,
                                            'Item Name': item.name,
                                            'Time Received': now},
                                           ignore_index=True)

    def print_history(self):
        print(self.history)
