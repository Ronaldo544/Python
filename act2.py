file_read = open('Codingal.txt', 'r',encoding='utf-8')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt', 'w',encoding='utf-8')
file_write.write(" File in write mode....")
file_write.write("Hi! I am penguin. I am 1 yr. old")
file_write.close()

file_append = open('Codingal.txt', 'a',encoding='utf-8')
file_append.write("\n File in append mode....")
file_append.write("Hi! I am penguin. I am 1yr. old")
file_append.close()
