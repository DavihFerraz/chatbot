import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext

# Configure a API Key
API_KEY = "AIzaSyD_TgVBvX5B9REpxNx7IUlf1mpLtH_1MF4"  # Substitua pela sua chave de API
genai.configure(api_key=API_KEY)

# Escolha o modelo
model = genai.GenerativeModel('gemini-pro')

# Inicia uma conversa com contexto
chat = model.start_chat(history=[])

# Função para enviar mensagem e obter resposta

def enviar_mensagem():
    user_input = entrada.get() #Pega a mensagem do campo de entrada
    if user_input.lower() == 'sair':
        chat_area.insert(tk.END, "Você: " + user_input + "\n") 
        chat_area.insert(tk.END, "Chatbot: Até logo! \n")
        janela.quit() #Fecha a aplicação
    else:
        chat_area.insert(tk.END, "Você: " + user_input  + "\n")
        resposta = chat.send_message(user_input).text
        chat_area.insert(tk.END, "Chatbot: " + resposta + "\n")
        entrada.delete(0, tk.END) #Limpa o campo de entrada




#Configuração da janela principal
janela = tk.Tk()
janela.title("Chatbot com Respostas Contextuais")

#Área de texto para exibir a conversa
chat_area = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=50, height=20)
chat_area.pack(padx=10, pady=10)
chat_area.config(font=("Arial", 12), bg="#f0f0f0", fg="#333")


#Campo de entrada para o usuário digitar
entrada = tk.Entry(janela, width=40)
entrada.pack(padx=10, pady=10)
entrada.config(font=("Arial", 12))


#Botão para enviar mensagem
botao_enviar = tk.Button(janela, text='Enviar', command=enviar_mensagem)
botao_enviar.pack(padx=10, pady=10)

#Inicia o loop da interface grafica
janela.mainloop()