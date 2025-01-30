pintar=float(input('Digite quantos metros quadrados serão pintados: '))
cobertura=3
preco_lata=80
litros=pintar/cobertura
latas_necessarias=(litros+17.999)//18
preco=latas_necessarias*preco_lata
print("Latas necessárias: ",latas_necessarias)
print("Valor total: R$",preco)
