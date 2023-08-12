while True:
    dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL" : "komik bir şeye verilen cevap",
    "ROFL" : "bir şakaya karşılık cevap",
    "SHEESH" : "onaylamamak",
    "CREEPY" : "korkunç",
    "AGGRO" : "agresifleşmek/sinirlenmek"
    }

    a = input("kelime giriniz")

    if a in dict.keys():
        print(dict[a])
    
    else:
        print("bu burada yok")
    continue
