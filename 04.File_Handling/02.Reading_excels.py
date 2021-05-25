# pip install pandas
# pip install xlrd
# pip install openpyxl porque la version de xlrd no soporta .xlsx

import os
import pandas as pd

os.chdir(r'D:\Documentos D\Programación\Github\Python3\python\04.File_Handling')

file = pd.ExcelFile("sales.xlsx")

print(file.sheet_names) # Imprime los nombres de las hojas que haya

sheet = file.parse('sales') # Coge todos los datos de un hoja y los formatea como una pandas.core.frane.Dataframe

print(sheet)

print(sheet.Date) # Para imprimir solo una de las columnas de la hoja

print(sheet.Amount.sum()) # Realiza un sumatorio sobre una columna

print(sheet.loc[0]) # Imprime una linea en concreto

print(sheet.loc[0, "Amount"]) # Imprimir un valor en concreto de un linea en concreto

# Para buscar por un parametro en concreto primero seteamos el indice y luego usamos la funcion loc[] con el valor a buscar.
sheet.set_index("Customer", inplace=True)

print(sheet.loc["MMC Inc."])


sheet = sheet.reset_index()

# Esto también se puede hacer de la siguiente forma:
print(sheet.loc[ sheet["Customer"] == "MMC Inc."])

# Imprime las ventas que se hayan hecho con una cantidad mayor a 2000
print(sheet.loc[ sheet["Amount"] > 2000])

# Imprime la venta cuya cantidad es la mayor
print(sheet.loc[ sheet["Amount"].idxmax() ])

# Imprime el cliente que tiene la mayor cantidad
print(sheet.loc[ sheet["Amount"].idxmax() ]["Customer"])

# Imprime los clientes que tiene una cantidad mayor a 1800
print(sheet.loc[ sheet["Amount"] > 1800] ["Customer"])

# Si el cliente se repite solo lo imprime una vez usando una lista
print(sheet.loc[ sheet["Amount"] > 1800 ] ["Customer"].unique())

# Para imprimir un cliente en concreto
print(sheet.loc[ sheet["Amount"] > 1800 ] ["Customer"].unique()[0])
print(sheet.loc[ sheet["Amount"] > 1800 ] ["Customer"].unique()[1])

# Para imprimirlos todos
for customer in sheet.loc[ sheet["Amount"] > 1800 ] ["Customer"].unique():
    print(customer)