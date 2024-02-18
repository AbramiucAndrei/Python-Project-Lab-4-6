from business import *
from domain import *
def test_prim():
    """
    test pentru functia de numar prim
    """
    assert prim(2)==1
    assert prim(1)==0
    assert prim(-100)==0
    assert prim(31)==1
    assert prim(11)==1
    assert prim(9)==0
def test_get_modul_patrat():
    """
    se testeaza daca se calculeaza corect modulul(^2)
    """
    assert get_modul_patrat(convertListDict([6,8]))==100
    assert get_modul_patrat(convertListDict([0,0]))==0
    assert get_modul_patrat(convertListDict([1,1]))==2
    assert get_modul_patrat(convertListDict([-1,1]))==2

def test_subtask_3_2():
    """
    se testeaza daca se identifica corect toate
    numerele din lista cu modulul < 10
    """
    assert subtask_3_2(convertEntireListToDict([[5,8],[10,10],[1,1],[0,0],[8,6]]))==convertEntireListToDict([[5,8],[1,1],[0,0]])
    
def test_subtask_3_3():
    """
    se testeaza daca se identifica corect toate
    numerele din lista cu modulul == 10
    """
    assert subtask_3_3(convertEntireListToDict([[5,8],[10,10],[1,1],[0,0],[8,6]]))==convertEntireListToDict([[8,6]])

def test_subtask_4_1():
    """
    se testeaza daca suma numerelor dintr-o secventa
    se realizeaza corect
    """
    lista=[[1,5],[2,4],[11,4],[-15,-20],[12,128]]
    lista=convertEntireListToDict(lista)
    assert calculeaza_suma(lista,1,3)==convertListDict([-2,-12])
    assert calculeaza_suma(lista,0,4)!=convertListDict([12,121])
def test_subtask_4_2():
    """
    se testeaza daca produsul numerelor dintr-o secventa
    se realizeaza corect
    """
    lista=[[2,4],[11,4],[-15,-20]]
    lista=convertEntireListToDict(lista)
    assert calculeaza_produs(lista,0,2)==convertListDict([950,-900])
    assert calculeaza_produs(lista,0,0)==convertListDict([2,4])

    lista=convertEntireListToDict([[1,5],[2,4],[11,4],[-15,-20],[12,128]])
    assert calculeaza_produs(lista,0,4)=={'real': -427400, 'imag': 743800}
def test_subtask_4_3():
    """
    se testeaza daca se sorteaza descrescator corect
    """
    lista=[[1,5],[2,4],[11,4],[-15,-20],[12,128]]
    lista=convertEntireListToDict(lista)
    assert subtask_4_3(lista)==convertEntireListToDict([[12,128],[1,5],[2,4],[11,4],[-15,-20]])
def test_subtask_5_1():
    """
    se testeaza daca se elimină din listă numerele complexe la care
    partea reala este prim.

    """
    lista=[[1,5],[2,4],[11,4],[12,128]]
    lista=convertEntireListToDict(lista)
    assert subtask_5_1(lista)==convertEntireListToDict([[1,5],[12,128]])
def test_subtask_5_2():
    """
    se testeaza daca se elimina corect din lista numerele complexe la care modulul
    este > decât un număr dat
    """
    lista=convertEntireListToDict([[5,8],[10,10],[1,1],[0,0],[8,6]])
    assert elimina_subtask_5_2(lista,10)==convertEntireListToDict([[5,8],[1,1],[0,0],[8,6]])

def test_undo_6():
    """
    test pentru functia undo
    """
    v=[]
    history=[]
    history.append(list(v))

    #cv=v[:]
    #history.append(list(v))
    v=[[15,1]]
    history.append(list(v))
    v.append([12,1])
    history.append(list(v))
    v.append([-1,1])
    history.append(list(v))

    v.pop()
    history.append(list(v))

    v=undo(history)#undo
    assert v==[[15,1],[12,1],[-1,1]]
    v=undo(history)
    assert v==[[15,1],[12,1]]
    v=undo(history)
    assert v==[[15,1]]
    v=undo(history)
    assert v==[]
    try:
        v=undo(history)
        assert False
    except ValueError:
        assert True



def teste():
    """
    se apeleaza pe rand toate testele
    pentru functii
    """
    test_get_modul_patrat()
    #test_subtask_1_1()  SI test_subtask_1_2() -->Sunt cu UI
    #test_subtask_3_1() - UI
    test_subtask_3_2()
    test_subtask_3_3()
    test_subtask_4_1()
    test_subtask_4_2()
    test_subtask_4_3()
    test_subtask_5_1()
    test_subtask_5_2()
    test_undo_6()#undo
    test_prim()
