curso02 = int(input("Digite quantas avaliações o curso 2 teve: "))
curso01 = int(input("Digite quantas avaliações o curso 1 teve: "))
if curso01 == curso02:
    print("Empate nas avaliações.")
elif curso01 > curso02:
    print("O curso01 é maior.")
else:
    print("O curso02 é maior.")