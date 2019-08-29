from PIL import Image

img = Image.open("../../images/lab-09/check3-3orig.png")

img = img.convert('L')
img = img.resize((28,28))
img.save("../../images/lab-09/check3-3.png")
