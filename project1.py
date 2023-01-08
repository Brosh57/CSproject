import qrcode

url = input("Enter url for qrcode: ")
img = qrcode.make(url)
img.save("youtubeQR.jpg")
