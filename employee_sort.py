employees = [
    {"name": "Carlos", 
    "email": "carlos@empresa.com",
    "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]

department_sort = {}
for i in employees:
    department_sort = {i["department"]}
print(department_sort)  