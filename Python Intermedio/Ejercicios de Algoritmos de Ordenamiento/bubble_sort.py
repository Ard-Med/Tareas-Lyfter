# Crea un bubble_sort por tu cuenta sin revisar el código de la lección.
# Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).

def bubble_sort_right_to_left(arr):
    n = len(arr)
    print(f"Initial: {arr}")
    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                print(f"Pass {i + 1}, step {j}: {arr}")
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Final:   {bubble_sort_right_to_left(arr)}")