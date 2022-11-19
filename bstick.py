#Some reading if one is so inclined:
#docs https://arvydas.github.io/blinkstick-python/
#examples https://github.com/arvydas/blinkstick-python/wiki/BlinkStick-Pro%3A-Change-Color-of-a-Single-LED
#examples etc home https://github.com/arvydas/blinkstick-python/wiki
#blinkstick tutorials https://www.blinkstick.com/help/tutorials
#updating electricity price, brought by Juhku https://byproductmusic.com/JH/nordpool/nordpool_just_nyt.html

from blinkstick import blinkstick

for bstick in blinkstick.find_all():
    print ("Found device:")    
    print ("    Manufacturer:  " + bstick.get_manufacturer())
    print ("    Description:   " + bstick.get_description())
    print ("    Serial:        " + bstick.get_serial())

bstick = blinkstick.find_first()

#set and get device info-block1 here
bstick.set_info_block1("Electricity price BlinkStick")
print (bstick.get_info_block1())

import ssl
context = ssl._create_unverified_context()

from urllib import request 
link = "https://byproductmusic.com/JH/nordpool/nordpool_just_nyt.html"
f = request.urlopen(link, context=context)
myfile = f.read()
lineiterator = iter(myfile.splitlines())
for i in range(0,9):
    next(lineiterator)
line10 = next(lineiterator)
line10 = line10.decode("utf-8")
print(line10)

if (float(line10) >= 40):
    bstick.set_color(name="red")
if (float(line10) >= 20 and float(line10) < 40):
    bstick.set_color(name="orange")
if (float(line10) < 20):
    bstick.set_color(name="green")
