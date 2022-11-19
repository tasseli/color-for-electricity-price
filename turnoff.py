#Some reading if one is so inclined:
#docs https://arvydas.github.io/blinkstick-python/
#examples https://github.com/arvydas/blinkstick-python/wiki/BlinkStick-Pro%3A-Change-Color-of-a-Single-LED
#examples etc home https://github.com/arvydas/blinkstick-python/wiki
#blinkstick tutorials https://www.blinkstick.com/help/tutorials
#updating electricity price, brought by Juhku https://byproductmusic.com/JH/nordpool/nordpool_just_nyt.html

from blinkstick import blinkstick

bstick = blinkstick.find_first()
bstick.turn_off()
