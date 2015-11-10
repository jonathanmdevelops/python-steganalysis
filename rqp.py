import os
import sys
import math
import Image

"""
Performs the actual RQP analysis.
"""
def analyse(file_path, file_name):
  image = Image.open(file_path).convert('RGB')
  pixels = image.load()
  width, height = image.size

  unique_colours = set()

  for x in xrange(0, width):
    for y in xrange(0, height):
      unique_colours.add(pixels[x,y])

  possible_pairs = nCr(len(unique_colours),2)

  if possible_pairs < 1:
    ratio = 1
  else:
    ratio = float(get_colour_pairs(list(unique_colours))) / possible_pairs
  ratio *= 100
  print file_name + "\t \t " + str(ratio)

def nCr(n,r):
    if n < 2:
      return 0
    f = math.factorial
    return f(n) / (f(r) * f(n-r))

def get_colour_pairs(pairs):
  if len(pairs) < 2:
    return 0

  num_pairs = 0

  for i in xrange(0, len(pairs) - 1):
    for j in xrange(i+1, len(pairs)):
      if is_pair(pairs[i], pairs[j]):
        num_pairs += 1

  return num_pairs

def is_pair(c1,c2):
  r1, g1, b1 = c1[0],c1[1],c1[2]
  r2, g2, b2 = c2[0],c2[1],c2[2]

  return (r1-r2)**2 + (g1-g2)**2 + (b1-b2)**2 <= 3