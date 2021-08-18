#Programa de cálculo de média utilizando 3 notas

nota1 = float(input('Sua Primeira Nota: '))
nota2 = float(input('Sua Segunda Nota: '))
nota3 = float(input('Sua Terceira Nota: '))
media = (nota1 + nota2 + nota3) / 3
print('Com as notas {:.1f}, {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, nota3, media))
if 7 > media >=5:
    print('O Aluno está em RECUPERAÇÃO!')
elif media < 5:
    print('O Aluno está REPROVADO!')
elif media >=7:
    print('O Aluno está APROVADO!')