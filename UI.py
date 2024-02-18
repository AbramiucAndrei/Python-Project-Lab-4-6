from domain import creeaza_complex
def citeste_complex():
    """
    citeste partea reala si apoi imaginara ce corespund unui numar complex
    numar[0]=partea reala
    numar[1]=partea imaginara
    """
    print("Introduceti numarul complex:")
    numar=input()
    numar=numar.split()
    if(len(numar)!=2): return citeste_complex()

    try:
        numar[0]=int(numar[0])
        numar[1]=int(numar[1])
    except ValueError:
        print("Nu e numar")
        return citeste_complex()

    return creeaza_complex(numar[0],numar[1])

def get_comanda():
    """
    se citeste de la tastatura comanda dorita si se returneaza sub forma de intreg
    """
    c=input("Introduceti comanda:")
    try:
        c=int(c)
    except ValueError:
        print("Nu e numar")
        return get_comanda()

    return c

def get_subcomanda():
    """
    se citeste de la tastatura subcomanda dorita si se returneaza sub forma de intreg
    """
    sc=input("Introduceti subcomanda:")
    try:
        sc=int(sc)
    except ValueError:
        print("Nu e numar")
        return get_subcomanda()

    return sc

def get_numar():
    """
    citeste numar intreg de la tastatura
    """
    x=input("Introduceti un numar:")
    try:
        x=int(x)
    except ValueError:
        print("Nu e numar")
        return get_numar()

    return x

def get_pozitie():
    """
    Se citeste la tastatura pozitia la care se va efectua
    o inserare/stergere
    pozitia >=0
    """
    poz=input("Introduceti o pozitie:")
    if not poz.isnumeric():
        print("Nu e numar")
        return get_pozitie()
    else:
        poz=int(poz)
        assert poz>=0
        return poz


def get_interval():
    """
    se introduce de la tastatura intervalul de pozitii
    in care urmarim sa efectuam anumite operatii
    se vor returna doua pozitii
    prima reprezinta capatul stang al intervalului
    iar a doua reprezinta capatul drept
    """
    interval=input("Introduceti intervalul de pozitii:")
    interval=interval.split()
    try:
        interval[0]=int(interval[0])
        interval[1]=int(interval[1])
    except ValueError:
        print("Nu e numeric")
        return get_interval()

    st=interval[0]
    dr=interval[1]

    if not (st<=dr and st>=0):
        raise ValueError("Interval invalid")

    return st,dr

def get_mode():
    """
    se citeste de la tastatura 1 sau 2
    reprezentand modul ce se doreste a fi folosit
    """
    mode=-1
    while not (mode==1 or mode==2):
        mode=int(input("Introduceti modul de folosire a aplicatiei: "))
    return mode

def get_instruction(instr):
    """
    se citeste de la tastatura instructiunea
    si se returneaza , insotita de o lista de numere,ce are
    diferite interpretari: pozitie,numar,etc
    """
    instr=instr.strip()
    instr=instr.split()

    if instr[0].isalpha():
        try:
            for i in range(1,len(instr)):
                x=int(instr[i])
                instr[i]=x
        except ValueError:
            return 'NONE', []

        instr[0]=instr[0].lower()
        return instr[0], list(instr[1:])#!!!!!!!
    else:
        return 'NONE', []

def show_subcomenzi_1():
    """
    se afiseaza submeniul 1
    """
    print("1.Adaugă număr complex la sfârșitul listei\n")
    print("2.Inserare număr complex pe o poziție dată\n")
    print("3.Exit")

def show_subcomenzi_2():
    """
    se afiseaza subcomenzile pentru meniul 2
    """
    print("1.• Șterge element de pe o poziție dată\n")
    print("2.• Șterge elementele de pe un interval de poziții.\n")
    print("3.• Înlocuiește toate aparițiile unui număr complex cu un alt număr complex\n")
    print("4.Exit")

def show_subcomenzi_3():
    """
    afiseaza subcomenzile din meniul 3
    """
    print("1.Tipărește partea imaginara pentru numerele din listă. Se dă intervalul de poziții\n")
    print("2.Tipărește toate numerele complexe care au modulul mai mic decât 10\n")
    print("3.Tipărește toate numerele complexe care au modulul egal cu 10\n")
    print("4.Exit")


def show_subcomenzi_4():
    """
    se afiseaza submeniul pentru functionalitatea 4
    """
    print("1.Calculeaza suma numerelor dintr-o subsecventă dată (se da poziția de început și sfârșit).\n")
    print("2.Calculeaza produsul numerelor dintr-o subsecventă dată (se da poziția de început și sfârșit).\n")
    print("3.Tipărește lista sortată descrescător după partea imaginara\n")
    print("4.Exit")

def show_subcomenzi_5():
    """
    se afiseaza submeniul pentru comanda 5
    """
    print("1.Elimină din listă numerele complexe la care partea reala este prim\n")
    print("2.Elimina din lista numerele complexe la care modulul este > decât un număr dat\n")
    print("3.Exit")

def afiseaza_comenzi():
    """
    se afiseaza meniul principal de comenzi
    """
    print("1. Adaugă număr în listă\n")
    print("2. Modifică elemente din listă\n")
    print("3. Căutare numere\n")
    print("4. Operații cu numerele din listă\n")
    print("5. Filtrare\n")
    print("6. Undo\n")
    print("7.Exit")

def afisare_moduri():
    """
    se afiseaza cele doua moduri in care putem introduce
    instructiunile in program
    """
    print("1. Batch mode\n")
    print("2.Normal mode\n")
