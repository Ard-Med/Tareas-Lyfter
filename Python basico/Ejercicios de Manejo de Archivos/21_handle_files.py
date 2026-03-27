# Cree un programa que lea nombres de canciones de un archivo (línea por línea)
# y guarde en otro archivo los mismos nombres ordenados alfabéticamente.


def open_sending_file(sending_path):
	with open(sending_path) as file:
		return (file.readlines())


def write_songs_to_file(receiving_path, content):
    with open(receiving_path, 'w') as file:
        content.sort()
        file.write("\n".join(content))
        return (content)


def file_paths ():
    sending_file = r"C:/Users/Desktop/Lyfter/sending_file.txt"
    receiving_file = r"C:/Users/Desktop/Lyfter/receiving_file.txt"
    print(write_songs_to_file(receiving_file, open_sending_file(sending_file)))


file_paths()