import os

cwd = os.getcwd()  # Obtiene el directorio de trabajo actual (cwd)
files = os.listdir(cwd)  # Obtiene todos los archivos del directorio
print("Files in %r: %s" % (cwd, files))

# Si muestra un error de que no encuentra el fichero y este existe, puede ser
# porque estamos trabajando en un directorio distinto, para cambiar de directorio
# usamos la funcion os.chdir(), poniendo r'' para que la cadena que pongamos sea
# interpretada literalmente
os.chdir(r'D:\Documentos D\Programación\Github\Python3\python\04.File_Handling')

# Por defecto la flag es la r de lectura si no ponemos nada
# Si el fichero no existe da un error
# f = open("test.txt", "r")
f = open("test.txt")

print(f.read()) # Imprime todas las lineas del fichero

f.close()

# Create mode, si existe da un error
f = open("test2.txt", "x")

f.close()