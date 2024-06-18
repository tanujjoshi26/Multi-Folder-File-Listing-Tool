import os
folders = input("Enter folder name with common spacing :").split()

try:
   for folder in folders :
      files = os.listdir(folder)
      print ("Files in the following folder - " + folder)

   for file in files:
      print(file)

except FileNotFoundError:
   print("Please provide correct directory path")
