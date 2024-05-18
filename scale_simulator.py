import serial
import time
import tkinter as tk
from tkinter import scrolledtext
from serial.tools import list_ports
import threading

# Criação da instância serial.Serial
serial_port = None

# Variável de controle para verificar se o thread está em execução
execution_thread = False

def send_weight():
    global serial_port
    global execution_thread

    if execution_thread:
        return

    porta = porta_var.get()
    scale_type = scale_type_var.get()

    if not serial_port or serial_port.port != porta:
        serial_port = serial.Serial(porta, 9600)
        time.sleep(2)

    execution_thread = True

    def send_loop():
        global execution_thread
        global sended_text_log

        while True:
            weight_value = float(weight_entry.get())
            if scale_type == "TruTestS2":
                stringDefaultBalanca = f"[{weight_value}](stable)"
            elif scale_type == "OutroTipoDeBalanca":
                stringDefaultBalanca = f"{weight_value} kg"
            else:
                stringDefaultBalanca = f"[{weight_value}](stable)"
            serial_port.write(stringDefaultBalanca.encode())
            sended_text_log.insert(tk.END, f"Enviado: {stringDefaultBalanca}\n")
            sended_text_log.see(tk.END) 
            print("Enviado:", stringDefaultBalanca)
            time.sleep(1)

            # Verifica se a execução deve ser interrompida
            if not execution_thread:
                break

        print("--- Execução encerrada! ---")
        sended_text_log.insert(tk.END, "--- Execução encerrada! ---\n")
        sended_text_log.see(tk.END)

    threading.Thread(target=send_loop).start()

def parar():
    global execution_thread
    execution_thread = False

def update_weight(event):
    send_weight()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Simulador de balança incremental")

weight_label = tk.Label(root, text="Valor inicial:")
weight_label.grid(row=0, column=0)

weight_entry = tk.Scale(root, from_=0, to=2000, orient="horizontal", command=update_weight)
weight_entry.grid(row=0, column=1)

porta_label = tk.Label(root, text="Porta Serial:")
porta_label.grid(row=1, column=0)

portas_disponiveis = [porta.device for porta in list_ports.comports()]
porta_var = tk.StringVar(root)
porta_var.set(portas_disponiveis[0])  

porta_dropdown = tk.OptionMenu(root, porta_var, *portas_disponiveis)
porta_dropdown.grid(row=1, column=1)

scale_type_label = tk.Label(root, text="Tipo de balança")
scale_type_label.grid(row=2, column=0)


scales = ["TruTestS2", "OutroTipoDeBalanca"]


scale_type_var = tk.StringVar(root)
scale_type_var.set(scales[0])

scale_type_dropdown = tk.OptionMenu(root, scale_type_var, *scales)
scale_type_dropdown.grid(row=2, column=1)

send_button = tk.Button(root, text="Enviar", command=send_weight)
send_button.grid(row=4, columnspan=2)

stop_button = tk.Button(root, text="Parar", command=parar)
stop_button.grid(row=4, column=2)

sended_text_log = scrolledtext.ScrolledText(root, wrap=tk.WORD)
sended_text_log.grid(row=5, columnspan=3, sticky="nsew")

root.mainloop()
