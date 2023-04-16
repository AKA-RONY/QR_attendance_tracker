# Student data will be fetched from the Database

def matchCreds(username, password):
    if username == "123" and password == "student":
        return 0
    elif username == "123" and password == "teacher":
        return 1
    elif username == "123" and password == "admin":
        return 2

