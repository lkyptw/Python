import os

# get current working directory
dir = os.getcwd()

for filename in os.listdir(dir):
	if filename.endswith(".py"):
		print(filename)


