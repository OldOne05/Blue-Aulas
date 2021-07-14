class Calendário():
    def __init__(self):
        self.dia = 1

    def __str__(self):
        return f"{self.dia}"

    def pulaDia(self):
        self.dia += 1

class personagens():
    def __init__(self):
        self.sujo = False
        self.fome = 0  #Máximo de 3 até de morrer de fome
        self.doente = 0 #Máximo de 2 até de morrer de doença
        self.vida = True
        self.saiu = False
        self.descansado = True
        self.sanidade = 0 #Máximo de 3 até endoidar
        
        if self.fome == 3:    
            self.vida = False
        if self.descansado == False:
            self.sanidade += 0.5
        if self.fome < 0:
            self.fome = 0
        if self.doente == 2:
            self.vida = False

    def __str__(self):
        if self.saiu == True:
            return f" está fora de casa."
        else:
            return f" está " + ("vivo(a), " + (("sujo(a), " if self.sujo else "limpo(a), ") + ("com fome, " if self.fome >= 1.5 else "sem fome, ") + ("está mentalmente bem, " if self.sanidade <= 1.5 else "está com sinais de loucura, ") + ("descansado(a) e " if self.descansado else "cansado(a) e ") + ("doente." if self.doente >= 1 else "saudável.")) if self.vida else "morto(a).")
    
    def descansar(self):
        self.descansado = True
        self.fome += 0.5
        self.sujo = True
        if self.doente > 0:
            self.doente += 0.5
        if self.sanidade > 0:
            self.sanidade += 0.5
        if self.fome == 3:    
            self.vida = False
        if self.descansado == False:
            self.sanidade += 0.5
        if self.fome < 0:
            self.fome = 0
        if self.doente == 2:
            self.vida = False

class itens():
    def __init__(self):
        self.comida = 10
        self.agua = 10
        self.arma = 1
        self.mascara = 1
        self.cadeado = 1
        self.Cadeadoqbr = 1
        self.radio = 1
        self.baralho = 1
        self.gaita = 1
        self.violao = 1
        self.remedio = 5

def alimentar():
    alimentar = input("Você quer alimentar os personagens?[Sim/Não] \U0001F35C ").replace(" ","").lower()
    while alimentar not in ["sim", "não", "nao"]:
        print("Resposta inválida")
        alimentar = input("Você quer alimentar os personagens?[Sim/Não] \U0001F35C ").replace(" ","").lower()
    while alimentar == "sim":
        print("Quem você quer alimentar? (ALIMENTAR ALGUÉM = -1 COMIDA E -1 ÁGUA)")
        if dolores.vida == True and dolores.saiu == False:
            print("Alimentar Dolores?")
        elif dolores.vida == False:
            print("Dolores está morto")
        elif dolores.saiu == True:
            print("Dolores saiu")
        if jose.vida == True and jose.saiu == False:
            print("Alimentar José?")
        elif jose.vida == False:
            print("José está morto")
        elif jose.saiu == True:
            print("José saiu")
        if ana.vida == True and ana.saiu == False:
            print("Alimentar Ana?") 
        elif ana.vida == False:
            print("Ana está morta")
        elif ana.saiu == True:
            print("Ana saiu")
        if carlos.vida == True and carlos.saiu == False:
            print("Alimentar Carlos?")
        elif carlos.vida == False:
            print("Carlos está morto")
        elif carlos.saiu == True:
            print("Carlos saiu")


        escolha = input("\n---*Digite o nome do personagem. Se não quiser comer ou ninguém estiver em casa, digite (0)").replace(" ","").lower()
        while escolha not in ["dolores","carlos","ana",'jose',"josé", "0"]:
            print("Resposta inválida")
            escolha = input("---").replace(" ","").lower()

        if escolha == "dolores":
            dolores.fome = 0
            bau.comida -= 1
            bau.agua -= 1
        if escolha == "josé" or escolha == "jose":
            jose.fome = 0
            bau.comida -= 1
            bau.agua -= 1
        if escolha == "ana":
            ana.fome = 0
            bau.comida -= 1
            bau.agua -= 1
        if escolha == "carlos":
            carlos.fome = 0
            bau.comida -= 1
            bau.agua -= 1
        if escolha == "0":
            alimentar = "não"
        elif escolha != "0":
            alimentar = input("Deseja continuar alimentando a família? [Sim/Não] \U0001F35C ").replace(" ","").lower()
            while alimentar not in ["sim", "não", "nao"]:
                print("Resposta inválida")
                alimentar = input("Deseja continuar alimentando a família? [Sim/Não] \U0001F35C ").replace(" ","").lower()

