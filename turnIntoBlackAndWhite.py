from PIL import Image

file = "C://Users/ABC/20.jpg"
img = Image.open(file)

img = img.convert("L")
img.show()