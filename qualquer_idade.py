print("Em que ano você nasceu?")
nascimento = input()
nascimento = int(nascimento)
print("Para qual ano você quer saber sua idade?")
idadequalquer = input()
idadequalquer = int(idadequalquer)
idadefinal = idadequalquer - nascimento
print( "No ano ", idadequalquer , "você terá", idadefinal, "anos!")
