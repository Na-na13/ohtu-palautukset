# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma") # muutos mainissa

x = int(input("luku 1: "))
y = int(input("luku 2: "))
<<<<<<< HEAD
print(f"{summa(x, y)}") # muutos
print(f"{erotus(x, y)}") # muutos
=======
print(f"{summa(x, y)}") # muutos
print(f"{erotus(x, y)}") # muutos
>>>>>>> main

logger("lopetetaan")
print("goodbye") # lisäys bugikorjaus-branchissa
