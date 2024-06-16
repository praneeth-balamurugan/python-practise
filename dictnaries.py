# customer={
#     "name":"Praneeth",
#     "age":"40",
#     "is_verfied":True
# }
# print(customer)
# print(customer["name"])
# customer["name"]="BP"
# print(customer["name"])
# print(customer)

val=input("Phone:")
digits_mapping={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
output=""
for ch in val:
    output+=digits_mapping.get(ch,"!")+" "
print(output)

