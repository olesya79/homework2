from csv import writer

file = open('Books.csv', 'w')

line = "To Kill a Mockingbird, Harper Lee, 1960\n"
file.write(str(line))
line = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(line))
line = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(str(line))
line = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(str(line))
line = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(line))
line_new = str(input('Введите новую запись: '))
with open('Books.csv', 'a', newline='\n') as object_csv:
    writer_object = writer(object_csv)

    writer_object.writerow(line_new)
file.write(str(line_new))
file.close()
