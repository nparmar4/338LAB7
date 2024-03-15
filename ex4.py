import random
import time
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
            node = self._balance_node(node, key)  # Rebalance the tree after insertion
        else:
            node.right = self._insert(node.right, key)
            node = self._balance_node(node, key)  # Rebalance the tree after insertion
        return node

    def _balance_node(self, node, key):
        balance = self._get_balance(node)

        # Case 3a: adding a node to an outside subtree
        if balance > 1 and key < node.left.key:
            print("Case #3a: adding a node to an outside subtree")
            return self._right_rotate(node)
        # Case 3b: adding a node to an inside subtree
        if balance < -1 and key > node.right.key:
            print("Case #3b: adding a node to an inside subtree")
            return self._left_rotate(node)
        return node

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._height(node.right) - self._height(node.left)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        return y

    def _lr_rotate(self, z):
        z.left = self._left_rotate(z.left)
        return self._right_rotate(z)

    def _rl_rotate(self, z):
        z.right = self._right_rotate(z.right)
        return self._left_rotate(z)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def measure_balance(self):
        return self._measure_balance(self.root)

    def _measure_balance(self, node):
        if node is None:
            return {}

        left_height = self._height(node.left)
        right_height = self._height(node.right)
        balance = abs(left_height - right_height)

        return {
            node.key: balance,
            **self._measure_balance(node.left),
            **self._measure_balance(node.right)
        }


def generate_random_tasks():
    tasks = []
    integers = list(range(1, 1001))

    for _ in range(1000):
        random.shuffle(integers)
        tasks.append(integers.copy())

    return tasks

def evaluate_tasks(tree, tasks):
    avg_performance = []
    largest_balance = []

    for task in tasks:
        start_time = time.time()
        for integer in task:
            tree.search(integer)
        end_time = time.time()
        avg_performance.append((end_time - start_time) / len(task))

        balance = tree.measure_balance()
        if balance:
            largest_balance.append(max(balance.values()))
        else:
            largest_balance.append(0)

    return avg_performance, largest_balance

def plot_scatter(avg_performance, largest_balance):
    plt.scatter(largest_balance, avg_performance, alpha=0.5)
    plt.title('Scatterplot of Balance vs Search Time')
    plt.xlabel('Absolute Balance')
    plt.ylabel('Search Time')

    # Set the limits of the x-axis to be more spread out with a higher multiplier
    plt.xlim(0, max(largest_balance) * 1.5)  # Adjust the multiplier as needed

    plt.show()

if __name__ == "__main__":
    tasks = generate_random_tasks()
    tree = BST()

    avg_performance, largest_balance = evaluate_tasks(tree, tasks)
    plot_scatter(avg_performance, largest_balance)
    
    # Test cases
    tree = BST()
    print("Test Case 1 - Case 3a:")
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(10)
    tree.insert(25)
    tree.insert(50)

    print("\nTest Case 2 - Case 3b:")
    tree = BST()
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(35)
    tree.insert(45)
    tree.insert(42)
