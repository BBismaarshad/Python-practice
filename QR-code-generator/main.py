import qrcode as qr


# Create QR code for your portfolio website

img = qr.make("https://my-wesite-kappa.vercel.app/")
img.save("BismaArshad_portfolio.png")