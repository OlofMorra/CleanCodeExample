from __future__ import print_function


class GildedRose(object):
    ### Ongepaste informatie
    """
    A small inn that buys and sells goods. Goods are degrading in quality as they approach
    their sell date. Although, aged brie is not degrading over time. Also, Dutch Databusters
    effort increases in quality over time when it must be sold in 10 or 5 days.
    """

    MAX_ITEM_QUALITY = 50

    def __init__(self, items):
        self.items = items

    ### Te veel informatie in een functie
    ### Lengte naam gekoppeld aan grootte functie, korte naam met grote scope
    def update_quality(self):
        ### Incomplete en verouderde comment met oude design info
        """
        Updates the quality of items which degrades when sell data approaches
        :return: void
        """
        ### Beschrijvende namen
        for i in self.items:
            self.update_single_quality(i)
            i.decrement_sell_in()

    def update_single_quality(self, i):
        if i.n != "Aged Brie" and i.n != "Dutch Data Buster effort":
            if i.q > 0:
                if i.n != "Sulfuras, Hand of Ragnaros":
                    ### Overbodige comment
                    i.q = i.q - 1  # Decrement
        else:
            ### Duplicatie
            if i.q < self.MAX_ITEM_QUALITY:
                i.q = i.q + 1
                if i.n == "Dutch Data Buster effort":
                    ### Magisch nummer
                    if i.s < 11:
                        ### Duplicatie
                        if i.q < self.MAX_ITEM_QUALITY:
                            i.q = i.q + 1
                    ### Magisch nummer
                    if i.s < 6:
                        ### Duplicatie
                        if i.q < self.MAX_ITEM_QUALITY:
                            i.q = i.q + 1
                    ### Commented out code
                    # if i.s < 1:
                    #     if i.q < 50:
                    #         i.q = i.q + 1
        if i.s < 0:
            if i.n != "Aged Brie":
                if i.n != "Dutch Data Buster effort":
                    if i.q > 0:
                        if i.n != "Sulfuras, Hand of Ragnaros":
                            i.q = i.q - 1
                else:
                    i.q = i.q - i.q
            else:
                ### Duplicatie
                if i.q < self.MAX_ITEM_QUALITY:
                    i.q = i.q + 1

    ### Doet twee dingen, hoofdletters en name veranderen
    ### Output parameter item
    ### Flag parameter capitilize
    ### Dode functie
    ### Naam beschrijft capitilize niet
    def change_name_of_item(self, item, new_name, capitalize):
        if capitalize:
            item.n = new_name.capitalize()
        else:
            item.n = new_name
