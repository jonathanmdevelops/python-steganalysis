import os
import Image

"""
Given an absolute path to an uncompressed PNG image
outputs and saves an L converted grayscale.
"""
def generate(file_path, file_name, extension):
  grayscale_image = Image.open(file_path).convert('L')
  pixels = grayscale_image.load()
  width, height = grayscale_image.size

  for x in xrange(0, width):
    for y in xrange(0, height):
    	bit_value = pixels[x,y] & 3
    	if bit_value == 3:
    		pixels[x,y] = 255
    	if bit_value == 2:
    		pixels[x,y] = 170
    	if bit_value == 1:
    		pixels[x,y] = 85
    	if bit_value == 0:
    		pixels[x,y] = 0


  if not os.path.exists("output"):
    os.makedirs("output")

  try:
    lsbfile_name = "output/" + file_name + "_lsb" + extension
    grayscale_image.save(lsbfile_name)
  except IOError:
    print "Error saving LSB image."