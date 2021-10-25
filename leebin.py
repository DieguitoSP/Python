def main():
    pass
# Lee fichero binario

print (' Lee archivo binario ')
nombre_fihcero = 'lista.bin'
fichero =open(nombre_fihcero,'rb')
lista = list(fichero.read())
print()
print(lista)
print(' el archivo ha sido leido ')

if __name__ == "__main__":
    main()
