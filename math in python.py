# +, -, *, /
inputtype = input("Enter the operation you want to perform:- ")
if inputtype == "add":
    inputvar = int(input("Enter the first digit you add:- "))
    inputvar2 = int(input("Enter the second digit you add:- "))

    print("The addition of the two no is:- ", inputvar + inputvar2)

elif inputtype == "sub":
    inputvar = int(input("Enter the first digit you subtract:- "))
    inputvar2 = int(input("Enter the second digit you subtract:- "))

    print("The subtract of the two no is:- ", inputvar - inputvar2)

elif inputtype == "mul":
    inputvar = int(input("Enter the first digit you multiply:- "))
    inputvar2 = int(input("Enter the second digit you multiply:- "))

    print("The multiply of the two no is:- ", inputvar * inputvar2)

elif inputtype == "div":
    inputvar = int(input("Enter the first digit you divid:- "))
    inputvar2 = int(input("Enter the second digit you divid:- "))

    print("The divid of the two no is:- ", inputvar / inputvar2)

else:
    print("The task you typed cannot be performed.")

input()
