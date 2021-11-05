def checkValid(txt):
    if "@" in txt and "." in txt:
        return True
    return False
text = input("enter the email: ")
if checkValid(text):
    print("This is a valid email")
else:
    print("This is not a valid email")