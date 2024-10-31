""" print(pd.__version__)

data = {'Nombre': ['Ana', 'Luis', 'María'], 'Edad': [23, 45, 31]}
df = pd.DataFrame(data)

print(df.head())
# Calcular la media de la columna "Edad"
print(df['Edad'].mean())

df = pd.read_csv('pandas/file1.csv')
print(df) """

""" 
import pandas as pd
x = {'ID': [1, 2, 3, 4], 'Name': ['Rose', 'John', 'Jane', 'Mary'], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 'Salary': [1, 2, 3, 4]}

df = pd.DataFrame(x)
# print(df)


z = df[['Department', 'Salary', 'ID']]
print(z) 
"""
import pandas as pd

students = {'Student':['David', 'Samuel', 'Terry', 'Evan'], 'Age':[27, 24, 22, 32], 'Country':['UK', 'Canada', 'China', 'USA'], 'Course':['Python', 'Data', 'Machine', 'Web'], 'Marks':[85, 72, 89, 76]}

df = pd.DataFrame(students)

# z = df[['Department', 'Salary', 'ID']]

b = df['Marks']
# print(b)

i = df.iloc[2, 2]
# print(f"The value i is {i}")

new_index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

df2 = pd.DataFrame(new_index, columns=['Artist'])
print(df2)Muchas