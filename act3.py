file = open("Codingal.txt","r",encoding='utf-8')
counter = 0

Content = file.read()
CoList = Content.split("\n")

for i in CoList:
    if i:
        counter += 1
print("This is the number of lines in the file")
print(counter)