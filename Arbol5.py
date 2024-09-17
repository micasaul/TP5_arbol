# Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), 
# desarrollar un algoritmo que contemple lo siguiente:

from FArbol.TP5.Arbol import BinaryTree

tree=BinaryTree()

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano 
# que indica si es un héroe o un villano, True y False respectivamente;
MCU = [
    {'nombre': "Black Widow", 'is_hero': True},
    {'nombre': "Thor", 'is_hero': True},
    {'nombre': "Iron Man", 'is_hero': True},
    {'nombre': "Captain America", 'is_hero': True},
    {'nombre': "Hulk", 'is_hero': True},
    {'nombre': "Hawkeye", 'is_hero': True},
    {'nombre': "Docor Strange", 'is_hero': True},
    {'nombre': "Thanos", 'is_hero': False},
    {'nombre': "Ultron", 'is_hero': False},
    {'nombre': "Dr Doom", 'is_hero': False},
    {'nombre': "Red Skull", 'is_hero': False},
]

for personaje in MCU:
    tree.insert_node(personaje['nombre'], personaje["is_hero"])

# b. listar los villanos ordenados alfabéticamente;
print("Los villanos son: ")
tree.inorden_villanos()
print()

# c. mostrar todos los superhéroes que empiezan con C;
print("Los superheroes que empiezan con C son: ")
tree.inorden_superheros_start_with("C")
print()

# d. determinar cuántos superhéroes hay el árbol;
super= tree.contar_super_heroes()
print(f"Hay {super} superheroes ")
print()

# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
pos= tree.search("Docor Strange")
pos.value = "Doctor Strange"

# f. listar los superhéroes ordenados de manera descendente;
print("Los superheroes son: ")
tree.inorden_superheroes()
print()

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
super = BinaryTree()
villano = BinaryTree()
tree.dividir(super, villano)

# I. determinar cuántos nodos tiene cada árbol;
nodos = tree.contar()
print(f"Hay {nodos} nodos")
print()

# II. realizar un barrido ordenado alfabéticamente de cada árbol.
print("Arbol de superheroes: ")
super.inorden()
print()
print("Arbol de villanos: ")
villano.inorden()