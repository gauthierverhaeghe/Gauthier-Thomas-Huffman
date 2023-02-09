from collections import Counter
import heapq

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
liste = mettre_ordre_croissant(dico)

class BT:

    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.encoding = ''
        self.left = None
        self.right = None

    def __lt__(self, other) -> bool:
        return self.freq < other.freq

    def __repr__(self) -> str:
        return f'([{self.freq} - {self.char}], {repr(self.left)}, {repr(self.right)})'

def créer_arbre(liste):
    arbre = BT
    racine = liste[0][1]/liste





