import sys
from pathlib import Path
import os
from PIL import Image

source = sys.argv[1]
destination = sys.argv[2]

if not os.path.exists(destination):
    os.makedirs(destination)

c = 1
for filename in os.listdir(source):
    if filename.endswith('.jpg'):
        img = Image.open(f'{source}{filename}')
        name = 'converter_img'+str(c)+'.png'
        img.save(f'{destination}{name}', 'png')
        c += 1
        print(os.path.join(source, filename))
        print(os.path.join(destination, name))
        continue
    else:
        continue
