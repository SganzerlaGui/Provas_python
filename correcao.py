semestre = 1

while semestre <= 2:
    print(f"\n--- LEITURA DE NOTAS: {semestre}º SEMESTRE ---")
    
    cp1 = float(input("Digite a nota do Checkpoint 1: "))
    cp2 = float(input("Digite a nota do Checkpoint 2: "))
    cp3 = float(input("Digite a nota do Checkpoint 3: "))
    
    if cp1 <= cp2 and cp1 <= cp3:
        menor_cp = cp1
    elif cp2 <= cp1 and cp2 <= cp3:
        menor_cp = cp2
    else:
        menor_cp = cp3

    sp1 = float(input("Digite a nota da Sprint 1: "))
    sp2 = float(input("Digite a nota da Sprint 2: "))
    gs = float(input("Digite a nota da Global Solution: "))
    
    media = ((cp1 + cp2 + cp3 - menor_cp + sp1 + sp2) / 4) * 0.4 + (gs * 0.6)
    
    print(f"Média do {semestre}º Semestre: {media:.1f}")
    
    semestre += 1
