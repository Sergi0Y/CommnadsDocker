# IMPORT PANDAS
import pandas as pd

# CREACIÓN DE DICCIONARIO
x = {'ID': [1, 2, 3, 4], 'Name': ['Rose', 'John', 'Jane', 'Mary'], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 'Salary': [1, 2, 3, 4]}

# CREACIÓN DE TABLA
df = pd.DataFrame(x)

# MOSTRAR TABLA
print(x)

# MOSTRAR COLUMNAS SELECCIONADAS
z = df[['Department', 'Salary', 'ID']]

print(z)

# MOSTRAR COLUMNAS COMO SERIES
b = df['Marks']

# ILOC / LOC 

# MÉTODO 'ILOC' PARA BUSCAR VALORES POR COORDENADAS
i = df.iloc[2, 2]

# SIRVE PARA BUSCAR UN RANGO DE POSICIÓN DE DATOS
i2 = df.iloc[0:2, 0:3]

# TAMBIÉN SE PUEDE BUSCAR POR NÚMERO Y VALOR DE LA FILA O COLUMNA 'LOC'
e = df.loc[1, 'Artist']

