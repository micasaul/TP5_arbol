# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:

from FArbol.TP5.Arbol import BinaryTree

tree = BinaryTree()

creatures = [
    {'criatura': "Ceto", 'derrotado por': None},
    {'criatura': "Tifón", 'derrotado por': "Zeus"},
    {'criatura': "Equidna", 'derrotado por': "Argos Panoptes"},
    {'criatura': "Dino", 'derrotado por': None},
    {'criatura': "Pefredo", 'derrotado por': None},
    {'criatura': "Enio", 'derrotado por': None},
    {'criatura': "Escila", 'derrotado por': None},
    {'criatura': "Caribdis", 'derrotado por': None},
    {'criatura': "Euriale", 'derrotado por': None},
    {'criatura': "Esteno", 'derrotado por': None},
    {'criatura': "Medusa", 'derrotado por': "Perseo"},
    {'criatura': "Ladon", 'derrotado por': "Heracles"},
    {'criatura': "Aguila de Caucaso", 'derrotado por': None},
    {'criatura': "Quimera", 'derrotado por': "Belerofonte"},
    {'criatura': "Hidra de Lerna", 'derrotado por': "Heracles"},
    {'criatura': "Leon de Nemea", 'derrotado por': "Heracles"},
    {'criatura': "Esfinge", 'derrotado por': "Edipo"},
    {'criatura': "Dragon de la Colquida", 'derrotado por': None},
    {'criatura': "Cerbero", 'derrotado por': None},
    {'criatura': "Cerda de Cromion", 'derrotado por': "Teseo"},
    {'criatura': "Ortro", 'derrotado por': "Heracles"},
    {'criatura': "Toro de Creta", 'derrotado por': "Teseo"},
    {'criatura': "Jabali de Calidon", 'derrotado por': "Atalanta"},
    {'criatura': "Carcinos", 'derrotado por': None},
    {'criatura': "Gerion", 'derrotado por': "Heracles"},
    {'criatura': "Cloto", 'derrotado por': None},
    {'criatura': "Laquesis", 'derrotado por': None},
    {'criatura': "Atropos", 'derrotado por': None},
    {'criatura': "Minotauro de Creta", 'derrotado por': "Teseo"},
    {'criatura': "Harpias", 'derrotado por': None},
    {'criatura': "Argos Panoptes", 'derrotado por': "Hermes"},
    {'criatura': "Aves del Estinfalo", 'derrotado por': None},
    {'criatura': "Talos", 'derrotado por': "Medea"},
    {'criatura': "Sirenas", 'derrotado por': None},
    {'criatura': "Piton", 'derrotado por': "Apolo"},
    {'criatura': "Cierva Cerinea", 'derrotado por': None},
    {'criatura': "Basilisco", 'derrotado por': None},
    {'criatura': "Jabali de Erimanto", 'derrotado por': None},
]

for i in creatures:
    tree.insert_node(i['criatura'], i['derrotado por'])

# a. listado inorden de las criatura y quienes la derrotaron;
print("Las criaturas y quienes las derrotaron son: ")
tree.inorden_values()
print()

# b. se debe permitir cargar una breve descripción sobre cada criatura;
def descripcion (tree, criatura, descripcion):
    pos= tree.search(criatura)
    pos.descripcion = descripcion
descripcion(tree, "Talos", "Autómata gigante hecho de bronce que protegía a la Creta minoica de piratas e invasores")

# c. mostrar toda la información de la criatura Talos;
pos= tree.search("Talos")
print(f"Nombre: {pos.value}, Derrotado por: {pos.other_value}, Descripcion: {pos.descripcion}")
print()

# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criatura;
dic = tree.mas_derrotas()
ordenado = sorted(dic.items(), key=lambda item: item[1], reverse=True)
print(f"Los 3 dioses que derrotaron la mayor cantidad de criaturas son: {ordenado[:3]}")
print()

# e. listar las criatura derrotadas por Heracles;
print("Las criaturas derrotadas por Heracles son: ")
tree.inorden_heracles()
print()

# f. listar las criatura que no han sido derrotadas;
print("Las criaturas que no han sido derrotadas son: ")
tree.inorden_no()
print()

# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
def capturada(tree, criatura, capturador=None):
    pos= tree.search(criatura)
    pos.capturada= capturador

for i in creatures:
    capturada(tree, i['criatura'])

# h. modifique los nodos de las criatura Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
criaturas=["Cerbero", "Toro de Creta", "Cierva Cerinea", "Jabali de Erimanto"]
for criatura in criaturas:
    capturada(tree, criatura, "Heracles")

# i. se debe permitir búsquedas por coincidencia;
print("Las busquedas coincidentes con M son: ")
tree.search_coincidente("M")
print()

# j. eliminar al Basilisco y a las Sirenas;
tree.delete_node("Basilisco")
tree.delete_node("Sirenas")

# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
descripcion(tree, "Aves del Estinfalo", "Heracles derroto a varias")

# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
pos= tree.search("Ladon")
pos.value = "Dragon Ladon"

# m. realizar un listado por nivel del árbol;
print("El listado del arbol por nivel es: ")
tree.by_level()
print()

# n. muestre las criatura capturadas por Heracles.
print("Las criaturas capturadas por Heracles son: ")
tree.inorden_capturadas()