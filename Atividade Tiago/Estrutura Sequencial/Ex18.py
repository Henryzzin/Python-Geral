arquivo=float(input("Digite o tamanho do arquivo para ser baixado (MegaBytes): "))
velocidade=float(input("Digite a velocidade da internet (MegaBytes por segundo): "))
tempo=arquivo/velocidade/60
print("Demorará",tempo,"minutos para baixar.")
