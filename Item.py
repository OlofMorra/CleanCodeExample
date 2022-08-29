from __future__ import print_function
from enum import Enum

class Item:
    def __init__(self, name, sell_in, quality):
        self.n = name
        self.s = sell_in
        self.q = quality

    def __repr__(self):
        return "%s, sellIn: %s, quality: %s" % (self.n, self.s, self.q)

    def decrement_sell_in(self):
        if self.n != "Sulfuras, Hand of Ragnaros":
            self.s = self.s - 1