import google.generativeai as genai

# Defina sua chave da API
genai.configure(api_key="AIzaSyD_TgVBvX5B9REpxNx7IUlf1mpLtH_1MF4")

# Criar o chatbot
model = genai.GenerativeModel("gemini-pro")  # Usa o modelo Gemini

def chatbot(prompt):
    response = model.generate_content(prompt)
    return response.text

# Loop para interação
print("Bem-vindo ao chatbot! Digite 'sair' para encerrar.")
while True:
    user_input = input("Você: ")
    if user_input.lower() == "sair":
        print("Chatbot encerrado!")
        break
    resposta = chatbot(user_input)
    print("Bot:", resposta)
