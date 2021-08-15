nome = input('Digite seu nome: ');
peso = float(input(nome +', quanto você pesa em em Kg? (kg) '));
altura = float(input('Quanto você mede em altura? (m) '));
imc = peso/(altura ** 2);

print(nome +', o seu IMC é de {:.1f}'.format(imc));

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
