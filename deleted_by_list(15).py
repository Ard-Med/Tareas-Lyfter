# Cree un programa que use una lista para eliminar keys de un diccionario.

employee = {
    "name" : "Ard",
    "email" : "ard@work.com",
    "access_level" : 13,
    "age" : 33,
}

deleted_items = ["access_level", "age"]

for key in deleted_items:
    employee.pop(key)

print(employee)
print(deleted_items)