globalvar = "this is a global variable"

def function1 ():
    string1 = "This is stored in function 1"
    print(string1)

def function2 ():
    function1()
    print("that first string was called from function 1")
    globalvar = 5
    print(globalvar)

function2()
# print(string1)
# NameError: name 'string1' is not defined