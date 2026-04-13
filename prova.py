semestre = 1

while  semestre <= 2:

    cp1 = float(input("qual foi a sua nota do Checkpoint 1?: "))
   
    cp2 = float(input("Qual foi a sua nota do Checkpoint 2?: "))
   
    cp3 = float(input("Qual foi a sua nota do Checkpoint 3?: "))
   
    if cp1 <= cp2 and cp1 <= cp3:
   
        print(f"A menor nota foi a {float(cp1):.2f}, ela será descontada!")
        menor_nota = cp1
   
    elif  cp2 <= cp1 and cp2 <= cp3:
        print(f"A menor nota foi a {float(cp2):.2f}, ela será descontada!")
        menor_nota = cp2
    
    elif cp3 <= cp1 and cp3 <= cp2:
        print(f"A menor nota foi a {float(cp3):.2f}, ela será descontada!")
        menor_nota = cp3
    
    else:
        print("Não foi possivel entender oque você escreveu!")
    
    menor_cp = menor_nota
    
    sp1 = float(input("Qual foi a sua nota do Sprint 1 ?: "))
    
    sp2 = float(input("Qual foi a sua nota do Sprint 2?: "))
    
    gs = float(input("Qual foi a sua nota do Global Solution?: "))
    
    media = ((cp1 + cp2 + cp3 - menor_cp + sp1 + sp2) / 4) * 0.4 + gs * 0.6
    
    print(f"sua media foi {media:.2f}! e a sua media de peso foi")
    
    print(f"Esse foi o primeiro semestre!")

    media_primeiro = media

    semestre += 1

    print("Segundo semestre: ")

    cp1 = float(input("qual foi a sua nota do Checkpoint 1?: "))
   
    cp2 = float(input("Qual foi a sua nota do Checkpoint 2?: "))
   
    cp3 = float(input("Qual foi a sua nota do Checkpoint 3?: "))
   
    if cp1 <= cp2 and cp1 <= cp3:
   
        print(f"A menor nota foi a {float(cp1):.2f}, ela será descontada!")
        menor_nota = cp1
   
    elif  cp2 <= cp1 and cp2 <= cp3:
        print(f"A menor nota foi a {float(cp2):.2f}, ela será descontada!")
        menor_nota = cp2
    
    elif cp3 <= cp1 and cp3 <= cp2:
        print(f"A menor nota foi a {float(cp3):.2f}, ela será descontada!")
        menor_nota = cp3
    
    else:
        print("Não foi possivel entender oque você escreveu!")
    
    menor_cp = menor_nota
    
    sp1 = float(input("Qual foi a sua nota do Sprint 1 ?: "))
    
    sp2 = float(input("Qual foi a sua nota do Sprint 2?: "))
    
    gs = float(input("Qual foi a sua nota do Global Solution?: "))
    
    media2 = ((cp1 + cp2 + cp3 - menor_cp + sp1 + sp2) / 4) * 0.4 + gs * 0.6
    
    print(f"sua media foi {media:.2f}! e a sua media de peso foi")
    
    print(f"Esse foi o primeiro semestre!")

    media_segundo = media2

    print(f"Sua nota do primeiro semestre foi de {float(media):.2f}")
    print(f"Sua nota do segundo semestre foi de {float(media_segundo):.2f}")
    break








    











