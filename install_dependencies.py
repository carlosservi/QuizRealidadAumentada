import subprocess

# Ruta al archivo requirements.txt
requirements_file = 'requirements.txt'

# Comando para instalar los paquetes utilizando pip
command = ['pip', 'install', '-r', requirements_file]

# Ejecuta el comando
subprocess.call(command)