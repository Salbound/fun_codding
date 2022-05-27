from datetime import date


def senha_Markem_Imaje():
    data_atual = date.today().strftime("%d%m%Y")
    senha = ""

    for i in data_atual:
        senha = senha + str((int(i) % 4) + 1)
    print(f"Senha Markem Imaje do dia: {senha}")
    



# ----------------------------------------------------------------------------------------

def main():
    senha_Markem_Imaje()

if __name__ == "__main__":
    main()