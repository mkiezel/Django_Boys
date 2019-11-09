from __future__ import print_function


PN = input('Podaj numer wersji:')
pmName = "gilded_rose_v" + PN


def test(days,version):
    Gildedrose = __import__(version)
    
    x = ""
    if __name__ == "__main__":
        items = [
                Gildedrose.Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
                Gildedrose.Item(name="Aged Brie", sell_in=2, quality=0),
                Gildedrose.Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
                Gildedrose.Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                Gildedrose.Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
                Gildedrose.Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
                Gildedrose.Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
                Gildedrose.Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
                Gildedrose.Item(name="Conjured Mana Cake", sell_in=3, quality=14),  # <-- :O
                ]


        import sys
        if len(sys.argv) > 1:
            days = int(sys.argv[1]) + 1
        for day in range(days):
            for item in items:
                x += str(item)
                x += "\n"
            Gildedrose.GildedRose(items).update_quality()
    return x
t=[]
t.append(test(7,"gilded_rose_v1"))
t.append(test(7,pmName))
t.append(test(15,"gilded_rose_v1"))
t.append(test(15,pmName))
t.append(test(25,"gilded_rose_v1"))
t.append(test(25,pmName))
t.append(test(40,"gilded_rose_v1"))
t.append(test(40,pmName))

for i in range (0,len(t)-1,2):
    print("test "+ str(int(i/2+1)) +":",end = "")
    if t[i] == t[i+1]:
        print(" Passed!")
    else:
        print(" Fail!")
