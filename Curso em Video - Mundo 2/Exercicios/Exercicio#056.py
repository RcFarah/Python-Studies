# Exercicio #056

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
# do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idade_lista = []
nome_lista = []
sexo_lista = []
mulher_menos_vinte = 0
homem_mais_velho = 0
nome_homem_velho = ''

for infos in range(1, 5):
    print('------ PESSOA {} ------'.format(infos))

    nome = str(input('Digite o nome da pessoa: ')).strip().title()
    nome_lista.append(nome)

    idade = int(input('Digite a idade da pessoa: '))
    idade_lista.append(idade)

    sexo = int(input('Selecione a opção com o sexo da pessoa:\n'
                     '[1] Masculino\n'
                     '[2] Feminino\n'
                     '[3] Outros\n'))
    if sexo == 1:
        sexo_lista.append('Masc')
        homem_mais_velho += idade
        nome_homem_velho = nome
        if homem_mais_velho < idade:
            homem_mais_velho = idade
            nome_homem_velho = nome

    elif sexo == 2:
        sexo_lista.append('Fem')

        if idade <= 20:
            mulher_menos_vinte = mulher_menos_vinte + 1

    elif sexo == 3:
        sexo_lista.append('Outro')

soma_idades = sum(idade_lista)
media_idade = soma_idades / 4

print('A média de idade do grupo é de: {}\n'
      'O homem mais velho do grupo é: {}\n'
      'Tem {} mulheres com menos de 20 anos.'.format(int(media_idade), nome_homem_velho, mulher_menos_vinte))
