# CONCATENAR VARIABLES EN STRINGS (FORMAT)
print(f"The value i is {i}")

var = int(3.99)
print(var)
var1 = int(5*5)
print(var1)

total_min = 43+42+57

total_hr = total_min / 60

print(total_hr)
total_hr = 2.367

print(total_hr)
x = 4
x = x/2
print(x)

name = "Michael Jackson"
name
print(name[0:4])

a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)


e = 'clocrkr1e1c1t'
print(e[::2])

g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, \
Everywhere that Mary went The lamb was sure to go "

nb = g.split()

print(g)
print(nb)

print("AB\nC\nDE")
"holaMike".find("Mike")

 
length = len(g)
print(length)


# TUPLAS Y LISTAS

tuple1 = ("disco", 10, 1.2)
print(tuple1[2])


a_list = [1, "hello", [1, 2, 3], True]
print(a_list[1:4])


A = [1, 'a']
B = [2, 1, 'd']

print(A + B)

Shopping_List = ["Watch", "Laptop", "Shoes", "Notebook", "Clothes", "Football"]
Shopping_List.remove("Clothes")
print(Shopping_List)



say_what = ('say', 'what', 'you', 'will')
print(say_what[-1])

A = (1, 2, 3, 4, 5)
print(A[1:4])

###
B = [1, 2, [3, 'a'], [4, 'b']]
print(B[3][1])


x = [1, 2, 3] + [1, 1, 1]
print(x)

A = [1]
A.append([2, 3, 4, 5])
print(A.count)

cantidad = len(A)
print(cantidad)




mi_set = set(list)
print(mi_set)

A = [1, 2, 2, 1]
B = {1, 2, 2, 1}
igual = set(A) == B
print(igual)

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])

album_set3 = album_set1 | album_set2


print(album_set1.issubset(album_set3))

# CICLOS / BUCLES

Bib = 7
if (Bib > 8):
    print("This album is Amazing!")
else:
    print("this album is ok")





if ("a" == "A"):
    print("x")
else:
    print("xxx")


for i in [1, 2, 3]:
    print(i)

for i in range(-5, 6):  # Empieza en 1 y termina en 5
    print(i)


Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for i in Genres: 
    print(i)

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 6, 10]
i = 0

while i < len(PlayListRatings):
    if PlayListRatings[i] < 6:
        break
    else: 
        print(PlayListRatings[i])
        i += 1


M_table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(M_table):
    value = M_table[i] * 7
    print(value)
    i += 1


M6_table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for value in range(1, 11):
    print("6 *", value, "=", value*6)

for i, x in enumerate(['A', 'B', 'C']):
    print(i, x)

def div(a, b):
    return(a/b)

try:
    # Código que puede causar un error
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)

except ValueError:
    # Captura el error cuando la conversión de texto a número falla
    print("Error: Debes ingresar un número válido.")

except ZeroDivisionError:
    # Captura el error cuando intentas dividir entre cero
    print("Error: No se puede dividir entre cero.")

except Exception as e:
    # Captura cualquier otro error no especificado
    print("Ocurrió un error inesperado:", e)