print("\nBem Vindo ao PucFit! Por favor, insira as próximas informações para cadastro ")

usuario_cadastro = input("\nCrie um nome de usuario para cadastro ou insira seu email: ")
senha_cadastro = input("\nCrie uma senha de cadastro: ")

logado = False

while logado == False:
    print('\n-----LOGIN-----')
    usuario = input("\nDigite seu nome de usuario ou email: ")
    senha = input("\nDigite sua senha : ")

    if usuario == usuario_cadastro and senha == senha_cadastro:
        print("\nLogin feito com sucesso")
        logado = True
    else:
        print("\nLogin incorreto, senha ou Usuario incorretos, Digite novamente")

print("\nBem Vindo ao PucFit! Por favor, insira as próximas informações ")


peso_valido = False
while peso_valido == False:
    peso_user = float(input("\nDigite o seu peso em kg: "))
    if peso_user > 0:
        peso_valido = True
    else:
        print("\nPeso inválido, Digite Novamente")

altura_valida = False
while altura_valida == False:
    altura_user = float(input("\nDigite sua altura em metros: "))
    if altura_user > 0:
        altura_valida = True
    else:
        print("\nAltura inválida, Digite novamente")

imc_calculado = False
hidratacao_calculada = False
calorias_calculadas = False
meta_definida = False

executar = True

