math = float(input('Insira a nota de matemática:    '))
port = float(input('Insira a nota de português:   '))
ing = float(input('Insira a nota de inglês:   '))

media = (math + port + ing) / 3

if media <= 5:
    print(f'''A nota do aluno foi {media:.2f}
          Reprovado!''')
elif media < 7:
    print(f'''A nota do aluno foi {media:.2f}
          Recuperação!''')
elif media >= 7:
    print(f'''A nota do aluno foi {media:.2f}
          Aprovado!''')
    