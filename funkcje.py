task = "2" #input('wprowadz numer zadania: ')

if task == "1":
    krok = input('wprowadz krok (int):')
    try:
        krok = int(krok)

        for i in range(0 , 301, krok):
            if i>69 and i<151:
                print(i, '!')
            else:
                print(i)

        lista = range(100, 251, krok)
        ilosc_liczb = len(lista)
        suma_liczb = sum(lista)
        print("dlugosc =", ilosc_liczb, "; suma =", suma_liczb)

    except ValueError as e:
        print('twoj krok nie jest integerem!!!')

elif task == "2":
    while True:
        opcje = input('Wpisz "zakoncz" lub kliknij enter by kontynuowac:')
        if opcje == 'zakoncz':
            exit()

        else:
            dowolna_liczba = input('wprowadz dowolna liczbe:')
            try:
                dowolna_liczba = float(dowolna_liczba)
                if dowolna_liczba == 0 and dowolna_liczba == 13:
                    print('twoja liczba to 0 lub 13 i powoduje blad')
                
                else:
                    solution1 = 72/dowolna_liczba
                    solution2 = (7 * dowolna_liczba ** 4 - 5 * dowolna_liczba ** 2)/(dowolna_liczba - 13)
                    print('wynik z rownania pierwszego =', solution1, '; wynik z wyrazenia drugiego =', solution2)

            except ValueError as e:
                print('To nie jest liczba!!!')
