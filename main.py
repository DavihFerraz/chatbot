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

def chatbot(user_input):
    # Envia a mensagem do usuário para o modelo
    response = chat.send_message(user_input)
    return response.text

def main():
    print("Bem-vindo ao Chatbot com Respostas Contextuais! Digite 'sair' para encerrar.")
    
    while True:
        # Recebe a entrada do usuário
        user_input = input("Você: ")
        
        # Verifica se o usuário quer sair
        if user_input.lower() == "sair":
            print("Chatbot: Até logo!")
            break
        
        # Gera a resposta do chatbot
        response = chatbot(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()