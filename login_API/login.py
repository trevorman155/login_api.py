

granted= False
def grant():
    global granted

granted= True
def login(name, password):
    file=open("user details.txt.txt","r")
    for i in file:
        a,b=i.split(",")
        b=b.strip()
    print(a,b)

    if (a == name and b == password):
        success= True
        breakpoint()
    file.close()
    if (success):
        print("Login Successful!!")
        grant()
    else:
        print("wrong username or password!")
def register(name,password):
    file=open("user details.txt.txt", "a")
    file.write("/n"+name+","+password)
    file.close()
    grant()
def access(option):
    global name
    if(option=="login"):
        name = input("Enter your name:")
        password = input("Enter your password:")
        login(name, password)
    else:
        print("Enter your name and password")
        name = input("Enter your name:")
        password = input("Enter your password:")
        register(name, password)


def begin():
    global option
    print("Welcome to Trevor's Programming Club")
    option=input("Login or Register (login,register):")
    if(option!="login" and option!="reg"):
        begin()
begin()
access('option')
if (granted):
    print("Welcome to Trevor's Programming Club")
    print("### User Details ###")
    print("Username:",name)
















