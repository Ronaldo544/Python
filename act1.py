file= open('Codingal.txt', 'r',encoding='utf-8')
print(file.read())
file.close()

file = open('Codingal.txt', 'r',encoding='utf-8')
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open('Codingal.txt', 'a',encoding='utf-8')
file.write("Hi! I am Penguin and I am 1 yr old.")
file.close()