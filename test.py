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
            #print("-------- day %s --------" % day)
            for item in items:
                #print(item)
                x += str(item)
                x += "\n"
            #print("")
            Gildedrose.GildedRose(items).update_quality()
    return x

a = test(7,"gilded_rose_v1")
ap = test(7,pmName)
b = test(15,"gilded_rose_v1")
bp = test(15,pmName)
c = test(25,"gilded_rose_v1")
cp = test(25,pmName)
d = test(40,"gilded_rose_v1")
dp = test(40,pmName)

print("test 1:",end = "")
if a == ap:
    print(" Passed")
else:
    print(" Fail")

print("test 2:",end = "")
if b == bp:
    print(" Passed")
else:
    print(" Fail")

print("test 3:",end = "")
if c == cp:
    print(" Passed")
else:
    print(" Fail")

print("test 4:",end = "")
if d == dp:
    print(" Passed")
else:
    print(" Fail")
