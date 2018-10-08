
from PIL import Image
im = Image.open('intf.jpg')
print(im.format, im.size,im.mode)

im.thumbnail((200,100))
im.save('thumb.png','PNG')

print(im.format, im.size,im.mode)
