## JOGO DA FORCA
 
palavra = "python"
chances = 5
letras_usuario = []
ganhou = False
 
while True:
    ganhou = True
    for letra in palavra:
 
        if letra.lower() in letras_usuario:
            print(letra, end="")
        else:
            print("_", end="")
            ganhou = False
    print("")
 
    if ganhou:
        print("Parabéns! Você acertou a palavra!")
        break
 
    tentativa = input("Escolha uma letra para adivinhar: ").lower()
 
    if tentativa in letras_usuario:
        print("Você já tentou essa letra!")
        continue
 
    letras_usuario.append(tentativa)
 
    if tentativa not in palavra.lower():
        chances -= 1
        print("Letra incorreta! Você ainda tem {} chances!!".format(chances))
 
    if chances == 0:
        print("Você perdeu! A palavra era: {}".format(palavra))
        break
