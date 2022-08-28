#!/usr/bin/env python

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


# In[21]:


class Item:
    def __init__(self, name, sell_in, quality):
        self.n = name
        self.s = sell_in
        self.q = quality

    def __repr__(self):
        return "%s, sellIn: %s, quality: %s" % (self.n, self.s, self.q)


# In[19]:


from __future__ import print_function

if __name__ == "__main__":
    print ("OMGHAI!")
    items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=85),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=85),
             Item(name="Dutch Data Buster effort", sell_in=15, quality=20),
             Item(name="Dutch Data Buster effort", sell_in=10, quality=49),
             Item(name="Dutch Data Buster effort", sell_in=5, quality=49),
             Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    days = 3
    
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()


# In[ ]:




