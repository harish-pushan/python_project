import qrcode
img = qrcode.make('https://www.youtube.com/watch?v=BbeeuzU5Qc8')
type(img)  # qrcode.image.pil.PilImage
img.save("test.png")