# Dada n cantidad de notas de un estudiante, calcular:
# Cuantas notas tiene aprobadas (mayor a 70).
# Cuantas notas tiene desaprobadas (menor a 70).
# El promedio de todas.
# El promedio de las aprobadas.
# El promedio de las desaprobadas.

counter = 1
approved_subjects = 0
approved_average = 0
failed_subjects = 0 
failed_average = 0
total_average = 0
total_subjects = int(input("enter your subjects: "))

while (counter <= total_subjects):
    current_subject = int(input (f"Enter subject number {counter} score: "))
    if (current_subject >= 70 ):
        approved_subjects = approved_subjects + 1
        approved_average = approved_average + current_subject
    else:
        failed_subjects = failed_subjects + 1
        failed_average = failed_average + current_subject
    total_average = total_average + (current_subject/total_subjects)
    counter = counter + 1
    
# me gustaria saber si hay una manera de manejar estos promedios sin usar if else
approved_average = approved_average / approved_subjects if approved_subjects > 0 else 0
failed_average = failed_average / failed_subjects if failed_subjects > 0 else 0

print(f"your total approved subjects is {approved_subjects} with an average of {approved_average}.")
print(f"your total failed subjects is {failed_subjects} with an average of {failed_average}.")
print(f"your total average is {total_average}")