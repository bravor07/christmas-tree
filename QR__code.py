import qrcode

url = "https://bravor07.github.io/christmas-tree/"
img = qrcode.make(url)
img.save("christmas_qr.png")
img.show()