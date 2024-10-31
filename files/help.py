file = open("index.txt", "r")
print(file.name) # index.txt
print(file.mode)   # r
FileContent = file.read()
print(FileContent)
print(type(FileContent))
file.close()
print(file.closed)
###
with open("/text/index.txt", "r") as file1:
    file_stuff = file1.readline()   # Almacena cada línea del archivo
    # file_stuff = file1.readline(5) Imprime 5 caracteres del texto
    print(file_stuff)   # imprime cada línea del archivo
#
    for line in file1:  # recorre imprimiendo todas las líneas del archivo
        print(line)
    """ file_stuff = file1.read()
    print(file_stuff) # Imprime el archivo completo
print(file1.closed)
 """


# Write

with open("text/css.txt", "w") as file2:
    file2.write("this is line A\n")    
    file2.write("this is line B\n")   
    file2.write("this is line C\n")   

with open("text/css.txt", "r") as file2:
    file2r = file2.read()
    print(file2r)
# For
Lines = ["this is line A\n", "this is line B\n", "this is line C\n"]
with open("text/css.txt", "w") as file2:
    for line in Lines:
        file2.write(line)
# AGREGAR ALGO SIN BORRAR
with open("text/css.txt", "a") as file2:
    file2.write("this is line D\n")

#copy file

with open('text/index.txt', 'r') as readfile:
    with open('text/css.txt', 'w') as writefile:
        for line in readfile:
            writefile.write(line)

# ADDITIONAL MODES
# r+ : Reading and writing. Cannot truncate the file.
# w+ : Writing and reading. Truncates the file.
# a+ : Appending and Reading. Creates a new file, if none exists.
# You dont have to dwell on the specifics of each mode for this lab.



# A+
# Read and append
with open('text/css.txt', 'a+') as testwritefile:
    # Escribir contenido nuevo
    testwritefile.write("Nuevo texto aquí\n")
    
    # Mostrar la posición inicial del puntero
    print("Initial Location: {}".format(testwritefile.tell()))

    # Leer el contenido del archivo
    data = testwritefile.read()
    if not data:
        print('Read nothing') 
    else: 
        print(data)
        
    # Mover el puntero al inicio y volver a leer el contenido
    testwritefile.seek(0, 0) 
    print("\nNew Location : {}".format(testwritefile.tell()))

    data = testwritefile.read()
    if not data:
        print('Read nothing') 
    else: 
        print(data)
    
    print("Location after read: {}".format(testwritefile.tell()))


# R+
with open('text/css.txt', 'r+') as testwritefile:
    testwritefile.seek(0, 2) #write at bottom of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    testwritefile.seek(0, 0)
    print(testwritefile.read())

# R+ TRUNCATE
with open('/Example2.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())