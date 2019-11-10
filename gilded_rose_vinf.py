class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                pass
            elif item.name == "Aged Brie":
                item.update_item(1,1)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.concert_update()
            elif item.name == "Conjured Mana Cake":
                item.update_item(-2,1)
            else:
                item.update_item(-1,1)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_item(self,qualit,sellin):
        if self.sell_in > 0:
            self.quality += qualit
        else:
            self.quality += 2 * qualit
        self.sell_in -= sellin
        if self.quality < 0:
            self.quality = 0
        if self.quality > 50:
            self.quality = 50
    
    def concert_update(self):
        if self.sell_in > 10:
            self.quality += 1
        elif self.sell_in > 5:
            self.quality += 2
        elif self.sell_in > 0:
            self.quality += 3
        else:
            self.quality = 0

        if self.quality > 50:
            self.quality = 50

        self.sell_in -= 1