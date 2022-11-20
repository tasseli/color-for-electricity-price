#Some reading if one is so inclined:
#docs https://arvydas.github.io/blinkstick-python/
#examples https://github.com/arvydas/blinkstick-python/wiki/BlinkStick-Pro%3A-Change-Color-of-a-Single-LED
#examples etc home https://github.com/arvydas/blinkstick-python/wiki
#blinkstick tutorials https://www.blinkstick.com/help/tutorials
#updating electricity price, brought by Juhku https://byproductmusic.com/JH/nordpool/nordpool_just_nyt.html

from blinkstick import blinkstick
from urllib import request
import ssl
import time, sys

for bstick in blinkstick.find_all():
    print ("Found device:")
    print ("    Manufacturer:  " + bstick.get_manufacturer())
    print ("    Description:   " + bstick.get_description())
    print ("    Serial:        " + bstick.get_serial())

bstick = blinkstick.find_first()

#set and get device info-block1 here
bstick.set_info_block1("Electricity price BlinkStick")
print (bstick.get_info_block1())

context = ssl._create_unverified_context()
line10 = '0'

def update_price():

    link = "https://byproductmusic.com/JH/nordpool/nordpool_just_nyt.html"
    f = request.urlopen(link, context=context)
    myfile = f.read()
    lineiterator = iter(myfile.splitlines())
    for i in range(0,9):
        next(lineiterator)
    line10 = next(lineiterator)
    line10 = line10.decode("utf-8")
    print(line10)
    f.close()
    sys.stdout.flush()

update_price()

def update_color():
    if (float(line10) > 40):
        bstick.set_color(name="red")
    if (float(line10) >= 20 and float(line10) < 40):
        bstick.set_color(name="orange")
    if (float(line10) < 20):
        bstick.set_color(name="green")
    sys.stdout.flush()

update_color()

while (True):
    time.sleep(60*60)
    update_price()
    update_color()
