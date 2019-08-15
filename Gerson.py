from time import sleep 

prato1 = str('Prato 1: Arroz com Bife  R$:17,00')
prato2 = str('Prato 2: Macarrão bolonhesa  R$:12,00')
prato3 = str('Prato 3: Nhoque bolonhesa  R$:13,00')
prato4 = str('Prato 4: Strogonoff  R$:15,00')
prato5 = str('Prato 5: Escondidinho de Carne  R$:11,00')
prato6 = str('Prato 6: Escondidinho de Frango  R$:10,00')
prato7 = str('Prato 7: Sopa de Ervilha  R$:8,00')
prato8 = str('Prato 8: Salada do Chefe  R$:5,00')

bebida1 = str('Bebida 1: Água sem gás  R$:4,00')
bebida2 = str('Bebida 2: Água com gás  R$:5,00')
bebida3 = str('Bebida 3: Refrigerante de Lata  R$:6,00')
bebida4 = str('Bebida 4: Suco Natural  R$:10,00')
bebida5 = str('Bebida 5: Cerveja de Lata  R$:7,00')
bebida6 = str('Bebida 6: Vinho  R$:12,00')
bebida7 = str('Bebida 7: Saquê  R$:20,00')
bebida8 = str('Bebida 8: Energético  R$:7,99')

print('\nOlá, bem vindo ao nosso restaurante. Eu me chamo Gerson')

from time import sleep 
for contagem in range(0,1):
    sleep(1)
    nmcliente = str(input('\nComo o(a) senhor(a) se chama? '))

print('\nSeja muito bem vindo', nmcliente,)

pergunta1 = str(input('\nJá conhece a nossa casa? '))

