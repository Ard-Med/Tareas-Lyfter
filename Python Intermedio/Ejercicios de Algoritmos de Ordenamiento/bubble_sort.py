# Crea un bubble_sort por tu cuenta sin revisar el código de la lección.
# Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).

def bubble_sort_right_to_left(list):
    n = len(list)
    print(f"Initial: {list}")
    for i in range(n):
        for j in range(n - 1, i, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
                print(f"Pass {i + 1}, step {j}: {list}")
    return list

list = [64, 34, 25, 12, 22, 11, 90]
print(f"Final:   {bubble_sort_right_to_left(list)}")