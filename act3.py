file1 = open('Codingal.txt',
             'r',encoding='utf-8')
file2 = open('CodingalUpdated.txt',
             'w',encoding='utf-8')

for line in file1.readlines():
    if not (line.startswith('Coding')):
        print(line)
        file2.write(line)
file2.close()
file1.close()


             
             