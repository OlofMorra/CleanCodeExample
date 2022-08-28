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
        self.assertEquals(0, items[0].q, 'Item quality should be degraded to 0 from 1')


if __name__ == '__main__':
    unittest.main()
