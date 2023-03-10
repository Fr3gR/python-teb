with open("dane.csv", encoding="UTF-8") as f:
    x = f.readlines()
    for k in x:
        t = k.split(",")
        plec = t[2]
        wiek = t[3]
        if wiek >= "65" and plec == "m" or wiek >= "60" and plec == "k":
            with open("dane2.csv", "a", encoding="UTF-8") as p:
                p.write(k)
                print(k)
