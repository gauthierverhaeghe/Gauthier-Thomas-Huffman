import heapq

class BinaryTree:
    '''binary tree for huffman codes'''

    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.encoding = ''
        self.gauche = None
        self.droit = None

    def __lt__(self, other) -> bool:
        return self.freq < other.freq

    def __repr__(self) -> str:
        return f'([{self.freq} - {self.char}], {repr(self.gauche)}, {repr(self.droit)})'

def construire_dictionnaire(texte):
    '''construire un dictionnaire des caractères et de leur fréquence dans le texte'''
    dictionnaire = {}
    # Parcourir tous les caractères du texte et compter leur fréquence
    for char in texte:
        if char in dictionnaire:
            dictionnaire[char] += 1
        else:
            dictionnaire[char] = 1
    # Ajouter les caractères qui ne sont pas dans le texte avec une fréquence de 0
    for char in set(texte):
        if char not in dictionnaire:
            dictionnaire[char] = 0
    return dictionnaire



def construire_arbre(dictionnaire):
    '''construire un arbre de Huffman à partir d'un dictionnaire de fréquences'''
    file_de_priorite = []
    # Créer un objet BinaryTree pour chaque caractère du dictionnaire et ajouter le tout à une file de priorité
    for char, freq in dictionnaire.items():
        noeud = BinaryTree(char, freq)
        heapq.heappush(file_de_priorite, noeud)
    # Combiner les deux noeuds les plus petits jusqu'à obtenir un seul arbre
    while len(file_de_priorite) > 1:
        gauche = heapq.heappop(file_de_priorite)
        droite = heapq.heappop(file_de_priorite)
        somme = gauche.freq + droite.freq
        parent = BinaryTree(None, somme)
        parent.gauche = gauche
        parent.droit = droite
        heapq.heappush(file_de_priorite, parent)
    return file_de_priorite[0]


def build_encoding_table(arbre):
    '''construire un dictionnaire des caractères et de leur encodage Huffman à partir d'un arbre de Huffman'''
    table_encodage = {}
    pile = [(arbre, '')]
    #On dépile un noeud et son encodage de la pile tant qu'il y a des nœuds dans la pile
    while pile:
        noeud, encodage = pile.pop()
        #Si le noeud est une feuille (c'est-à-dire qu'il correspond à un caractère), on ajoute l'encodage correspondant au dictionnaire des encodages
        if noeud.char is not None:
            table_encodage[noeud.char] = encodage

        #Si le noeud a un fils gauche, on empile le fils gauche avec son propre encodage (qui est l'encodage actuel + 0)
        #Si le noeud a un fils droit, on empile le fils droit avec son propre encodage (qui est l'encodage actuel + 1)

        if noeud.gauche is not None:
            pile.append((noeud.gauche, encodage + '0'))
        if noeud.droit is not None:
            pile.append((noeud.droit, encodage + '1'))

    return table_encodage


def encode(texte, table_encodage):
    '''encoder un texte en utilisant une table d'encodage de Huffman'''
    texte_encodé = ''
    for char in texte:
        texte_encodé += table_encodage[char]
    return texte_encodé

def decode(texte, arbre):
    # Vérifie que l'arbre est bien un objet BinaryTree
    if not isinstance(arbre, BinaryTree):
        raise TypeError("L'arbre doit être un objet BinaryTree")
    
    # Initialisation
    noeud = arbre
    texte_decode = ""

    # Boucle de décodage
    for bit in texte:
        # Vérifier que le noeud est bien un objet BinaryTree
        if not isinstance(noeud, BinaryTree):
            raise TypeError("Le noeud doit être un objet BinaryTree")
        
        if bit == "0":
            noeud = noeud.gauche  # descendre à gauche
        else:
            noeud = noeud.droit  # descendre à droite

        # Si le noeud est une feuille, ajouter le caractère correspondant au texte décodé
        if isinstance(noeud.char, str):
            texte_decode += noeud.char
            noeud = arbre  # revenir à la racine

    return texte_decode



# Test de la fonction construire_dictionnaire
texte = 'Hello World!'
dictionnaire = construire_dictionnaire(texte)
print(dictionnaire)  # devrait renvoyer {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

# Test de la fonction construire_arbre
arbre = construire_arbre(dictionnaire)
print(arbre)  # devrait renvoyer l'arbre binaire de Huffman correspondant au dictionnaire

# Test de la fonction build_encoding_table
table_encodage = build_encoding_table(arbre)
print(table_encodage)  # devrait renvoyer le dictionnaire des encodages de Huffman pour chaque caractère

# Test de la fonction encode
texte_encode = encode(texte, table_encodage)
print(texte_encode)  # devrait renvoyer le texte '01001110011000010110111001100100011000010111001001100001'

# Test de la fonction decode
texte_decode = decode(texte_encode, arbre)
print(texte_decode)  # devrait renvoyer le texte 'abracadabra'
