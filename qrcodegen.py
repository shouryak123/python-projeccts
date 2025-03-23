import qrcode
import qrcode.constants

#qr code generated from a url that is user input and saved as an image file


def make_qrcode(url):
    qr =qrcode.QRCode(
        version = 5,#size of the qr code 1 being the smallest
        error_correction =qrcode.constants.ERROR_CORRECT_H,#low error correction
        box_size =10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)
   
    img =qr.make_image(fill="black",back_color = "white")
    img.save("qrcode.png")

    img.show()

urls =input("enter urls seperated with commas: ").split(",")
urls=[url.strip() for url in urls]
for url in urls:
    make_qrcode(url)
