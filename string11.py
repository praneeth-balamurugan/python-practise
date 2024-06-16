# name = input('whats your name')
# year=int(input("u r birth year"))
# print("hii"+name+"your age is"+ str(year))

# student="praneeth"
# copy=student[:]
# print(student[:])
# print(student[0:2])
# print(student[1:-1])
# print(student[0:3])
# print("copy string is "+copy)

first="Praneeth"
last="balu"
msg= f'Hii {first} your lastname is {last}'
print(msg)

no=len(msg)
up=msg.upper()
finding=msg.find('P')
replacing=msg.replace('your','u r')
print(str(no)+" "+up)
print(str(finding))
print(replacing)
print('balu'in msg)
