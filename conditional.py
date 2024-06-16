# price=100
# good_credit=False

# if good_credit:
#     down_payment=0.1*price
# else:
#     down_payment=0.2*price
# print(f"Down payment:{down_payment}")

# weight = int(input("Weight:"))
# unit=input('(L)bs or (K)g:')
# if unit.upper()=='L':
#     converted=weight*0.45
#     print(f"You are {converted}kilos")
# else:
#     converted=weight/0.45
#     print(f"You are {converted} pounds")

# i=1
# while i<=5:
#     print('*'*i)
#     i+=1;

print("enter")
first=input()
first=first.lower()
if first=="help":
    print('''start - to start the car
    stop - to stop the car
    quit- to exit''')
    command=input()
    command=command.lower()
    if command=="start":
        print("Car started")
    elif command=="stop":
        print("Car sopped")
    elif command=="quit":
        print("Quitted")
    else:
        print("I dont understand")