import numpy as np
import colorama
from colorama import *
from colorama import Fore, Back, Style

colorama.init()

print(Fore.CYAN + "On a pour equation : axÂ²+bx+c = 0")
print("----------------------------------")
A = float(input("Entrer la valeur de a: "))
B = float(input("Entrer la valeur de b: "))
C = float(input("Entrer la valeur de c: "))
print("----------------------------------")
delta = (B**2-4*A*C)
print(Fore.WHITE + f"Le discriminant delta est donc : bÂ²-4ac")
print(f"D'ou delta = {B}Â² - 4*{A}*{C}")
print(f"Alors delta = {B**2} - {4*A*C}")
print(f"On a alors delta = {B**2-4*A*C}")

if B**2-4*A*C > 0:
    print("Donc l'equation admet 2 solutions")
    print(f"x1 = (-b-(racine de delta)/2a = {-B}-{np.sqrt(delta)}/{2*A} = {(-B-np.sqrt(delta))/(2*A)}")
    print(f"x2 = (-b+(racine de delta)/2a = {-B}+{np.sqrt(delta)}/{2*A} = {(-B+np.sqrt(delta))/(2*A)}")
    print("--------------------------------------------------------------")
    print(Fore.GREEN + f"Donc l'ensemble des solutions est: x1={(-B-np.sqrt(delta))/(2*A)} et x2={(-B+np.sqrt(delta))/(2*A)}")
    print("-" * 50)
    print(f"La forme canonique de l'equation est : {A}((x + {B/(2*A)})Â² - {(B**2-4*A*C)/(4*(A**2))})")
    print(" ")
    input(Back.RED + "Press Enter to exit")
elif B**2-4*A*C == 0:
    print("Donc l'equation admet une seul solutions")
    print(f"x = -b/2a = {-B}/{2*A} = {-B/2*A}")
    print("--------------------------------------------------------------")
    print(Fore.GREEN + f"Donc la solution est x ={-B}/{2*A}")
    print("-" * 50)
    print(f"La forme canonique de l'equation est : {A}((x + {B/(2*A)})Â² - {(B**2-4*A*C)/(4*(A**2))})")
    print(" ")
    input(Back.RED + "Press Enter to exit")
else:
    print(Fore.RED + "La solution n'admet aucune solution car delta est negative")
    print(" ")
    input(Back.RED + "Press Enter to exit")
