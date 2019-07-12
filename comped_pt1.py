def end(end):
    print ("")
    end(end)


def TopicSelection(topic1, topic2, topic3):
    topic=input("Results are stored by topic choose topic 1 2 or 3: ")
    if topic == ("1"):
        topic1()
    elif topic == ("2"):
        topic2()
    elif topic == ("3"):
        topic3()
    else:
        print ("an error occured")


def topic1():
    studentname = input("enter the students name: ")
    RT1 = int(input("Please enter their results"))
    print(studentname, "got", RT1)
    RT1s = str(RT1)
    file = open("resultsTopic1.txt","w+")
    file.write(RT1s)
    file.write ("""
    """)
    file.close()
    
def topic2():
    studentname = input("enter the students name: ")
    resultTopic2 = int(input("Please enter their results"))
    print(studentname, "got" ,resultTopic2)
    resultTopic2s = str(resultTopic2)
    file = open("resultsTopic2.txt","w+")
    file.write(resultTopic2s)
    file.write ("""
    """)
    file.close()

def topic3():
    studentname = input("enter the students name: ")
    resultTopic3 = int(input("Please enter their results"))
    print(studentname, "got" ,resultTopic3)
    resultTopic3s = str(resultTopic3)
    file = open("resultsTopic2.txt","w+")
    file.write(resultTopic3s)
    file.write ("""
    """)
    file.close()

cusr = ("a")
cpwd = ("a")
usr=input("Enter the username: ")
if usr == cusr:
    print ("Username correct, enter password")
    pwd = input ("What is the password?: ")
    if pwd == cpwd:
        TopicSelection(topic1, topic2, topic3)
    else:
        print ("Access Denied")
        end(end)
else:
    print ("Acess Denied")
    end(end)