while executar == True:
    print('\n-----------MENU-----------'
          '\n 1: Calcule meu IMC'
          '\n 2: Calcule minha meta de hidratação diária'
          '\n 3: Estime meu gasto calórico de atividade física'
          '\n 4: Exiba minha meta diária de exercícios'
          '\n 5: Monte uma Dieta Básica (Opcional)'
          '\n 6: Exiba modelos especificos de Treinos de Musculação para mim (Opcional)'
          '\n 7: Meu resumo diário')

    seletor = input("\nDigite o número da opção que deseja acessar: ")

    if seletor == "1":
        print('\n-----------CALCULO DE IMC-----------\n')
        imc = peso_user / (altura_user**2)
        print(f"Seu IMC: {round(imc, 2)}")
        imc_calculado = True

        if imc < 18.5:
            print("\nAbaixo do peso")
        elif imc < 25:
            print("\nPeso normal")
        elif imc < 30:
            print("\nSobrepeso")
        else:
            print("\nObesidade")

    elif seletor == "2":
        print('\n-----------CALCULO DE META DE HIDRATAÇÃO DIÁRIA-----------\n')
        hidratacao_diaria = peso_user * 0.035
        print(f"Sua meta de hidratação diária é de: {round(hidratacao_diaria, 2)} L")
        hidratacao_calculada = True

    elif seletor == "3":
        print('\n-----------CALCULO DE GASTO CALÓRICO POR ATIVIDADE FÍSICA-----------\n'
              '\n1:Caminhada '
              '\n2:Corrida '
              '\n3:Musculação '
              '\n4:Ciclismo')

        atividade = input("\nDigite o número da atividade que deseja calcular: ")

        met_valido = False

        if atividade == "1":
            met = 3.5
            met_valido = True
        elif atividade == "2":
            met = 8.0
            met_valido = True
        elif atividade == "3":
            met = 6.0
            met_valido = True
        elif atividade == "4":
            met = 7.5
            met_valido = True
        else:
            print("\nAtividade inválida!")

        if met_valido == True:
            tempo = float(input("\nQuanto tempo (em minutos) de exercícios serão realizados?: "))
            calorias_gastas = met * peso_user * (tempo / 60)
            print(f"\nA sua quantidade de calorias gastas foi de: {round(calorias_gastas, 2)}")
            calorias_calculadas = True

    elif seletor == "4":
        print("\n-----------META DIÁRIA DE EXERCÍCIOS-----------\n"
              '\n Qual é o seu objetivo?'
              '\n 1: Emagrecer'
              '\n 2: Manter Peso'
              '\n 3: Ganhar Massa')

        objetivo = input("\nDigite o número do seu objetivo: ")

        # MET significa Equivalente Metabólico da Tarefa (Metabolic Equivalent of Task),
        #  é uma unidade de medida que quantifica o gasto energético de atividades físicas

        if objetivo == "1":
            meta_diaria = "45-60 min"
            meta_definida = True
        elif objetivo == "2":
            meta_diaria = "30-45 min"
            meta_definida = True
        elif objetivo == "3":
            meta_diaria = "60-90 min"
            meta_definida = True
        else:
            print("\nOpção inválida!")

        if meta_definida == True:
            print(f"\nSua meta diária de exercícios é: {meta_diaria}")

    elif seletor == "5":
        print("\n-----------DIÉTA BÁSICA-----------\n"
           '\nQual é o seu objetivo?'
            '\n1: Emagrecer'
            '\n2: Manter Peso'
            '\n3: Ganhar Massa')

        objetivo = input("\nDigite o numero do seu objetivo: ")

        if objetivo == "1":
            print("\n-----------DIÉTA PARA EMAGRECIMENTO-----------\n"
            "\nCafé da manhã: ovos + frutas"
            "\nAlmoço: frango grelhado + salada + arroz integral"
            "\nJantar: salada + proteína leve (frango ou peixe)"
            "\nEvitar: açúcar, refrigerante e frituras"
            "\nDica: manter déficit calórico e beber bastante água")

        elif objetivo == "2":
            print("\n-----------DIÉTA PARA MANTER PESO-----------\n"
            "\nCafé da manhã: pão integral + ovo + fruta"
            "\nAlmoço: arroz + feijão + carne + salada"
            "\nJantar: refeição leve equilibrada"
            "\nDica: manter alimentação equilibrada e rotina regular")

        elif objetivo == "3":
            print("\n-----------DIÉTA PARA EMAGRECIMENTO-----------\n"
            "\nCafé da manhã: ovos + aveia + banana"
            "\nAlmoço: arroz + feijão + carne + batata"
            "\nJantar: proteína + carboidrato (frango + arroz ou macarrão)"
            "\nDica: aumentar consumo de proteína e calorias")

        else:
            print("Opção Inválida!")

    elif seletor == "6":
        print("\n-----------SEU MODELO DE TREINO DE MUSCULAÇÃO-----------\n"
            '\n Escolha uma das opções abaixo!:\n'
            '\n 1: Ganho de massa'
            '\n 2: Definição'
            '\n 3: Força'
            '\n 4: Resistência Muscular')
        
        opçãot = (input("\nDigite o número de sua opção: "))
   
        if opçãot == "1":
            print ("\n-----------GANHO DE MASSA-----------\n"
                   '\nRepetições: 6–12'
                   '\nSéries: 3–5'
                   '\nDescanso: 60–90s'
                   '\nRitmo controlado'
                   '\n(dica: tente aumentar carga ou repetições toda semana)')
        elif opçãot == "2":
            print ("\n-----------DEFINIÇÃO-----------\n"
                    '\nRepetições: 12-15'
                    '\nSéries: 3-4'
                    '\nDescanso: 30–60s'
                    '\nMais intensidade'
                    '\n(dica: faça tudo em sequência (circuito), descanse e repita)')
        elif opçãot == "3":
            print ("\n-----------FORÇA-----------\n"
                    '\nRepetições: 1-5'
                    '\nSéries: 4-6'
                    '\nDescanso: 2-5min'
                    '\nPoucos exercícios, foco nos básicos'
                    '\n(dica: aqui qualidade é maior que quantidade. Se exagerar, você pode travar.)')
        elif opçãot == "4":
            print ("\n-----------TREINO PARA RESISTENCIA MUSCULAR-----------\n"
                    '\nRepetições: 15–25'
                    '\nSéries: 2–4'
                    '\nDescanso: 30–45s'
                    '\nCarga leve/moderada'
                    '\n(dica: Vai sentir queimação absurda, esse é o objetivo.)')
            
        else:
            print("\nOpção Inválida!")

    elif seletor == "7":
        print("\n-----------MEU RESUMO DIÁRIO-----------\n")

        if imc_calculado == True:
            print(f"Seu IMC: {round(imc, 2)}")
        else:
            print("Seu IMC: não calculado")

        if calorias_calculadas == True:
            print(f"Sua quantidade de calorias gastas: {round(calorias_gastas, 2)}")
        else:
            print("Sua quantidade de calorias gastas: nenhuma")

        if meta_definida == True:
            print(f"Sua meta diária de exercícios é: {meta_diaria}")
        else:
            print("Sua meta diária de exercícios é: não definida")

        if hidratacao_calculada == True:
            print(f"Meta de hidratação diária: {round(hidratacao_diaria, 2)} L")
        else:
            print("Meta de hidratação diária: não calculada")

    else:
        print("Opção inválida!")

    voltar = input("\nDeseja continuar o programa? (s/n): ").lower()

    if voltar == "s":
        continue

    elif voltar == "n":
        print("\nPrograma encerrado")
        executar = False

    else:
        print("Opcão Invalida!")