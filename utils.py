import os
import platform
from datetime import datetime

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

def get_data_hora_input():
    while True:
        try:
            data_str = input("Digite a Data (DD/MM/AAAA): ").strip()
            hora_str = input("Digite o Horário (HH:MM): ").strip()
            data_completa_str = f"{data_str} {hora_str}"
            data_obj = datetime.strptime(data_completa_str, "%d/%m/%Y %H:%M")
            return data_obj.strftime("%Y-%m-%d %H:%M:%S")
            
        except ValueError:
            print("❌ Data ou hora inválidas! Tente novamente.")