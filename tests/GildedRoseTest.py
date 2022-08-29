import unittest

from GildedRose import GildedRose
from Item import Item


class GildedRoseTest(unittest.TestCase):
    def test_quality_degradation_when_sell_in_date_passed(self):
        # Given
        items = [Item('TestItem', -1, 10)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals('TestItem', items[0].n, 'We should test an item called "TestItem"')
        self.assertEquals(-2, items[0].s, 'SellIn must be decreased by one')
        self.assertEquals(8, items[0].q)

    def test_quality_degradation_when_sell_in_date_not_passed(self):
        # Given
        items = [Item('TestItem', 1, 10)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(9, items[0].q)

    @unittest.expectedFailure
    def test_quality_of_item_becomes_negative_raises_error(self):
        # Given
        items = [Item('TestItem', 1, 0)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        # Expect failure

    def test_quality_of_item_becomes_zero(self):
        # Given
        items = [Item('TestItem', 1, 1)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(0, items[0].q, 'Item quality should be degraded by 1')

    def test_aged_brie_increases_in_quality_before_sell_in_date_passed(self):
        # Given
        items = [Item('Aged Brie', 1, 1)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(2, items[0].q, 'Item quality should be increased by 1')

    def test_aged_brie_increases_in_quality_after_sell_in_date_passed(self):
        # Given
        items = [Item('Aged Brie', 0, 1)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(3, items[0].q, 'Item quality should be increased by 2')

    def test_quality_does_not_increase_above_fifty(self):
        # Given
        items = [Item('Aged Brie', 1, 50)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(50, items[0].q, 'Item quality should remain 50')

    def test_sulfuras_quality_does_not_change(self):
        # Given
        sulfuras_quality = 85
        items = [Item('Sulfuras, Hand of Ragnaros', 1, sulfuras_quality)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(sulfuras_quality, items[0].q, 'Item quality should remain 85')

    def test_sulfuras_sell_in_does_not_change(self):
        # Given
        sell_in = -1
        items = [Item('Sulfuras, Hand of Ragnaros', sell_in, 85)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(sell_in, items[0].s, 'SellIn does not change')

    def test_dutch_databusters_quality_increases_by_one(self):
        # Given
        items = [Item('Dutch Data Buster effort', 11, 1)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(2, items[0].q, 'Quality should increase by one')

    def test_dutch_databusters_quality_increases_by_two(self):
        # Given
        items = [Item('Dutch Data Buster effort', 10, 1)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(3, items[0].q, 'Quality should increase by one')

    def test_dutch_databusters_quality_increases_by_two(self):
        # Given
        items = [Item('Dutch Data Buster effort', 10, 1)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(3, items[0].q, 'Quality should increase by two')

    def test_dutch_databusters_quality_increases_by_three(self):
        # Given
        items = [Item('Dutch Data Buster effort', 5, 1)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(4, items[0].q, 'Quality should increase by two')

    def test_dutch_databusters_quality_drops_to_zero_after_deadline(self):
        # Given
        items = [Item('Dutch Data Buster effort', 0, 10)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(0, items[0].q, 'Quality should drop to zero')

    def test_conjured_items_degrades_by_two_before_sell_in_date(self):
        # Given
        items = [Item('Conjured item', 1, 10)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(8, items[0].q, 'Quality should decrease by two')

    def test_conjured_items_degrades_by_four_after_sell_in_date(self):
        # Given
        items = [Item('Conjured item', 0, 10)]
        gilded_rose = GildedRose(items)

        # When
        gilded_rose.update_quality()

        # Then
        self.assertEquals(6, items[0].q, 'Quality should decrease by four')


if __name__ == '__main__':
    unittest.main()
