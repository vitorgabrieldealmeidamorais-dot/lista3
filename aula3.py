#6. Mensagem de Boas-Vindas:  Escreva um código que  utilize o  print()  para exibir a frase:  "--- BEM-VINDO AO MUNDO DE PYTHON ---"-----------------------------------------------------------

print("----Bem Vindo ao Mundo de Python---")

#7. Captura de Nome:  Escreva um script que pergunte  ao usuário:  "Qual o nome do seu herói?"  e armazene a resposta em uma variável---------------------------------------------------

define = input("Qual o nome do seu herói?")

#8. Exibição Variável:  Com base no exercício anterior,  faça o programa exibir:  "O herói [nome] acaba de entrar na guilda!-------------------------------------------------------

print(f"O Heroi {define} Acaba de Entra na Guilda!")

#9. Diálogo de NPC:  Crie um pequeno diálogo. O programa  deve perguntar o nome de uma cidade e depois imprimir:  "Viajante, você está  a caminho de [Nome da Cidade], tome cuidado!----------------------------------------
print("Aldeão: Ola viajante")
print("Aldeão: Voce parece perdido")
print("Aldeão: Procura-se por algum Lugar?")
print("Heroi: A Sim estou procurando por uma cidade")
cidade = input("Qual Cidade Procura?")
print(f"Aldeão: A sim viajante, você está  a caminho de {cidade} tome Cuidado!! ")

#10. Impressão Múltipla:  Use um único comando  print()  para exibir três itens de um inventário (ex: Espada, Escudo, Poção) em linhas diferentes ou separados por vírgulas-------------------------------------------

print("Tijolo,Tabuas,Pregos")

#11. Visual de Interface:  Use o  print()  para desenhar  uma pequena moldura de menu no console, como esta:----------------------------------------------------------------------------------------

print("-----------------------------------------------")
print("                 Como Esta                     ")
print("-----------------------------------------------")

#12. Confirmação de Ação:  Crie um código que pergunte:  "Deseja salvar o progresso? (S/N)"  e apenas exiba no console a resposta  digitada-----------------------------------------------------
print("-----------------------------------------------")
print("                 Menu de Selve                 ")
print("-----------------------------------------------")
valor = float(input("Deseja Salvar?                          "))
print("1--Para Salvar                                 ")
print("2--Para Não Salvar                             ")
print("-----------------------------------------------")

if valor == 1:
    print("Salvando o Sistema")
    
elif valor == 2:
    print("Cancelado o Salvamento do Sistema")
    
else:
    print("Fechando o Sistema")
    