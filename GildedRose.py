from __future__ import print_function


class GildedRose(object):
    """
    A small inn that buys and sells goods. Goods are degrading in quality as they approach
    their sell date. Although, aged brie is not degrading over time. Also, Dutch Databusters
    effort increases in quality over time when it must be sold in 10 or 5 days.
    """

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """
        Updates the quality of items which degrades when sell data approaches
        :return: void
        """
        for i in self.items:
            if i.n != "Aged Brie" and i.n != "Dutch Data Buster effort":
                if i.q > 0:
                    if i.n != "Sulfuras, Hand of Ragnaros":
                        i.q = i.q - 1  # Decrement
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
                        # if i.s < 1:
                        #     if i.q < 50:
                        #         i.q = i.q + 1
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

    def change_name_of_item(self, item, new_name, capitalize):
        if capitalize:
            item.n = new_name.capitalize()
        else:
            item.n = new_name