if pergunta1.upper() == 'NÃO':
    cardapio = str(input('\nGostaria então de ver nosso cardapio? '))
    if cardapio.upper() == 'SIM':
        print('\nAqui está nosso cardapio')
        print('\nPratos:')
        print('\n',prato1, '\n',prato2, '\n',prato3, '\n',prato4,
         '\n',prato5, '\n',prato6, '\n',prato7, '\n',prato8)
        print('\nBebidas:')
        print('\n',bebida1, '\n',bebida2, '\n',bebida3, '\n',bebida4,
         '\n',bebida5, '\n',bebida6, '\n',bebida7, '\n',bebida8,)
    
    pergunta2 = str(input('\nJá se decidiu? '))
    if pergunta2.upper() == 'SIM':
        anotarpedi = str(input('\nPoderia anotar seu pedido? '))
        if anotarpedi.upper() == 'SIM':
            pedido2 = str(input('\n'))
            if pedido2.upper() == 'VOU QUERER O PRATO 1':
                print('\nTudo bem, seu pedido já está sendo preparado!')
            elif pedido2.upper() == 'VOU QUERER O PRATO 2':
                print('\nOK, irei preparar esse!')
            elif pedido2.upper() == 'VOU QUERER O PRATO 3':
                print('\nCerto, vou prepara-lo imediadamente!')
            elif pedido2.upper() == 'VOU QUERER O PRATO 4':
                print('\nAmante de Strogoff né? Vou mandar preparar!')
            elif pedido2.upper() == 'VOU QUERER O PRATO 5':
                print('\nPerfeito, já está fazendo!')
            elif pedido2.upper() == 'VOU QUERER O PRATO 6':
                print('\nOtima escolha!')
            elif pedido2.upper() == 'VOU QUERER O PRATO 7':
                print('\nUma sopa saindo!')
            elif pedido2.upper() == 'VOU QUERER O PRATO 8':
                print('\nOk, a iguaria do Chefe então!')
            
            pedirbebida = str(input('\nAceita uma bebida? '))
            if pedirbebida.upper() == 'SIM':
                print('\nQual seria?')
                resulbebida = str(input(''))
                if resulbebida.upper() == 'VOU QUERER A BEBIDA 1':
                    print('Boa escolha, uma opção sempre saudavel!')
                elif resulbebida.upper() == 'VOU QUERER A BEBIDA 2':
                    print('Um gás saudavel, tudo bem')
                elif resulbebida.upper() == 'VOU QUERER A BEBIDA 3':
                    print('Um refrigerante, tudo bem')
                elif resulbebida.upper() == 'VOU QUERER A BEBIDA 4':
                    print('Suco natural é sempre bom mesmo!')
                elif resulbebida.upper() == 'VOU QUERER A BEBIDA 5':
                    print('Uma cervejinha gelada saindo!')
                elif resulbebida.upper() == 'VOU QUERER A BEBIDA 6':
                    print('Um vinho pra aquecer a noite')
                elif resulbebida.upper() == 'VOU QUERER A BEBIDA 7':
                    print('Animar a noite!')
                elif resulbebida.upper() == 'VOU QUERER A BEBIDA 8':
                    print('Otimo pra ter uma noite agitada!')
            elif pedirbebida.upper() == 'NÃO':
                print('\nTudo bem, vou mandar fazer seu pedido')
            

            
    elif pergunta2.upper() == 'NÃO':
        print('\nOk, assim que se decidir pode me chamar!')
        pedido6 = str(input('\n'))
        if pedido6.upper() == 'PODE ANOTAR MEU PEDIDO?':
            print('\nPosso sim, qual seria?')

            pedido7 = str(input('\n'))
            if pedido7.upper() == 'VOU QUERER O PRATO 1':
                print('\nTudo bem, seu pedido já está sendo preparado!')
            elif pedido7.upper() == 'VOU QUERER O PRATO 2':
                print('\nOK, irei preparar esse!')
            elif pedido7.upper() == 'VOU QUERER O PRATO 3':
                print('\nCerto, vou prepara-lo imediadamente!')
            elif pedido7.upper() == 'VOU QUERER O PRATO 4':
                print('\nAmante de Strogoff né? Vou mandar preparar!')
            elif pedido7.upper() == 'VOU QUERER O PRATO 5':
                print('\nPerfeito, já está fazendo!')
            elif pedido7.upper() == 'VOU QUERER O PRATO 6':
                print('\nOtima escolha!')
            elif pedido7.upper() == 'VOU QUERER O PRATO 7':
                print('\nUma sopa saindo!')
            elif pedido7.upper() == 'VOU QUERER O PRATO 8':
                print('\nOk, a iguaria do Chefe então!')

            pedirbebida1 = str(input('\nAceita uma bebida? '))
            if pedirbebida1.upper() == 'SIM':
                print('\nQual seria?')
                resulbebida1 = str(input('\n'))
                if resulbebida1.upper() == 'VOU QUERER A BEBIDA 1':
                    print('\nBoa escolha, uma opção sempre saudavel!')
                elif resulbebida1.upper() == 'VOU QUERER A BEBIDA 2':
                    print('\nUm gás saudavel, tudo bem')
                elif resulbebida1.upper() == 'VOU QUERER A BEBIDA 3':
                    print('\nUm refrigerante, tudo bem')
                elif resulbebida1.upper() == 'VOU QUERER A BEBIDA 4':
                    print('\nSuco natural é sempre bom mesmo!')
                elif resulbebida1.upper() == 'VOU QUERER A BEBIDA 5':
                    print('\nUma cervejinha gelada saindo!')
                elif resulbebida1.upper() == 'VOU QUERER A BEBIDA 6':
                    print('\nUm vinho pra aquecer a noite')
                elif resulbebida1.upper() == 'VOU QUERER A BEBIDA 7':
                    print('\nAnimar a noite!')
                elif resulbebida1.upper() == 'VOU QUERER A BEBIDA 8':
                    print('\nOtimo pra ter uma noite agitada!')
            elif pedirbebida1.upper() == 'NÃO':
                print('\nTudo bem, vou mandar fazer seu pedido')

        

