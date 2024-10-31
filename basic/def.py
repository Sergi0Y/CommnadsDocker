from random import randint as rnd

memReg = 'test/members.txt'
exReg = 'test/inactive.txt'
fee = ('yes', 'no')

def genFiles(current, old):
    with open(current, 'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015, 2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999),date,fee[rnd(0, 1)]))


    with open(old, 'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015, 2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1, 25)) 
            writefile.write(data.format(rnd(10000, 99999),date, fee[1]))


genFiles(memReg, exReg)

def cleanFiles(currentMem, exMem):
    # Abre los archivos en los modos adecuados
    with open(currentMem, 'r+') as currFile, open(exMem, 'a+') as exFile:
        # Lee todas las líneas de currentMem
        members = currFile.readlines()
        
        # Separar el encabezado y miembros activos/inactivos
        header = members[0]
        active_members = [header]
        inactive_members = [header]
        
        for member in members[1:]:
            if 'no' in member.split()[-1]:  # Si el estado es 'no'
                inactive_members.append(member)
            else:
                active_members.append(member)
        
        # Volver al inicio de currentMem y sobrescribir solo con miembros activos
        currFile.seek(0)
        currFile.writelines(active_members)
        currFile.truncate()  # Eliminar cualquier línea extra

        # Agregar los miembros inactivos a exMem
        exFile.writelines(inactive_members)


memReg = 'test/members.txt'
exReg = 'test/inactive.txt'
cleanFiles(memReg,exReg)

# code to help you see the files

headers = "Membership No  Date Joined  Active  \n"

with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())