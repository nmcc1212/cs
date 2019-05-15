file = open("login.txt","r")
line=file.readlines()

user = line[0]

pwd = line[1]


for x in range (4):
    guessedusrname = input ("What is the username")
    if user == guessedusrname:
        print ("Username correct, enter password")
        guessedpwd = input ("What is the password?")
        if guessedpwd == pwd:
            print ("Access Granted")
        else:
            print ("Access Denied")
    else:
        print ("Acess Denied")
