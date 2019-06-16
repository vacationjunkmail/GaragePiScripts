#!/usr/bin/env python3
import os

png_dir = '/var/www/relay/static/'

file_list = [f for f in os.listdir(png_dir) if f.endswith('png')]

[os.remove(os.path.join(png_dir,f)) for f in file_list]

if len(file_list):
	print("{} files removed".format(len((file_list))))

#for f in file_list:
	#f = os.path.join(png_dir,f)
	#print(f)
	
