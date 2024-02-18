from UI import *
from domain import *
def prim(numar):
    """
    reurneaza 1 daca numarul este prim
    si 0 daca nu este prim
    """
    if numar<2:
        return 0
    if numar%2==0:
        if numar==2:
            return 1
        else:
            return 0
    for d in range(2,numar//2+1):
        if numar%d==0:
            return 0
    return 1


def get_modul_patrat(numar):
    """
    returneaza modul la puterea a doua, a
    numarului transmis prin parametru
    pentru a nu se pierde din precizie atunci cand se aplica radicalul
    """
    a=get_real(numar)
    b=get_imaginar(numar)
    suma=a*a+b*b
    return suma

def subtask_1_1(lista):
    """
    • Adaugă număr complex la sfârșitul listei

    """
    nr_nou=citeste_complex()
    lista.append(nr_nou)
    
def subtask_1_2(lista):
    """
    Inserare numar complex citit de la
     tastatura pe o pozitie data
    """
    nr_nou=citeste_complex()
    pozitie=get_pozitie()
    lista.insert(pozitie,nr_nou)



def meniul_1(v,history):
    """
    meniul de interactiune pentru functionalitatea 1
    """

    while True:
        show_subcomenzi_1()
        subcomanda = -1
        while not (subcomanda >= 1 and subcomanda <= 3):
            subcomanda=get_subcomanda()
        if subcomanda==1:
            subtask_1_1(v)
        elif subcomanda==2:
            subtask_1_2(v)
        else:
            break
        history.append(list(v))

        print(v)

def batch_subtask_2_1(v,poz):
    """
    se sterge din lista v de pe pozitia poz elementul
    """
    if not (poz<len(v)):
        raise ValueError("pozitie incorecta")

    v.pop(poz)
def subtask_2_1(v):
    """
    sterge element de pe o pozitie data
    se citeste pozitia de la tastatura si se sterge elementul din lista
    de la pozitia data
    """
    poz = get_pozitie()
    while not (poz<len(v)):
        poz = get_pozitie()
    #assert poz<len(v)
    v.pop(poz)

def subtask_2_2(v):
    """
    sterge elementele de pe un interval de pozitii
    interval citit de la tastatura
    """

    st,dr=get_interval()

    while not (dr<len(v)):
        st, dr = get_interval()
    #assert dr<len(v)

    for i in range(dr-st+1):
        v.pop(st)

def subtask_2_3(v):
    """
    inlocuieste toate aparitiile unui numar complex cu alt
    numar complex
    1.citim numarul complex de inlocuit
    2.citim noul numar complex
    3.inlocuim toate aparitiile primului,cu al doilea
    """
    de_scos=citeste_complex()
    de_pus=citeste_complex()
    for i, el in enumerate(v):
        if el==de_scos:
            v[i]=de_pus




def meniul_2(v,history):
    """
    meniul de interactiune pentru functionalitatea 2
    """
    while True:
        show_subcomenzi_2()
        subcomanda=-1
        while not (subcomanda >=1 and subcomanda<=4):
            subcomanda=get_subcomanda()

        if subcomanda==1:
            subtask_2_1(v)
        elif subcomanda==2:
            subtask_2_2(v)
        elif subcomanda==3:
            subtask_2_3(v)
        else:
            break
        history.append(list(v))

        print(v)


def batch_subtask_3_1(lista,st,dr):
    """
    functia tipareste partea imaginara pentru numerele din lista,
    ce se afla intre pozitiile st si dr
    """

    if st>dr or dr>=len(lista) or st<0:
        raise ValueError

    imaginare = []
    for i in range(st, dr + 1):
        imaginare.append(get_imaginar(lista[i]))
    return imaginare

def subtask_3_1(lista):
    
    """
    se executa comanda 3,subcomanda 1
    functia tipareste partea imaginara pentru numerele din "lista"
    ,ce se afla intr-un anumit interval de pozitii
    """

    st, dr = get_interval()

    while not (dr<len(lista)):
        st, dr = get_interval()

    
    imaginare=[]
    for i in range (st,dr+1):
        imaginare.append(get_imaginar(lista[i]))
    return imaginare

def subtask_3_2(lista):
    """
    se executa comanda 3,subcomanda 2
    tipărește toate numerele complexe care au modulul mai mic decât 10
    """
    mai_mici_ca_10=[]
    for elem in lista:
        if(get_modul_patrat(elem)<100):
            mai_mici_ca_10.append(elem)
    return mai_mici_ca_10

def subtask_3_3(lista):
    """
    se executa comanda 3,subcomanda 3
    tipărește toate numerele complexe care au modulul egal cu 10
    """
    egale_cu_10=[]
    for elem in lista:
        if(get_modul_patrat(elem)==100):
            egale_cu_10.append(elem)
    return egale_cu_10



def meniul_3(v):
    """
    meniul de interactiune pentru functionalitatea 3
    """

    while True:
        show_subcomenzi_3()
        subcomanda=-1
        while not (subcomanda >= 1 and subcomanda <= 4):
            subcomanda = get_subcomanda()
        rez=[]
        if subcomanda==1:
            rez=subtask_3_1(v)
            print(rez)
        elif subcomanda==2:
            rez=subtask_3_2(v)
            if rez==[]:
                print("Nu exista")
            else:
                print(rez)
        elif subcomanda==3:
            rez=subtask_3_3(v)
            if rez==[]:
                print("Nu exista")
            else:
                print(rez)
        else:
            break

def calculeaza_suma(lista,st,dr):
    """
    se calculeaza suma numerelor complexe din lista,
    ce se afla intre pozitiile st si dr inclusiv
    se returneaza suma,tot sub forma de numar complex
    """
    assert dr<len(lista)
    suma=creeaza_complex(0,0)
    for el in lista[st:dr+1]:
        suma["real"]=suma["real"]+get_real(el)
        suma["imag"]=suma["imag"]+get_imaginar(el)
    return suma
def calculeaza_produs(lista,st,dr):
    """
    se calculeaza produsul numerelor complexe din lista,
    ce se afla intre pozitiile st si dr inclusiv
    se returneaza produsul,tot sub forma de nr complex
    """
    assert dr<len(lista)
    prod=lista[st]

    for el in lista[st+1:dr+1]:
        re1=get_real(prod)
        im1=get_imaginar(prod)
        re2=get_real(el)
        im2=get_imaginar(el)

        new_real= re1*re2-im1*im2
        new_imag= re1*im2+re2*im1
        prod=creeaza_complex(new_real,new_imag)
    return prod
def subtask_4_1(lista):
    """
    se citeste o secventa
    se realizeaza suma numerelor din acea secventa si se returneaza
    """
    st,dr= get_interval()
    rez=[]
    rez= calculeaza_suma(lista,st,dr)
    return rez
def subtask_4_2(lista):
    """
    se citeste o secventa
    se realizeaza produsul numerelor din acea secventa si se returnreaza
    """
    st,dr=get_interval()
    rez=[]
    rez=calculeaza_produs(lista,st,dr)
    return rez

def subtask_4_3(lst):
    """
    se sorteaza descrescator lista dupa partea imaginara,
     se face o copie e ei si se returneaza lista sortata
    """
    #sorted_list=sorted(lista,key=itemgetter(1), reverse=True)
    lista=lst.copy()
    finish=0
    n=len(lista)-1
    iter = 0
    while finish==0:

        finish=1
        for i in range(n-iter):
            if get_imaginar(lista[i])<get_imaginar(lista[i+1]):
                lista[i], lista[i+1]=lista[i+1],lista[i]
                finish=0
            elif get_imaginar(lista[i])==get_imaginar(lista[i+1]) and get_real(lista[i])>get_real(lista[i+1]):
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                finish = 0
        iter+=1


    return lista


def meniul_4(v):
    """
    meniul de interactiune pentru functionalitatea 4
    """
    while True:
        show_subcomenzi_4()
        subcomanda = -1
        while not (subcomanda >= 1 and subcomanda <= 4):
            subcomanda = get_subcomanda()

        if subcomanda==1:
            rez=subtask_4_1(v)
            print(rez)
        elif subcomanda==2:
            rez=subtask_4_2(v)
            print(rez)
        elif subcomanda==3:
            rez=subtask_4_3(v)
            print(rez)
        else:
            break


def elimina_subtask_5_2(lista,numar):
    """
    elimina din lista numerele complexe la care modulul
     este > decât un număr dat
    """
    dupa_eliminare=lista[:]
    for el in lista[:]:
        if get_modul_patrat(el) > numar*numar or numar<0:
            dupa_eliminare.remove(el)
    return dupa_eliminare
def subtask_5_1(lista):
    """
    elimina din lista numerele complexe la care partea reala este
    un nr prim
    """
    dupa_eliminare= lista.copy()
    for elem in lista[:] :
        reala=get_real(elem)
        if(prim(reala)==1):
            dupa_eliminare.remove(elem)
    return dupa_eliminare

def subtask_5_2(lista):
    """
     citeste un numar de
     la tastatura si elimina din lista numerele complexe la care modulul
     este > decât numărul dat
    """
    valoare_de_comparatie=get_numar()
    new_list=elimina_subtask_5_2(lista,valoare_de_comparatie)
    return new_list
            

def meniul_5(v):
    """
    meniul de interactiune pentru functionalitatea 5
    """
    while True:
        show_subcomenzi_5()

        subcomanda=-1
        while not (subcomanda>=1 and subcomanda<=3):
          subcomanda=get_subcomanda()


        rez=[]
        if subcomanda==1:
            rez=subtask_5_1(v)

        elif subcomanda==2:
            rez=subtask_5_2(v)

        else:
            break
       # history.append(list(v))
        #print(v)
        print(rez)



def undo(history):
    """
    se returneaza lista in forma ei
    de inainte de efectuarea ultimei operatii
    FUNCTIA UNDO-
    """
    #show_subcomenzi_6()
    if len(history)<=1:
        raise ValueError("Lista nu mai are variante anterioare")
    history.pop()
    return list(history[-1])

def run():
    v = []
    history = []
    history.append(list(v))

    afisare_moduri()
    mode=get_mode()
    if mode==1: #BATCH
        while True:
            line_command=input("ADD/STERGE/FILTRARE/UNDO/EXIT\nIntroduceti comenzile separate prin ';' ")
            line_command=line_command.split(';')
            for cmd in line_command[:]:
                instr, aux1=get_instruction(cmd)
                if instr=='add':
                    """
                    adauga la sfarsitul listei numarul "aux1"
                    """
                    v.append(creeaza_complex(aux1[0],aux1[1]))
                    history.append(list(v))
                    print(v)
                elif instr=='sterge':
                    #"se sterge numarul de pe pozitia aux1[0] din lista v"
                    try:
                        batch_subtask_2_1(v,aux1[0])
                        history.append(list(v))
                        print(v)
                    except ValueError as ve:
                        print(ve)
                elif instr=='filtrare':
                   # "tipareste partea imaginara pentru numerele din "lista"
                   # ",ce se afla intr-un anumit interval de pozitii"
                   rez=[]
                   try:
                        rez=batch_subtask_3_1(v,aux1[0],aux1[1])
                        print(rez)
                   except ValueError as ve:
                       print(ve)
                elif instr=='undo':
                    try:
                        v=undo(history)
                        print(v)
                    except ValueError as ve:
                        print(ve)

                elif instr=='exit':
                    exit(0)



    else:
        while True:
            """
            meniul principal de functionalitati
            """
            afiseaza_comenzi()
            comanda=get_comanda()
            while not (comanda>=1 and comanda<=7):
                comanda=get_comanda()

            if comanda==1:
                meniul_1(v,history)
            elif comanda==2:
                meniul_2(v,history)
            elif comanda==3:
                meniul_3(v)
            elif comanda==4:
                meniul_4(v)
            elif comanda==5:
                meniul_5(v)
            elif comanda==6:
                try:
                    v=undo(history)
                    print(v)
                except ValueError as ve:
                    print(ve)

            else:
                print("BYE!")
                break
