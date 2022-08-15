import random
print ("*******************************")
print ("Seja bem vindo ao jogo da forca")
print ("*******************************")

arquivo = open("palavras.txt", "r")
palavras = []

for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

arquivo.close ()

numero = random.randrange(0,len(palavras))
PalavraSecreta = palavras[numero].upper()
LetrasAcertadas = []

for letra in PalavraSecreta:
    LetrasAcertadas.append("_")

enforcou = False
acertou = False
erros = 0

print (LetrasAcertadas)

while (not enforcou and not acertou):

    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
   
    if (chute in PalavraSecreta):
        Posicao = 0
        for letra in PalavraSecreta:
            if (chute == letra):
                    LetrasAcertadas [Posicao] = letra
            Posicao += 1
    else:
        erros += 1
    enforcou = erros == 6
    acertou = "_" not in LetrasAcertadas
    print (LetrasAcertadas) 

if (acertou):
        print ("Você ganhou!")
else:
        print ("Você perdeu")

print ("Fim do jogo")