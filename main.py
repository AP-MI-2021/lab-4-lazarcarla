def citire_lista():
    l=[]
    givenString=input("dati lista cu numerele separate printr-o virgula:")
    numbersAsString=givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l



def suma_max_min(l):
    '''
    determina suma dintre minimul si maximul listei
    :param l: lista cu numere intregi
    :return: suma dintre minumul si maximul listei
    '''
    max=0
    min=l[0]
    s=0
    for x in l:
        if x>max:
            max=x
    for x in l:
        if x<min:
            min=x

    s=max+min
    return s

def test_suma_max_min():
    assert suma_max_min([10, -3, 25, -1, 3, 25, 18])==22

def suma_cifrelor(x):
    s=0
    while x:
        s=s+x%10
        x=x//10
    return s

def numere_sum_cif_mai_mare_sau_egala_cu_n(l,n):
    '''
    determina numerele din lista care au suma cifrelor mai mare sau egala cu un numar citit de la tastatura
    :param l: lista de numere intregi
    :param n: numarul cu care comparam suma cifrelor numerelor
    :return: numerele care au suma cifrelor mai mare sau egala cu numarul citit
    '''
    rez=[]
    for x in l:
        if suma_cifrelor(x)>=n:
            rez.append(x)
    return rez

def test_numere_sum_cif_mai_mare_sau_egala_cu_n():
    assert numere_sum_cif_mai_mare_sau_egala_cu_n([25, 11, 10, 24, 39],7)==[25, 39]






def main():
    #test_concatenare_nr_pozitive()
    test_suma_max_min()
    test_numere_sum_cif_mai_mare_sau_egala_cu_n()
    l = []
    print("1.citire lista")
    print("2.Afișarea numărului obținut prin concatenarea tuturor numerelor pozitive din listă.")
    print("3.Suma dintre cel mai mare număr din listă și cel mai mic număr din listă.")
    print("4.Afișarea tuturor numerelor care au suma cifrelor mai mare sau egală decat un număr n citit de la tastatură.")
    print("5.Afișarea listei obținute din lista inițială în care numerele pătrat perfect sunt înlocuite cu radicalul acestora.")
    print("6.Iesire")
    while True:

        optiune = input("dati optiune:")
        if optiune == "1":
            l = citire_lista()
        #elif optiune == "2":
            #print(concatenare_nr_pozitive(l))
        elif optiune == "3":

            print(suma_max_min(l))

        elif optiune == "4":
            n=int(input("dati numarul natural n:"))
            print(numere_sum_cif_mai_mare_sau_egala_cu_n(l,n))
        #elif optiune == "5":
            #print((l))
        elif optiune == "6":
            break
        else:
            print("optiune gresita! reincercati!")


main()