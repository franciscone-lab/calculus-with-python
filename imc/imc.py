nome = input('Digite seu nome: ');
peso = float(input(nome +', quanto você pesa em em Kg? (kg) '));
altura = float(input('Quanto você mede em altura? (m) '));
imc = peso/(altura ** 2);

print(nome +', o seu IMC é de {:.2f}'.format(imc));
