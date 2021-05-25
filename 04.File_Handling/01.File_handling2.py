import os

cwd = os.getcwd()  # Obtiene el directorio de trabajo actual (cwd)

files = os.listdir(cwd)  # Obtiene todos los archivos del directorio

print("Archivos en %r: %s" % (cwd, files))

os.chdir(r'D:\Documentos D\Programación\Github\Python3\python\04.File_Handling')

# La flag w es de escritura y sobreesccribe el contenido del fichero.
f = open("write.txt","w")

f.write("Esto es una prueba de escritura en un fichero.")

f.close()

# La flag a es para añadir a un fichero, si no existe lo crea.
f = open("write.txt","a")

f.write("\nEste texto va a ser añadido")