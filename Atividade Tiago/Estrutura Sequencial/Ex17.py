pintar=float(input('Digite quantos metros quadrados serão pintados: '))
cobertura=6
preco_lata=80
litros=pintar/cobertura
print("Litros: ",litros)
latas_necessarias=(litros+17.999)//18
preco_lata=latas_necessarias*preco_lata
galoes_necessarios=(litros+3.5999)//3.6
preco_galao=galoes_necessarios*25
print("Latas necessárias: ",latas_necessarias,"--- PREÇO: R$", preco_lata)
print("Galões necessários ",galoes_necessarios,"--- PREÇO: R$", preco_galao)
cont_lata=0
cont_galao=0
while litros>0:
    if litros<=10.8:
        cont_galao=(litros+3.59999)//3.6
        litros=0
    else:
        cont_lata+=1
        litros-=18
print("A melhor compra seria realizada com:",cont_lata,"latas e",cont_galao,"galões. Preço: R$",(cont_lata*80)+(cont_galao)*25)