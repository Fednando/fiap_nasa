import platform
from datetime import datetime

print("Nome maquina: ................", platform.node())
print("Arquitetura: ................", platform.architecture())
print("Sistema Operacional: ................", platform.system())
print("Versão SO: ................", platform.release())
print("Processador: ................", platform.processor())
print("Versão do Python: ................", platform.python_version())

print(datetime.now().month)