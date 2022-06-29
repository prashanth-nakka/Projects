# Libraries
import pyqrcode

# Creating QR_Code for  url/context
qr_code = pyqrcode.create("https://github.com/prashanth-nakka?tab=repositories")

# creating QR_Code as .png format
qr_code.png("repo.png", scale=8)

