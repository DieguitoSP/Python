file = ("/etc/hosts")
f = open(file, 'r')
mensaje = f.read()
print (mensaje)
f.close()