jogar = "sim"
while jogar == "sim":
    if __name__ == "__main__":
        calendario = Calendário()
        dolores = personagens()
        jose = personagens()
        ana = personagens()
        carlos = personagens()
        bau = itens()
        invent = {"Espingarda":bau.arma, "Máscara de proteção": bau.mascara, "Cadeado": bau.cadeado, "Cadeado enferrujado": bau.Cadeadoqbr, "Rádio": bau.radio, "Baralho":bau.baralho, "Gaita": bau.gaita, "Violão": bau.violao}
        print("---"*14)
        print(' \U0001F927	\U0001F912 GRIPÃO A DOENÇA FATAL \U0001F927 \U0001F912')
        print()
        print('Chegou no país uma terrível doença chamada Gripão que esta matando as pessoas e o')
        print('governo decidiu colocar a população em um extremo confinamento em suas casas até que a')
        print('cura chegue ou que não tenha mais a doença no país.')
        print('Sua família, Mãe Dolores, Pai José, filha Ana e filho Carlos, precisam se proteger desta terrível doença.')
        print()
        print('Você decide o que fazer!')
        print()
        print(' \U0001F3AE	Que comece o jogo!!! \U0001F3AE')
        print()
        
        while True:
            print("---"*14)
            print(f"Hoje é o Dia {calendario} de quarentena.")
            print(f"Você(s) tem {bau.comida} de comida, {bau.remedio} remédios e {bau.agua} de água.")
            print("1 valor de comida ou água alimenta ou hidrata bem uma pessoa.")
            print(f"Seus itens ---> {invent}")
            print()
            print("---"*7)
            print(f"Dolores{dolores}")
            print(f"José{jose}")
            print(f"Ana{ana}")
            print(f"Carlos{carlos}")
            print("---"*14)
            print()
            
            if dolores.vida == False and carlos.vida == False and jose.vida == False and ana.vida == False:
                print("Todos morreram")
                print("Fim de jogo.")
                emoji = print("\U0001F637")
                print(f"Use máscara ")
                print()
                print("---CRÉDITOS---")
                print("Cauã Muliterno Marinho Campos")
                print("Rudhy Maycon Pereira da Costa")
                print("Marcelo da Rocha Machado")
                jogar = input("Você quer jogar novamente? (Sim/Não").replace(" ","").lower()
                while jogar not in ["sim", "não", "nao"]:
                    print("Resposta inválida")
                    jogar = input("Você quer jogar novamente? (Sim/Não").replace(" ","").lower()
                if jogar == "não" or jogar == "nao":
                    break

            if calendario.dia == 1:
                print()
                radio = input('O rádio amador está tocando, deseja ouvir a notícia ? (Sim/Não): \U0001F4FB ').replace(" ","").lower()
                while radio not in ["sim", "não", "nao"]:
                    print("Resposta Inválida")
                    radio = input('O rádio amador está tocando, deseja ouvir a notícia ? (Sim/Não): \U0001F4FB ').replace(" ","").lower()
                if radio == 'sim':
                    print('Está sendo noticiado que para sair brevemente do abrigo deve-se usar a mascara de proteção, pois do contrário você poderá ser contaminado com o GRIPÃO e contaminar toda a sua família!')
                else:
                    print('A mãe resolveu sair do abrigo sem mascara para ver a situação lá fora, porém como estava muito frio parece que se resfriou e terá que tomar remédio para não piorar!')
                    print(f'Ainda tem {bau.remedio} remédios no estoque')
                    remedio = input("Você quer dar o remédio para a mãe? (Sim/Não): \U0001F48A ").replace(" ","").lower()
                    while remedio not in ["sim", "não", "nao"]:
                        print("Resposta Inválida")
                        remedio = input("Você quer dar o remédio para a mãe? (Sim/Não): \U0001F48A ").replace(" ","").lower()
                    if remedio == "sim":
                        dolores.doente = 0
                    else:
                        dolores.doente += 1
                        print("Dolores contraiu algo... diferente. \U0001F922	")                            
            
            elif calendario.dia == 2:
                print()
                print("Barulhos do lado de fora. \U0001F628	")
                sair = input('Você quer ir lá fora ver o que é o barulho? (Sim/Não): ').replace(" ","").lower()
                while sair not in ["sim", "não", "nao"]:
                    print("Resposta Inválida")
                    sair = input('Você quer ir lá fora o que é o barulho? (Sim/Não): ').replace(" ","").lower() 
                if sair == 'sim':
                    print('Você vê um grupo de vândalos invadindo outras casas em busca de alimentos.')
                    cadeado = input("Quer fechar a porta com um cadeado? (Sim/Não): \U0001F6AA	").replace(" ","").lower()
                    while cadeado not in ["sim", "não", "nao"]:
                        print("Resposta Inválida")
                        cadeado = input("Quer fechar a porta com um cadeado? (Sim/Não): ").replace(" ","").lower()
                    if cadeado == "sim":
                        cadeado = input("Vocês tem 2 cadeados, um está enferrujado e o outro não, mas é de uma marca duvidosa.Qual você quer usar? [1->Enferrujado/2->Normal, mas duvidoso] ").replace(" ","").lower()
                        while cadeado not in ["1", "2"]:
                            print("Resposta Inválida")
                            cadeado = input("Vocês tem 2 cadeados, um está enferrujado e o outro não, mas é de uma marca duvidosa.Qual você quer usar? [1->Enferrujado/2->Normal, mas duvidoso] ").replace(" ","").lower()
                        if cadeado == "2":
                            print("O cadeado realmente não era confiável, os vândalos entraram e mataram toda a família.")
                            print()
                            dolores.vida = False
                            jose.vida = False
                            ana.vida = False
                            carlos.vida = False
                        elif cadeado == "1":
                            print("A família dormiu tranquilamente.")
                    else:
                        print("Os vândalos entraram e mataram toda a família.")
                        print()
                        dolores.vida = False
                        jose.vida = False
                        ana.vida = False
                        carlos.vida = False
                else:
                    print('Ficamos apreensivos com o barulho vindo do lado de fora e não tivemos coragem de abrir a porta!')

            elif calendario.dia == 3:
                baralho = input("Ana está entediada em ficar em casa todo o dia, quer jogar baralho com ela? (Sim/Não): ").replace(" ","").lower()
                while baralho not in ["sim", "não", "nao"]:
                    print("Resposta Inválida")
                    baralho = input("Ana está entediada em ficar em casa todo o dia, quer jogar baralho com ela? (Sim/Não): ").replace(" ","").lower()
                if baralho == "não" or baralho == "nao":
                    print("Ninguém quer brincar comigo, desse jeito vou ter que brincar comigo mesma. \U0001F92C	")
                    ana.sanidade += 1
            
            elif calendario.dia == 4:
                print("O rádio amador está tocando, deseja ligar? (Sim/Não) \U0001F4FB	")
                radio2 = input("--")
                while radio2 not in ["sim", "não", "nao"]:
                    print("Resposta Inválido")
                    radio2 = input("Deseja ligar? ")
                if radio2 == "sim":
                    print("Vocês sabem pelo rádio que uma vacina esta sendo produzida para salvar a humanidade.")
                print()
                if ana.sanidade > 0:
                    print("Ana está um pouco estranha, está falando com um tal de Matheus, só que não tem nenhum Matheus aqui. \U0001F47B \U0001F47B")

            elif calendario.dia == 5:
                print()
                print('Precisamos que alguém que vá a rua e procure por comida e água.')
                print("Alguém tem que sair para coletar suprimentos, quem vai sair?")
                if dolores.vida == True:
                    print("01 -- Dolores")
                if jose.vida == True:
                    print("02 -- José")
                if ana.vida == True:
                    print("03 -- Ana")
                if carlos.vida == True:
                    print("04 -- Carlos")
                sair = input("---Diga o número equivalente:").replace(" ","")
                while sair not in ["01", "02", "03", "04", "1", "2", "3", "4"]:
                    print("Pessoa Inválida")
                    sair = input("---Diga o número").replace(" ","")
                if sair == "01" or sair == "1":
                    dolores.saiu = True

                elif sair == "02" or sair == "2":
                    jose.saiu = True
                elif sair == "03" or sair == "3":
                    ana.saiu = True
                elif sair == "04" or sair == "4":
                    carlos.saiu = True
                    carlos.doente = 1
                
                item = {"Máscara" : bau.mascara, "Espingarda": bau.arma, "Comida" : bau.comida, "Remédio" : bau.remedio, "Gaita" : bau.gaita}
                mochila = {}
                
                for key,value in item.items():
                    print(key)
                    oque = input(f'Você quer levar esse item? (Sim/Não) ').replace(" ","").lower()
                    while oque not in ["sim", "não", "nao"]:
                        print("Resposta inválida")
                        oque = input(f'Você quer levar esse item? (Sim/Não) ').replace(" ","").lower()
                    if oque == "sim":
                        mochila.update({key:value})
                        print(mochila)          
                    if "Remédio" in mochila and "Comida" in mochila:
                        troca = input("Você só pode levar comida ou remédio,\n qual você quer descartar? (Comida/Remédio) ").replace(" ","").lower()
                        while troca not in ["comida", "remédio", "remedio"]:
                            print("Opção Inválida")
                            troca = input("Qual você quer descartar? (Comida/Remédio) ").replace(" ","").lower()
                        if troca == "comida":
                            mochila.pop("Comida", bau.comida) 
                        else:
                            mochila.pop("Remédio", bau.remedio)
                    else:
                        pass

            elif calendario.dia == 6:
                print()
                print('Retorno da Expedição')
                if 'Espingarda' in mochila:
                    print(f'A arma era antiga e não disparou contra os bandidos. O Personagem foi morto.!! ')
                    if dolores.saiu == True:
                        dolores.vida = False
                    elif jose.saiu == True:
                        jose.vida = False
                    elif ana.saiu == True:
                        ana.vida = False
                    elif carlos.saiu == True:
                        carlos.vida = False
                else: 
                    if 'Máscara' in mochila:
                        bau.mascara -= 1
                        print(f'O personagem voltou doente, pois a mascara rasgou. Será necessário dar remédio. \U0001F912	\U0001F48A	')
                        remedio = input("Você quer dar o remédio? (Sim/Não): \U0001F48A ").replace(" ","").lower()
                        while remedio not in ["sim", "não", "nao"]:
                            print("Resposta Inválida")
                            remedio = input("Você quer dar o remédio? (Sim/Não): \U0001F48A ").replace(" ","").lower()
                        if remedio == "sim":
                            bau.remedio -= 1
                        else:
                            if dolores.saiu == True:
                                dolores.doente = 1
                            elif jose.saiu == True:
                                jose.doente = 1
                            elif ana.saiu == True:
                                ana.doente = 1
                            elif carlos.saiu == True:
                                carlos.doente = 1
                    
                    if 'Remédio' in mochila:
                        print('O Personagem conseguiu trocar uma unidade de remédio por uma unidade de comida e água')
                        bau.remedio -= 1
                        bau.comida += 1
                        bau.agua += 1
                    if 'Gaita' in mochila:
                        print('O Personagem conseguiu trocar a gaita por uma unidade de comida, água e remédio')
                        bau.gaita -= 1
                        bau.comida += 2
                        bau.agua += 2
                        bau.remedio += 1
                    if dolores.saiu == True:
                        dolores.saiu = False
                    elif jose.saiu == True:
                        jose.saiu = False
                    elif ana.saiu == True:
                        ana.saiu = False
                    elif carlos.saiu == True:
                        carlos.saiu = False
                    print()
                    if ana.vida == True and ana.sanidade >= 2.5:
                        print("A família ouviu da cozinha um barulho de alguém correndo, chegando lá viram a Ana no canto da sala com as luzes apagadas \n quando foram falar com ela, ana saiu correndo e se trancou no quarto.\n Não conseguimos abrir a porta e só ouvimos vozes baixas dela e de outra pessoa, mas não temos certeza, talvez seja só o sono. \U0001F479	\U0001F479")
            
            elif calendario.dia == 7:
                print()
                if ana.vida == True and ana.sanidade >= 2.5:
                    if jose.vida == True:
                        print("Dolores vê que porta de ana está escancarada ao amanhecer, ao abrir a porta, é surpeendida pela Ana ensanguentada \ne vê que seu marido José está morto atrás da cama. \U0001F480	")
                        print("\U0001F52A")
                        print("Ana está assustada e não para de repetir 'FOI O MATHEUS, FOI O MATHEUS, FOI O MATHEUS' incessantemente")
                        print("A família está completamente abalada")
                        jose.vida = False
                    elif dolores.vida == True:
                        print("José vê que porta de ana está escancarada ao amanhecer, ao abrir a porta, é surpeendida pela Ana ensanguentada \ne vê que sua mulher Dolores está morta atrás da cama.")
                        print("\U0001F52A")
                        print("Ana está assustada e não para de repetir 'FOI O MATHEUS, FOI O MATHEUS, FOI O MATHEUS' incessantemente")
                        print("A família está completamente abalada")
                        dolores.vida = False

            elif calendario.dia == 8:
                print("Vocês ouvem batidas na porta.Descobrimos que se tratava de um grupo de mendigos \ne estavam em condições bem piores e nos imploraram por um pouco de comida, água e remédios.")
                doar = input("Vocês darão 2 comidas, 2 águas e 1 remédio? (Sim/Não").replace(" ","").lower()
                while doar not in ["sim", "não", "nao"]:
                    print("Resposta inválida")
                    doar = input("Vocês darão 2 comidas, 2 águas e 1 remédio?").replace(" ","").lower()
                if doar == "sim":
                    bau.comida -= 2
                    bau.agua -= 2
                    bau.remedio -= 2
                else:
                    pass

            elif calendario.dia == 9:
                if doar == "sim":
                    print("O mendigo que você ajudou, agora é o líder de uma comunidade e trouxe provisão para vocês. \U0001F47C	")
                    bau.comida += 2
                    bau.agua += 2

            elif calendario.dia == 10:
                print("Um vendedor bateu em nossa porta. Ele se apresentou e pelo jeito, o comércio não acabou com essa pandemia. \nEle quer fazer uma troca...")
                print("1 – oferece um remédio e em troca lhe dará uma caixa com 3 balas para espingarda")
                print("2 - oferece um garrafa de água e comida e em troca lhe dará uma mascara")
                comercio = input("Qual troca você fará? (Digite o número da troca, se não quiser trocar digite 0)").replace(" ","")
                while comercio not in ["1", "2", "01","02", "0", "00"]:
                    print("Resposta inválida")
                    comercio = input("Qual troca você fará").replace(" ","")
                if comercio == "1" or comercio == "01":
                    bau.remedio -= 1
                    bau.arma += 3
                    print("Troca realizada com sucesso")
                elif comercio == "2" or comercio == "02":
                    bau.comida -= 1
                    bau.agua -= 1
                    bau.mascara += 1
                    print("Troca realizada com sucesso")
                else:
                    pass

            elif calendario.dia == 11:
                radio3 = input("O rádio amador está tocando, deseja ligar? (Sim/Não) ")        
                while radio3 not in ["sim", "não", "nao"]:
                    print("Resposta inválida")
                    radio3 = input("O rádio amador está tocando, deseja ligar? (Sim/Não) ")
                if radio3 == "sim":
                    print("A vacina está pronta e as ruas vão ser desinfetadas amanhã, logo após, a aplicação da vacina vai começar  \U0001F489	")
                    print("Todos estão animados!!")
                else:
                    print("Vemos pessoas com roupas de proteção pela janela, devem ser do governo, mas o que estão fazendo?")

            elif calendario.dia == 12:
                radio4 = input("O rádio amador está tocando, deseja ligar? (Sim/Não) ")        
                while radio4 not in ["sim", "não", "nao"]:
                    print("Resposta inválida")
                    radio4 = input("O rádio amador está tocando, deseja ligar? (Sim/Não) ")
                if radio4 == "sim":
                    print("Amanhã é o dia da vacinação, já terminamos a desinfeccão nas ruas, ainda podem ter resquícios do Gripão.")

            elif calendario.dia == 13:
                print("Toda a população junto com a família foram se vacinar hoje, imunizados 100% \U0001F489 \U0001F489")
                print()
                print("VOCÊ GANHOU O JOGO, PARABÉNS \U0001F389	")
                emoji = print("\U0001F637")
                print(f"Use máscara \U0001F637")
                print()
                print("---CRÉDITOS---")
                print("Cauã Muliterno Marinho Campos")
                print("Rudhy Maycon Pereira da Costa")
                print("Marcelo da Rocha Machado")
                jogar = input("Você quer jogar novamente? (Sim/Não").replace(" ","").lower()
                while jogar not in ["sim", "não", "nao"]:
                    print("Resposta inválida")
                    jogar = input("Você quer jogar novamente? (Sim/Não").replace(" ","").lower()
                if jogar == "não" or jogar == "nao":
                    break
            
            if bau.remedio > 0:
                if dolores.doente >= 1.5 and dolores.vida == True:
                    dar_remedio = input("DOLORES ESTÁ MORRENDO COM A DOENÇA, QUER DAR O REMÉDIO PARA ELA? (Sim/Não) ").replace(" ","").lower()
                    while dar_remedio not in ["sim", "não", "nao"]:
                        print("Resposta inválida")
                        dar_remedio = input("QUER DAR O REMÉDIO PARA ELA? (Sim/Não) ").replace(" ","").lower()
                    if dar_remedio == "sim"and bau.remedio > 0:
                        dolores.doente = 0
                        bau.remedio -=1
                elif carlos.doente >= 1.5 and carlos.vida == True:
                    dar_remedio = input("CARLOS ESTÁ MORRENDO COM A DOENÇA, QUER DAR O REMÉDIO PARA ELE? (Sim/Não) ").replace(" ","").lower()
                    while dar_remedio not in ["sim", "não", "nao"]:
                        print("Resposta inválida")
                        dar_remedio = input("QUER DAR O REMÉDIO PARA ELE? (Sim/Não) ").replace(" ","").lower()
                    if dar_remedio == "sim" and bau.remedio > 0:
                        carlos.doente = 0
                        bau.remedio -=1
                elif jose.doente >= 1.5 and jose.vida == True:
                    dar_remedio = input("JOSÉ ESTÁ MORRENDO COM A DOENÇA, QUER DAR O REMÉDIO PARA ELE? (Sim/Não) ").replace(" ","").lower()
                    while dar_remedio not in ["sim", "não", "nao"]:
                        print("Resposta inválida")
                        dar_remedio = input("QUER DAR O REMÉDIO PARA ELE? (Sim/Não) ").replace(" ","").lower()
                    if dar_remedio == "sim"and bau.remedio > 0:
                        jose.doente = 0
                        bau.remedio -=1
                elif ana.doente >= 1.5 and ana.vida == True:
                    dar_remedio = input("ANA ESTÁ MORRENDO COM A DOENÇA, QUER DAR O REMÉDIO PARA ELA? (Sim/Não) ").replace(" ","").lower()
                    while dar_remedio not in ["sim", "não", "nao"]:
                        print("Resposta inválida")
                        dar_remedio = input("QUER DAR O REMÉDIO PARA ELA? (Sim/Não) ").replace(" ","").lower()
                    if dar_remedio == "sim"and bau.remedio > 0:
                        ana.doente = 0
                        bau.remedio -=1
            
            if dolores.vida == False and carlos.vida == False and jose.vida == False and ana.vida == False:
                print("Todos morreram")
                print("Fim de jogo.")
                emoji = print("\U0001F637")
                print(f"Use máscara ")
                print()
                print("---CRÉDITOS---")
                print("Cauã Muliterno Marinho Campos")
                print("Rudhy Maycon Pereira da Costa")
                print("Marcelo da Rocha Machado")
                jogar = input("Você quer jogar novamente? (Sim/Não").replace(" ","").lower()
                while jogar not in ["sim", "não", "nao"]:
                    print("Resposta inválida")
                    jogar = input("Você quer jogar novamente? (Sim/Não").replace(" ","").lower()
                if jogar == "não" or jogar == "nao":
                    break
            
            
            if bau.comida > 0:
                alimentar()
            calendario.pulaDia()
            dolores.descansar()
            jose.descansar()
            ana.descansar()
            carlos.descansar()
            print()