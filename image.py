from PIL import Image, ImageFilter

img = Image.open(r"./image_env/pikachu.jpg")

print(img.size)
print(img.format)
print(img.mode)
filter_image = img.filter(ImageFilter.BoxBlur(radius=7))
print(filter_image.save('blur_pikachu.png', 'png'))

img1 = Image.open(r"./image_env/bulbasaur.jpg")
convert_img1 = img1.convert('P')
convert_img1.show()
convert_img3 = img1.convert('L')
convert_img3.show()
convert_img2 = img1.convert('1')
convert_img2.show()

img2 = Image.open(r"./image_env/charmander.jpg")
print(img2.size)
rotate_img = img2.rotate(90)
rotate_img.show()
resize_img = img2.resize((160, 140))
resize_img.show()
print(resize_img.size)

img3 = Image.open(r"./image_env/squirtle.jpg")
img3.show()
crop_pixle = (100, 80, 400, 400)
crop_img = img3.crop(crop_pixle)
crop_img.show()
crop_img.save("crop_squirtle.png", "png")

img4 = Image.open(r"./image_env/pikachu.jpg")
img4.thumbnail((400, 400))
img4.save('thumbnail.png', 'png')
print(img4.size)
