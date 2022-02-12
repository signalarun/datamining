import re

shakes = open("in.txt", "r")

outFile = open('out.txt', 'a')

print("Starting")

# matches the pattern and gives the line that matches
for line in shakes:
    if re.match("(.*)CHI:(.*)|(.*)INV:(.*)", line):
        print(line)
        outFile.write(line)

outFile.close()
