# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.concert_update()
                item.item_quality_range_check()
                continue
            
            item.sell_in -= 1
            
            if item.name == "Aged Brie":
                item.quality += 1
            else:
                item.quality -= 1
            if item.name == "Conjured Mana Cake":
                item.quality -= 1
            
            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    item.quality +=  1  
                else:
                    item.quality -= 1
                if item.name == "Conjured Mana Cake":
                    item.quality -= 1

            item.item_quality_range_check()                   



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def item_quality_range_check(self):
        if self.quality > 50:
            self.quality = 50
        if self.quality < 0:
            self.quality = 0 

    def concert_update(self):
        self.quality += 1
        if self.sell_in < 11:
            self.quality += 1
        if self.sell_in < 6:
            self.quality += 1
        self.sell_in -= 1
        if self.sell_in < 0:
            self.quality = 0
        