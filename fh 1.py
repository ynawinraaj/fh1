# open file & read it's content
file=open('sample.txt','r')
print(file.read())
file.close()

# open file & read it's begining first 8 charecter
file=open('sample.txt','r')
print(file.read(8))
file.close()

#append your name and age
file=open('sample.txt','a')
file.write("my name is raaj my age is 14")
file.close()