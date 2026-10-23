# Jogo de adivinhação

numero_secreto = 37  # número escolhido

print("=== JOGO DE ADIVINHAÇÃO ===")
print("Tente descobrir o número secreto entre 1 e 50.")
print("Você tem 5 tentativas.\n")

for tentativa in range(1, 6):
    palpite = int(input(f"Tentativa {tentativa}: Digite seu palpite: "))

    if palpite == numero_secreto:
        print("\n🎉 Parabéns! Você acertou o número secreto!")
        break

    elif palpite > numero_secreto:
        print("📉 O número secreto é menor que o seu palpite.")

    else:
        print("📈 O número secreto é maior que o seu palpite.")

else:
    print(f"\n😢 Você perdeu! O número secreto era {numero_secreto}.")
