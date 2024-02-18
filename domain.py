def get_real(numar):
    """
    returneaza partea reala a numarului complex "numar"
    """
    return numar["real"]

def get_imaginar(numar):
    """
    returneaza partea imaginara a numarului complex "numar"
    """
    return numar["imag"]

def creeaza_complex(reala,imaginara):
    """
    functia primeste prin intermediul celor 2 parametri
    partea reala si cea imaginara a unui numar complex(posibil strig-uri)
    si returneaza numarul complex,reprezentat printr-un dictionar
    """
    nr_complex={
        "real": int(reala),
        "imag": int(imaginara)
    }
    return nr_complex

def convertListDict(numar):
    """
    functia primeste prin intermediul parametrului un numar complex,
    reprezentat printr-o lista cu doar 2 elemente
    si returneaza acelasi numar complex,reprezentat cu ajutorul unui dictionar
    cu 2 key-uri: partea reala si partea imaginara
    """
    return {"real": numar[0], "imag": numar[1]}

def convertEntireListToDict(lista):
    """
    functia primeste prin intermediul parametrului o lista ce contine
    un anumit numar de liste cu doar 2 elemente, fiind reprezentarea unui numar complex
    functia returneaza o lista ce contine toate numerele complexe primite in lista
    initiala,dar sunt memorate sub forma de dictionare, tot cu cate 2 elemente: partea reala si cea imaginara
    """
    new_list=[]
    for el in lista:
        new_el=convertListDict(el)
        new_list.append(new_el)
    return new_list
