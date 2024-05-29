#da erro por que separa letras maiusculas de minusculas
#dicionario
pessoa ={
    'Nome': 'Alex Machado',
    'Idade':39,
    'Profissão':'Progrmador',
    'Empresa':'Senai',
     'Gênero':'Mascolino',
     'Cidade':'Taguatinga'
}
#remover chave
del pessoa [input('Informe o nome da chave a ser deletada: ')]

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')