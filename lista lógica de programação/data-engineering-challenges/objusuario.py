from classusuario import usuario

user = usuario (
    "João","saraiva", "felicio",  2004, "Joãosaraivx@gmail.com", "(21) 99619-2178")
print(user.nome_completo())
print( user.calcular_idade())
print( user.email)
print( user.number_cellphone)