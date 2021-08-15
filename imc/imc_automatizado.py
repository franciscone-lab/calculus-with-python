imcGeral = 0;
i = 0;

qtdImc = int(input('Qtd de pessoas: '));
                   
while i < qtdImc:
    print('');
    print(f'Pessoa {i + 1}');
    nome = input('Digite seu nome: ');
    peso = float(input(f'{nome}, quanto você pesa em em Kg? (kg) '));
    altura = float(input('Quanto você mede em altura? (m) '));
    imc = peso/(altura ** 2);
    imcGeral += imc;
    print(f'{nome}, o seu IMC é de {imc:.1f}');
    if imc < 18.5:
        print('Diagnóstico: Abaixo do peso normal');
    elif imc >= 18.5 and imc < 25:
        print('Diagnóstico: Peso normal');
    elif imc >= 25 and imc < 30:
        print('Diagnóstico: Sobrepeso');
    elif imc >= 30 and imc < 40:
        print('Diagnóstico: Obeso');
    elif imc >= 40:
        print('Diagnóstico: Obesidade Mórbida');
    i += 1;

print('');
print('A media de IMC é de: {:.2f}'.format(imcGeral/qtdImc));
