from blinkstick import blinkstick

for bstick in blinkstick.find_all():
    print ("Found device:")    
    print ("    Manufacturer:  " + bstick.get_manufacturer())
    print ("    Description:   " + bstick.get_description())
    print ("    Serial:        " + bstick.get_serial())

for bstick in blinkstick.find_all():
    bstick.set_random_color()
    print (bstick.get_serial())

for bstick in blinkstick.find_all():
    bstick.turn_off()
    print (bstick.get_serial() + " turned off")

bstick = blinkstick.find_first()

#set and get device info-block1 here
bstick.set_info_block1("Kitchen BlinkStick")
print (bstick.get_info_block1())

import ssl
# This bypasses need for cert when using this context
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
#    bstick.set_random_color()