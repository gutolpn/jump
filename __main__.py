'''
 Programa de exemplo de aula
 Data: 24-10-2023

 @author: eu
'''
#Comentário do Pitty
import os
import WConio2 as WConio2
import cursor

cursor.hide()
os.system('cls')

#herói do jogo
heroi = '&'
heroiX = 20
heroiY = 4

#bicho do mal
bicho = '@'
bichoX = 10
bichoY = 7

#contador de frames
cont=0

#logica geral
while True:
    WConio2.gotoxy(0,0)   
    
    #desenhando a tela
    print('*'*42)
    for j in range(15):
        print('*', end='')
        for k in range(40):
            char = ' '
            
            if j==bichoY and k==bichoX:
                char=bicho
            
            if j==heroiY and k==heroiX:
                char=heroi

            print(char, end='')

        print('*')
    print('*'*42)

    #controlando    
    if cont%80 == 0:
        bichoX+=1
    if bichoX > 40:
        bichoX=0

    #pegando comandos do teclado
    if WConio2.kbhit():
        (key, symbol) = WConio2.getch()

        if symbol=='a':
            heroiX-=1
        elif symbol=='d':
            heroiX+=1

    cont+=1


