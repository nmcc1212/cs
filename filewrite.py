grade = str(78)
grade2 = str(50)

file = open("test.txt","w")

file.write(grade)
file.write ("""
""")
file.write(grade2)

file.close()

file2 = open("test.txt","r") 
print (file2.read())

file2.close() 
