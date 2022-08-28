#!/usr/bin/env python
# coding: utf-8

# Source: https://github.com/emilybache/GildedRose-Refactoring-Kata

# Gilded Rose Requirements Specification
# ======================================
# 
# Hi and welcome to team Gilded Rose. As you know, we are a small inn with a prime location in a
# prominent city ran by a friendly innkeeper named Allison. We also buy and sell only the finest goods.
# Unfortunately, our goods are constantly degrading in quality as they approach their sell by date. We
# have a system in place that updates our inventory for us. It was developed by a no-nonsense type named
# Leeroy, who has moved on to new adventures. Your task is to add the new feature to our system so that
# we can begin selling a new category of items. First an introduction to our system:
# 
# 	- All items have a SellIn value which denotes the number of days we have to sell the item
# 	- All items have a Quality value which denotes how valuable the item is
# 	- At the end of each day our system lowers both values for every item
# 
# Pretty simple, right? Well this is where it gets interesting:
# 
# 	- Once the sell by date has passed, Quality degrades twice as fast
# 	- The Quality of an item is never negative
# 	- "Aged Brie" actually increases in Quality the older it gets
# 	- The Quality of an item is never more than 50, except "Sulfuras" which always has Quality 85
# 	- "Sulfuras", being a legendary item, never has to be sold or decreased in Quality
# 	- "Dutch Data Buster effort", like aged brie, increases in Quality as its SellIn value approaches, i.e. deadline approaches; Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but Quality drops to 0 after the deadline
# 
# We have recently signed a supplier of conjured items. This requires an update to our system:
# 
# 	- "Conjured" items degrade in Quality twice as fast as normal items
# 
# Feel free to make any changes to the UpdateQuality method and add any new code as long as everything
# still works correctly. However, do not alter the Item class or Items property as those belong to the
# goblin in the corner who will insta-rage and one-shot you as he doesn't believe in shared code
# ownership (you can make the UpdateQuality method and Items property static if you like, we'll cover
# for you).

# In[20]:


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




