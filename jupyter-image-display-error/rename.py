import os
import glob

ext = input("Enter file extension type: ")

while not ext[0].isalpha():
    ext = input("Enter file extension type after the '.': ")
cap = ext[0].isupper()
n = len(ext)

if cap:
    ext = ext.lower()
else:
    ext = ext.upper()

files = glob.glob('*.'+ ext)
for file in files:
    print(file, 'converted to', file[:-n]+ext)
    os.rename(file, file[:-n]+ext)
    