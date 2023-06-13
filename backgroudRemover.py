from rembg import remove
from PIL import Image

input_path = 'images/img_01.png'
output_path = 'images/modImg_01.png'

inp = Image.open(input_path)
output = remove(inp)

output.save(output_path)