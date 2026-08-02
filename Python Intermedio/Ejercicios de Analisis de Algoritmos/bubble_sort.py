# Crea un bubble_sort por tu cuenta sin revisar el código de la lección.
# Modifica el bubble_sort para que funcione de derecha a izquierda, ordenando los números menores primero (como en la imagen de abajo).

def bubble_sort_right_to_left(arr): # O(1) - getting the length of the list
    n = len(arr)
    print(f"Initial: {arr}")
    for i in range(n): #Outer loop: O(n) iterations
        for j in range(n - 1, i, -1):   # Inner loop: O(n) iterations (shrinks by 1 each pass)
            if arr[j] < arr[j - 1]: # O(1) comparison
                arr[j], arr[j - 1] = arr[j - 1], arr[j] # O(1) swap
                print(f"Pass {i + 1}, step {j}: {arr}")  # O(1) print (excluded from complexity, but technically O(n) due to string formatting of the list)
    return arr #O(1)

arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Final:   {bubble_sort_right_to_left(arr)}")