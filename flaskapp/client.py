# импортируем нужные модули
import os
from io import BytesIO
import base64
img_data = None
# создаем путь к файлу (для кроссплатформенности, например)
path = os.path.join('./static','image0008.png')
11
# читаем файл и енкодируем его в строку base64
with open(path, 'rb') as fh:
img_data = fh.read()
b64 = base64.b64encode(img_data)
