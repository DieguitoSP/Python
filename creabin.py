def main():
    pass
# Crear fichero binario
print(' Crea un fichero binario ')

nombre_fichero = 'lista.bin'
fichero=open(nombre_fichero, 'wb')
lista=[19, 82, 92, 22 ]
fichero.write(bytearray(lista))
fichero.close()

print(' yupi!! el fichero se ha creado :) ')

if __name__ ==  "__main__":
    main()
