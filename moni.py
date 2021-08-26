import psutil, datetime;

print('1.CPU \n2.DISCO \n3.RAM')

componentes = int(input('O que você gostaria de monitorar? '))

arrayCPU1 = []
arrayCPU2 = []
arrayCPU3 = []

arrayMEMO1 = []
arrayMEMO2 = []
arrayMEMO3 = []

arrayDISCO1 = []
arrayDISCO2 = []
arrayDISCO3 = []



if (componentes == 1): 
    # data_e_hora_atuais = datetime.now()
    # data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
    # print(data_e_hora_em_texto)

    while (True):
            cpu1 = psutil.cpu_percent(interval=5)
            cpu2 = cpu1 * 1.1
            cpu3 = cpu1 * 1.05

            arrayCPU1 += [cpu1]
            arrayCPU2 += [cpu2]
            arrayCPU3 += [cpu3]

            print(cpu1, '%')
            print(cpu2, '%')
            print(cpu3, '%')
            print('\n')

elif (componentes == 2):
    while (True):

            memo1 = psutil.virtual_memory().percent
            memo2 = memo1 * 1.15
            memo3 = memo1 * 1.20

            arrayMEMO1 += [memo1]
            arrayMEMO2 += [memo2]
            arrayMEMO3 += [memo3]

            print(memo1, '%')
            print(memo2, '%')
            print(memo3, '%')
            print('\n')

elif (componentes == 3):
    while (True):

            disco1 = psutil.disk_usage('/').percent
            disco2 = (disco1 * 0.95)
            disco3 = disco2 * 3

            arrayDISCO1 += [disco1]
            arrayDISCO2 += [disco2]
            arrayDISCO3 += [disco3]

            print(disco1, '%')
            print(disco2, '%')
            print(disco3, '%')
            print('\n')
else:
    print('Erro')

# memo1 = psutil.virtual_memory().percent
# memo2 = memo1 * 1.15
# memo3 = memo1 * 1.20

# disco1 = psutil.disk_usage('/').percent
# disco2 = (disco1 * 0.95)
# disco3 = disco2 * 3

