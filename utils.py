import os
import platform

def clear_screen():
    system_name = platform.system()
    if system_name == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def pause():
    input("\nPressione Enter para continuar...")

def get_int_input(prompt: str) -> int:
    while True:
        try:
            value = input(prompt)
            return int(value)
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")

def get_str_input(prompt: str) -> str:
    return input(prompt).strip()