# def function(fname,lname):
#     print(f"Hii {fname} {lname}")


# print("Start")
# function(lname="Praneeth",fname="B")
# function("Praneeth","B")
# print("Stop")

# def square(num):
#     return num*num


# i=int(input('Enter a number'))
# print(f"The Square of {i} is {square(num=i)}")

try:
    age=int(input("Enter your age:"))
    print(age)
except ValueError:
    print("Invalid input!!")