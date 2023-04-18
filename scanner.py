import socket # Librería puerto

host = input("Introduce la IP a escanear: ")
ports = input("Introduce los puertos a escanear (separados con coma): ")

# Esto va a separar los puertos que hemos leído por consola
ports = ports.split(",")

# Nos dice la cantidad de puertos guardados en la array ports
print(len(ports))

