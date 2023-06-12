import qrcode
qr = qrcode.QRCode(version=1, box_size=10, border=5)
data = input("Enter the url you want as a QR code: ")
filename = input("Enter name of the qrcode: ")
qr.add_data(data)
img = qr.make_image(fill_color="black", back_color="white")
img.save(filename+".png")
