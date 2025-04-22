class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(root, value):
            if root is None:
                return Node(value)
            if value < root.value:
                root.left = _insert(root.left, value)
            else:
                root.right = _insert(root.right, value)
            return root
        self.root = _insert(self.root, value)

    def remove(self, value):
        def _minValueNode(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _remove(root, value):
            if root is None:
                return None
            if value < root.value:
                root.left = _remove(root.left, value)
            elif value > root.value:
                root.right = _remove(root.right, value)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                temp = _minValueNode(root.right)
                root.value = temp.value
                root.right = _remove(root.right, temp.value)
            return root
        self.root = _remove(self.root, value)

    def inorder(self):
        return self._traverse(self.root, "in")

    def preorder(self):
        return self._traverse(self.root, "pre")

    def postorder(self):
        return self._traverse(self.root, "post")

    def _traverse(self, node, order):
        result = []
        if node:
            if order == "pre":
                result.append(node.value)
            result += self._traverse(node.left, order)
            if order == "in":
                result.append(node.value)
            result += self._traverse(node.right, order)
            if order == "post":
                result.append(node.value)
        return result

    def height(self):
        def _height(node):
            if node is None:
                return -1
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def nodeDegree(self, value):
        node = self._find(self.root, value)
        if not node:
            return None
        degree = 0
        if node.left:
            degree += 1
        if node.right:
            degree += 1
        return degree

    def search(self, value):
        return self._find(self.root, value) is not None

    def _find(self, node, value):
        if not node:
            return None
        if node.value == value:
            return node
        elif value < node.value:
            return self._find(node.left, value)
        else:
            return self._find(node.right, value)

    def isStrictlyBinary(self):
        def _strict(node):
            if not node:
                return True
            if (node.left is None and node.right is None):
                return True
            if node.left and node.right:
                return _strict(node.left) and _strict(node.right)
            return False
        return _strict(self.root)

    def isFull(self):
        def _full(node):
            if not node:
                return True
            if (node.left is None) != (node.right is None):
                return False
            return _full(node.left) and _full(node.right)
        return _full(self.root)

    def isComplete(self):
        if not self.root:
            return True
        queue = [(self.root, 0)]
        i = 0
        while i < len(queue):
            node, index = queue[i]
            i += 1
            if node.left:
                queue.append((node.left, 2 * index + 1))
            if node.right:
                queue.append((node.right, 2 * index + 2))
        return queue[-1][1] == len(queue) - 1

def main():
    tree = BinaryTree()
    while True:
        print("===============================================")
        print("ESCOLHA UMA OPÇÃO:")
        print("1. Inserir elemento")
        print("2. Remover elemento")
        print("3. Buscar elemento")
        print("4. Imprimir em ordem")
        print("5. Imprimir em pré-ordem")
        print("6. Imprimir em pós-ordem")
        print("7. Verificar se a árvore é estritamente binária")
        print("8. Verificar se a árvore é cheia")
        print("9. Verificar se a árvore é completa")
        print("10. Mostrar altura da árvore")
        print("11. Mostrar grau de um nó")
        print("0. Sair")
        print("===============================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = int(input("Digite o valor a inserir: "))
            tree.insert(valor)
        elif opcao == "2":
            valor = int(input("Digite o valor a remover: "))
            tree.remove(valor)
        elif opcao == "3":
            valor = int(input("Digite o valor a buscar: "))
            print("Encontrado!" if tree.search(valor) else "Não encontrado.")
        elif opcao == "4":
            print("In-order:", tree.inorder())
        elif opcao == "5":
            print("Pré-ordem:", tree.preorder())
        elif opcao == "6":
            print("Pós-ordem:", tree.postorder())
        elif opcao == "7":
            print("Estritamente binária?" , "Sim" if tree.isStrictlyBinary() else "Não")
        elif opcao == "8":
            print("Árvore cheia?" , "Sim" if tree.isFull() else "Não")
        elif opcao == "9":
            print("Árvore completa?" , "Sim" if tree.isComplete() else "Não")
        elif opcao == "10":
            print("Altura da árvore:", tree.height())
        elif opcao == "11":
            valor = int(input("Digite o valor do nó: "))
            grau = tree.nodeDegree(valor)
            if grau is not None:
                print(f"Grau do nó {valor}: {grau}")
            else:
                print("Nó não encontrado.")
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
