
print("Tere! Olen sinu uus sõber - Python")
nimi = input("Mis on sinu nimi? ")
if nimi.isalpha() == True:
    print(f"{nimi} , sul on väga ilus nimi")
    try:
        index = int(input( f"{nimi}  ! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
        if index == 1:
            pikkus = float(input("mis on sinu pikkus?"))
            if pikkus >=100 and pikkus <=350 or mass >=20 and mass <=300:
               mass = float(input("mis on sinu mass?"))
               indeks = round((mass / (0.01*pikkus) ** 2),2)
               print (f"Sinu keha indeks on: {indeks} ")
               if indeks <= 16:
                   print("Tervisele ohtlik alakaal")
               elif indeks >=16 and indeks <=19:
                  print("Alakaal")
               elif indeks >=19 and indeks <=25:
                  print("Normaalkaal")
               elif indeks>=25 and indeks <=30:
                   print("Ülekaal")
               elif indeks>=30 and indeks <=35:
                  print("Rasvumine")
               elif indeks>=35 and indeks <=40:
                  print("Tugev rasvumine")
               elif indeks>=40:
                 print("Tervisele ohtlik rasvumine")
            else:
                print("vale pikkus")
        else:   
           print ("Kahju! See on väga kasulik info!")
           print()
    except:
        print("Viga!")
else:
    print("kirjutan õigi nimi!")