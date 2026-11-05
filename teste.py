import random
import time

def gerar_codiname():
    # Listas de elementos para o codinome
    adjetivos = ["Fantasma", "Sombrio", "Gélido", "Implacável", "Silencioso", "Cibernético", "Oculto", "Veloz"]
    substantivos = ["Fênix", "Lobo", "Falcão", "Víbora", "Sombra", "Trovão", "Neon", "Águia", "Titânio"]
    
    # Sorteia um elemento de cada lista
    adj = random.choice(adjetivos)
    sub = random.choice(substantivos)
    numero = random.randint(10, 99) # Número operacional de dois dígitos
    
    return f"Agente {sub} {adj} (ID: 0{numero})"

# Execução do programa
print("🕵️‍♂️ ACESSANDO BANCO DE DADOS DA AGÊNCIA...")
time.sleep(1) # Cria um efeito de carregamento

print("\n🤖 GERANDO NOVA IDENTIDADE SECRETA...")
time.sleep(1.5)

novo_nome = gerar_codiname()
