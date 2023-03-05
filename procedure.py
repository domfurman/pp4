def add_text(filename, text):
    try:
        with open(filename, 'a') as file:
            file.write(text + "\n")
        print("Line added")
    except IOError:
        print("Something went wrong")

add_text('file.txt', "Lorem")
add_text('file.txt', "Ipsum")
add_text('file.txt', "Dolores")
