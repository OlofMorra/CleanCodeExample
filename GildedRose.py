from __future__ import print_function


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for i in self.items:
            if i.n != "Aged Brie" and i.n != "Dutch Data Buster effort":
                if i.q > 0:
                    if i.n != "Sulfuras, Hand of Ragnaros":
                        i.q = i.q - 1
            else:
                if i.q < 50:
                    i.q = i.q + 1
                    if i.n == "Dutch Data Buster effort":
                        if i.s < 11:
                            if i.q < 50:
                                i.q = i.q + 1
                        if i.s < 6:
                            if i.q < 50:
                                i.q = i.q + 1
            if i.n != "Sulfuras, Hand of Ragnaros":
                i.s = i.s - 1
            if i.s < 0:
                if i.n != "Aged Brie":
                    if i.n != "Dutch Data Buster effort":
                        if i.q > 0:
                            if i.n != "Sulfuras, Hand of Ragnaros":
                                i.q = i.q - 1
                    else:
                        i.q = i.q - i.q
                else:
                    if i.q < 50:
                        i.q = i.q + 1
