import sys
import os
import lsb_generator as lsb_gen
import rqp as RQP

"""
Given an absolute path to an uncompressed PNG image the program
outputs the RQP analysis statistic.
"""

if len(sys.argv) < 2:
	print "An image path must be supplied as an argument."
	sys.exit()

file_path = str(sys.argv[1])

if not os.path.isfile(file_path):
  print file_path + " is not a file."
  sys.exit()

path_sections = os.path.splitext(os.path.basename(file_path))
file_name = path_sections[0]

extension = ".png" if len(path_sections) > 1 else path_sections[1]

lsb_gen.generate(file_path, file_name, extension)
RQP.analyse(file_path, file_name)