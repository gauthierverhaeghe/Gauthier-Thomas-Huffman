from collections import Counter
import heapq

'''
https://www.programiz.com/dsa/huffman-coding#:~:text=Huffman%20coding%20first%20creates%20a,concept%20of%20prefix%20code%20ie.
'''

def compter_lettre(texte:str)->dict:
    return Counter(texte)

def mettre_ordre_croissant(dictionnaire):
    queue = []
    heapq.heapify(queue)
    for clé, valeur in dictionnaire.items():
        heapq.heappush(queue, (valeur, clé))
    liste_triée = []
    while queue:
        suivant = heapq.heappop(queue)
        liste_triée.append((suivant[1], suivant[0]))
    return liste_triée


dico = compter_lettre('aaaaaaaaaaaaaaaaaahghghghghghghghghjhuijh')
print(dico)
print(type(dico))
liste = mettre_ordre_croissant(dico)
print(liste)


class BT:

    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.encoding = ''
        self.left = None
        self.right = None

    def ajouter_droit:
        pass
    def ajouter_gauche:
        pass
        
    def __lt__(self, other) -> bool:
        return self.freq < other.freq

    def __repr__(self) -> str:
        return f'([{self.freq} - {self.char}], {repr(self.left)}, {repr(self.right)})'


def liste_de_feuille(liste):
    new_liste = []
    for i in liste:
        new_liste.append((i,None ,None))
    return new_liste    

print(liste_de_feuille(liste))

def arbre_huffman(liste):


'''
def nouveau_noeud():
    pass

def noeud():
    pass


def Huffman(liste):
    liste = compter_lettre(liste)
    n = len(liste)
    Q = mettre_ordre_croissant(liste)
    for i in range(n):
        V = noeud(liste[i])
        Q.append(V)

    while len(Q) != 1:
        Z = nouveau_noeud()
        Z.left = x = Q.pop()
        Z.right = y = Q.pop()
        Z.frequency = x.frequency + y.frequency
        Q.append(Z)
    return Q
'''
