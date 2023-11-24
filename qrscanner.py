import qrcode

myqr = qrcode.make("https://youtu.be/IUQVO97zcE0?si=tiPD5MwQONjDUEWN")
myqr.save("myqr.png")