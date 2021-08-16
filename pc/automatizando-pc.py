import psutil

qtdPcs = int(input('Qtd de Máquinas: '))

print('\n 1.CPU \n 2.Disco \n')
tipoPeca = int(input('Qual equipamento você gostaria de monitorar? '))

def loopEspecificacoes(especificacoes):
    i = 0;
    while i < qtdPcs:
        print(especificacoes);
        i+= 1;

if tipoPeca == 0 or tipoPeca > 2:
    print('Número Inválido')
    
elif tipoPeca == 1:
    especificacoes = psutil.cpu_times_percent();
    loopEspecificacoes(especificacoes);

else:
    especificacoes = psutil.disk_usage('/home');
    loopEspecificacoes(especificacoes);