elif pergunta1.upper() == 'SIM':
    pedido1 = str(input('\nPosso anotar seu pedido? '))
    if pedido1.upper() == 'SIM':
        pedido3 = str(input('\n'))
        if pedido3.upper() == 'VOU QUERER O PRATO 1':
            print('\nTudo bem, seu pedido já está sendo preparado!')
        elif pedido3.upper() == 'VOU QUERER O PRATO 2':
            print('\nOK, irei preparar esse!')
        elif pedido3.upper() == 'VOU QUERER O PRATO 3':
            print('\nCerto, vou prepara-lo imediadamente!')
        elif pedido3.upper() == 'VOU QUERER O PRATO 4':
            print('\nAmante de Strogoff né? Vou mandar preparar!')
        elif pedido3.upper() == 'VOU QUERER O PRATO 5':
            print('\nPerfeito, já está fazendo!')
        elif pedido3.upper() == 'VOU QUERER O PRATO 6':
            print('\nOtima escolha!')
        elif pedido3.upper() == 'VOU QUERER O PRATO 7':
            print('\nUma sopa saindo!')
        elif pedido3.upper() == 'VOU QUERER O PRATO 8':
            print('\nOk, a iguaria do Chefe então!')
        pedirbebida2 = str(input('\nAceita uma bebida? '))
        if pedirbebida2.upper() == 'SIM':
            print('\nQual seria?')
            resulbebida2 = str(input('\n'))
            if resulbebida2.upper() == 'VOU QUERER A BEBIDA 1':
                print('\nBoa escolha, uma opção sempre saudavel!')
            elif resulbebida2.upper() == 'VOU QUERER A BEBIDA 2':
                print('\nUm gás saudavel, tudo bem')
            elif resulbebida2.upper() == 'VOU QUERER A BEBIDA 3':
                print('\nUm refrigerante, tudo bem')
            elif resulbebida2.upper() == 'VOU QUERER A BEBIDA 4':
                print('\nSuco natural é sempre bom mesmo!')
            elif resulbebida2.upper() == 'VOU QUERER A BEBIDA 5':
                print('\nUma cervejinha gelada saindo!')
            elif resulbebida2.upper() == 'VOU QUERER A BEBIDA 6':
                print('\nUm vinho pra aquecer a noite')
            elif resulbebida2.upper() == 'VOU QUERER A BEBIDA 7':
                print('\nAnimar a noite!')
            elif resulbebida2.upper() == 'VOU QUERER A BEBIDA 8':
                print('\nOtimo pra ter uma noite agitada!')
        elif pedirbebida2.upper() == 'NÃO':
            print('\nTudo bem, vou mandar fazer seu pedido')
            
    elif pedido1.upper() == 'AINDA NÃO':
        print('\nOk, retornarei mais tarde')

        pedido4 = str(input('\n'))
        if pedido4.upper() == 'PODE ANOTAR MEU PEDIDO?':
            print('\nPosso sim, qual seria?')
            
            pedido5 = str(input('\n'))
            if pedido5.upper() == 'VOU QUERER O PRATO 1':
                print('\nTudo bem, seu pedido já está sendo preparado!')
            elif pedido5.upper() == 'VOU QUERER O PRATO 2':
                print('\nOK, irei preparar esse!')
            elif pedido5.upper() == 'VOU QUERER O PRATO 3':
                print('\nCerto, vou prepara-lo imediadamente!')
            elif pedido5.upper() == 'VOU QUERER O PRATO 4':
                print('\nAmante de Strogoff né? Vou mandar preparar!')
            elif pedido5.upper() == 'VOU QUERER O PRATO 5':
                print('\nPerfeito, já está fazendo!')
            elif pedido5.upper() == 'VOU QUERER O PRATO 6':
                print('\nOtima escolha!')
            elif pedido5.upper() == 'VOU QUERER O PRATO 7':
                print('\nUma sopa saindo!')
            elif pedido5.upper() == 'VOU QUERER O PRATO 8':
                print('\nOk, a iguaria do Chefe então!')

            pedirbebida3 = str(input('\nAceita uma bebida? '))
            if pedirbebida3.upper() == 'SIM':
                print('\nQual seria?')
                resulbebida3 = str(input('\n'))
                if resulbebida3.upper() == 'VOU QUERER A BEBIDA 1':
                    print('\nBoa escolha, uma opção sempre saudavel!')
                elif resulbebida3.upper() == 'VOU QUERER A BEBIDA 2':
                    print('\nUm gás saudavel, tudo bem')
                elif resulbebida3.upper() == 'VOU QUERER A BEBIDA 3':
                    print('\nUm refrigerante, tudo bem')
                elif resulbebida3.upper() == 'VOU QUERER A BEBIDA 4':
                    print('\nSuco natural é sempre bom mesmo!')
                elif resulbebida3.upper() == 'VOU QUERER A BEBIDA 5':
                    print('\nUma cervejinha gelada saindo!')
                elif resulbebida3.upper() == 'VOU QUERER A BEBIDA 6':
                    print('\nUm vinho pra aquecer a noite')
                elif resulbebida3.upper() == 'VOU QUERER A BEBIDA 7':
                    print('\nAnimar a noite!')
                elif resulbebida3.upper() == 'VOU QUERER A BEBIDA 8':
                    print('\nOtimo pra ter uma noite agitada!')
            elif pedirbebida3.upper() == 'NÃO':
                print('\nTudo bem, vou mandar fazer seu pedido')

from time import sleep 
print('\nPreparando pedido')
sleep(2)
print('Preparando pedido.')
sleep(2)
print('Preparando pedido..')
sleep(2)
print('Preparando pedido...')
sleep(2)
print('Finalizando pedido')
sleep(2)
print('Finalizando pedido.')
sleep(2)
print('Finalizando pedido..')
sleep(2)
print('Finalizando pedido...')
sleep(6)

print('\nSeu pedido está pronto, tenha um bom apetite!')

sleep(5)