import socket # Librería puerto

def leer_archivo(filename): # No tenemos por qué definir el tipo de objeto que estamos pasando, pero es recomendable.
    # Con el archivo abierto haz lo siguiente:
    with open(filename, "r") as file: #r de read
        lineas = file.readlines()
        lineaslimpias=[]
        for linea in lineas:
            lineaslimpias.append(linea.rstrip())
        return lineaslimpias

hosts = leer_archivo('ips.txt')
print(hosts)
ports = leer_archivo('puertos_comunes.txt')

# Para cada host que hay en hosts
for host in hosts:
    # Para cada puerto que haya en puertos
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, int(port)))

        if result == 0:
            print (f"El puerto {port} está abierto en el host {host}")
        else:
            print (f"El puerto {port} está cerrado en el host {host}")
        sock.close()