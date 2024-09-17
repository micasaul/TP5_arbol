from FArbol.TP5.Cola import Queue

class BinaryTree:

    class __Node:
        def __init__(self, value, left=None, right=None, other_value=None):
            self.value = value
            self.left = left
            self.right = right
            self.other_value = other_value
            self.height = 0

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        """Actualiza la altura"""
        if root is not None:
            # print(f'actualizar altura de {root.value}')
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = max(left_height, right_height) + 1
            # print(f'altura izq {left_height} altura der {right_height}')
            # print(f'altura de {root.value} es {root.height}')

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        """Balancea el arbol"""
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                # print('desbalanceado a la izquierda')
                if self.height(root.left.left) >= self.height(root.left.right):
                    # print('rotar simple derecha')
                    root = self.simple_rotation(root, True)
                else:
                    # print('rotar doble derecha')
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                # print('desbalanceado a la derecha')
                if self.height(root.right.right) >= self.height(root.right.left):
                    # print('rotar simple izquierda')
                    root = self.simple_rotation(root, False)
                else:
                    # print('rotar doble izquierda')
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_value=None):
        """Agrega un nodo"""
        def __insert(root, value, other_value=None):
            if root is None:
                return BinaryTree.__Node(value, other_value=other_value)
            elif value < root.value:
                root.left = __insert(root.left, value, other_value)
            else:
                root.right = __insert(root.right, value, other_value)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insert(self.root, value, other_value)

    def search(self, key):
        """Busca un nodo con su valor"""
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    # print('lo encontre')
                    return root
                elif key < root.value:
                    # print(f'buscalo a la izquierda de {root.value}')
                    return __search(root.left, key)
                else:
                    # print(f'buscalo a la derecha de {root.value}')
                    return __search(root.right, key)
            # else:
            #     print('no hay nada')
        aux = None
        if self.root is not None:
            aux = __search(self.root, key)
        return aux

    def search_coincidente(self, key):
        """Busca un nodo con valor coincidente"""
        def __search_coincidente(root, key):
            if root is not None:
                __search_coincidente(root.left, key)
                if root.value.startswith(key):
                    print(root.value)
                __search_coincidente(root.right, key)

        __search_coincidente(self.root, key)

    def preorden(self):
        """Pasa por la raiz y recorre de izquierda a derecha"""
        def __preorden(root):
            if root is not None:
                print(root.value)
                # print(f'izquierda de {root.value}')
                __preorden(root.left)
                # print(f'derecha de {root.value}')
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)

    def inorden(self):
        """Recorre de izquierda a derecha pasando por la raiz"""
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        if self.root is not None:
            __inorden(self.root)

    def inorden_values(self):
        """Recorre inorden con other_value"""
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(f"{root.value}, derrotado por: {root.other_value}")
                __inorden(root.right)

        if self.root is not None:
            __inorden(self.root)

    def mas_derrotas(self):
        """Cuenta dios con mas derrotas"""
        dic = {}
        def __derrotas(root):
            if root is not None:
                __derrotas(root.left)
                if root.other_value is not None:
                    if root.other_value not in dic:
                        dic.update({root.other_value: 1})
                    else:
                        dic[root.other_value] += 1
                __derrotas(root.right)
            return dic

        if self.root is not None:
            __derrotas(self.root)
        return dic

    def postorden(self):
        """Recorre de derecha a izquierda pasando por la raiz"""
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        if self.root is not None:
            __postorden(self.root)

    def inorden_no(self):
        """Recorre inorden con condicion"""
        def __inorden_no(root):
            if root is not None:
                __inorden_no(root.left)
                if root.other_value is None:
                    print(root.value)
                __inorden_no(root.right)

        if self.root is not None:
            __inorden_no(self.root)

    def inorden_capturadas(self):
        """Recorre inorden con condicion"""
        def __inorden_heracles(root):
            if root is not None:
                __inorden_heracles(root.left)
                if root.capturada is "Heracles":
                    print(root.value)
                __inorden_heracles(root.right)

        if self.root is not None:
            __inorden_heracles(self.root)

    def inorden_heracles(self):
        """Recorre inorden con condicion"""
        def __inorden_heracles(root):
            if root is not None:
                __inorden_heracles(root.left)
                if root.other_value is "Heracles":
                    print(root.value)
                __inorden_heracles(root.right)

        if self.root is not None:
            __inorden_heracles(self.root)

    def inorden_villanos(self):
        """Recorre inorden con condicion"""
        def __inorden_villanos(root):
            if root is not None:
                __inorden_villanos(root.left)
                if root.other_value is not True:
                    print(root.value)
                __inorden_villanos(root.right)

        if self.root is not None:
            __inorden_villanos(self.root)

    def inorden_superheroes(self):
        """Recorre inorden con condicion"""
        def __inorden_superheroes(root):
            if root is not None:
                __inorden_superheroes(root.left)
                if root.other_value is True:
                    print(root.value)
                __inorden_superheroes(root.right)

        if self.root is not None:
            __inorden_superheroes(self.root)

    def inorden_superheros_start_with(self, start):
        """Recorre inorden con condicion de nombre"""
        def __inorden_superheros_start_with(root, start):
            if root is not None:
                __inorden_superheros_start_with(root.left, start)
                if root.other_value is True and root.value.startswith(start):
                    print(root.value)
                __inorden_superheros_start_with(root.right, start)

        if self.root is not None:
            __inorden_superheros_start_with(self.root, start)

    def contar_super_heroes(self):
        """Contador con condicion"""
        def __contar_super_heroes(root):
            counter = 0
            if root is not None:
                if root.other_value is True:
                    counter = 1
                counter += __contar_super_heroes(root.left)
                counter += __contar_super_heroes(root.right)
            return counter

        return __contar_super_heroes(self.root)
    
    def contar(self):
        """Contador"""
        def __contar(root):
            counter = 0
            if root is not None:                
                counter = 1
                counter += __contar(root.left)
                counter += __contar(root.right)
            return counter

        return __contar(self.root)

    def dividir(self, arbol1, arbol2):
        """Divide en 2"""
        def __dividir(root, arbol1, arbol2):
            if root is not None:
                __dividir(root.left, arbol1, arbol2)
                if root.other_value is True:
                    arbol1.insert_node(root.value, root.other_value)
                else: 
                    arbol2.insert_node(root.value, root.other_value)
                __dividir(root.right, arbol1, arbol2)

        if self.root is not None:
            __dividir(self.root, arbol1, arbol2)
    
    def hijo_der (self, nodo):
        """Devuelve el hijo derecho de un nodo"""
        def __search (root, nodo):
            if root is not None:
                if root.value == nodo:
                        # print("lo encontre")
                    root = root.right
                    print(f"el hijo derecho es {root.value}")
                elif nodo<root.value:
                        # print("izq")
                    return __search(root.left, nodo)
                else:
                        # print("der")
                    return __search(root.right, nodo)
        if self.root is not None:
            __search(self.root, nodo)

    def hijo_izq (self, nodo):
        """Devuelve el hijo izquierdo de un nodo"""
        def __search (root, nodo):
            if root is not None:
                if root.value == nodo:
                        # print("lo encontre")
                    root = root.left
                    print(f"el hijo izquierdo es {root.value}")
                elif nodo<root.value:
                        # print("izq")
                    return __search(root.left, nodo)
                else:
                        # print("der")
                    return __search(root.right, nodo)
        if self.root is not None:
            __search(self.root, nodo)   
    
    def by_level(self):
        """Recorre preorden mostrando nivel"""
        pendientes = Queue()
        if self.root is not None:
            pendientes.arrive(self.root)

        while pendientes.size() > 0:
            node = pendientes.attention()
            print(f"nivel {node.height}", node.value)
            if node.left is not None:
                pendientes.arrive(node.left)
            if node.right is not None:
                pendientes.arrive(node.right)

    def delete_node(self, value):
        """Elimina un nodo y lo reemplaza por su hijo más chico"""
        def __replace(root):
            if root.right is None:
                # print(f'no tiene derecha es el mayor {root.value}')
                return root.left, root
            else:
                # print('seguir buscando nodo par remplaz+ar a la dercha')
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            value_delete = None
            if root is not None:
                if root.value > value:
                    # print(f'buscar  a la izquierda de {root.value}')
                    root.left, value_delete = __delete(root.left, value)
                elif root.value < value:
                    # print(f'buscar  a la derecha de {root.value}')
                    root.right, value_delete = __delete(root.right, value)
                else:
                    # print('valor encontrado')
                    value_delete = root.value
                    if root.left is None:
                        # print('a la izquierda no hay nada')
                        return root.right, value_delete
                    elif root.right is None:
                        # print('a la derecha  no hay nada')
                        return root.left, value_delete
                    else:
                        # print('tiene ambos hijos')
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        # return root, value_delete
                    root = self.balancing(root)
                    self.update_height(root)
            return root, value_delete

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, value)
        return delete_value

