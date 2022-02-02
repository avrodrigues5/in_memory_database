import sys


class Node:
    def __init__(self, key, val):
        self.left = None
        self.right = None
        self.key = key
        self.val = val


# FOR SET OPERATION
def set_operation(root, key, val):
    if root is None:
        return Node(key, val)
    else:
        if root.key == key:
            root.val = val
            return root
        elif root.key < key:
            root.right = set_operation(root.right, key, val)
        else:
            root.left = set_operation(root.left, key, val)
    return root


# FOR GET OPERATION
def get_operation(root, key):
    if root is None:
        return "NULL"
    if root.key == key:
        return root.val

    # Key is greater than root's key
    if root.key < key:
        return get_operation(root.right, key)
    else:
        return get_operation(root.left, key)
    return "NULL"


def min_value_node(node):
    current = node

    # loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current


def unset_operation(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = unset_operation(root.left, key)

    elif key > root.key:
        root.right = unset_operation(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)

        root.key = temp.key

        root.right = unset_operation(root.right, temp.key)

    return root


def in_order(root, val):
    no_of_values = 0
    if root:
        if root.val == val:
            no_of_values += 1
        no_of_values += in_order(root.left, val)
        no_of_values += in_order(root.right, val)
    return no_of_values


def clone_binary_tree(root):
    # base case
    if root is None:
        return None

    # create a new node with the same data as the root node
    root_copy = Node(root.key, root.val)

    # clone the left and right subtree
    root_copy.left = clone_binary_tree(root.left)
    root_copy.right = clone_binary_tree(root.right)

    # return cloned root node
    return root_copy


i = 0
r = None
active_tree = [{"tree": r, "val": 0}]
while True:
    try:
        command = input("INPUT:").strip().split(' ')
        if command[0] == "SET":
            if len(command) != 3:
                print("command should be in format of SET <VAR> <NUM>")
            else:
                if active_tree[-1]["val"] == 0:
                    active_tree[-1]["tree"] = Node(command[1], command[2])
                    active_tree[-1]["val"] += 1
                else:
                    active_tree[-1]["tree"] = set_operation(active_tree[-1]["tree"], command[1],
                                                                          command[2])
        elif command[0] == "GET":
            if len(command) != 2:
                print("command should be in format of GET <VAR>")
            else:
                print(get_operation(active_tree[-1]["tree"], command[1]))
        elif command[0] == "UNSET":
            if len(command) != 2:
                print("command should be in format of UNSET <VAR>")
            else:
                if active_tree[-1]["val"] != 0:
                    active_tree[-1]["tree"] = unset_operation(active_tree[-1]["tree"], command[1])
                    active_tree[-1]["val"] -= 1
                else:
                    print("No elements to be unset")
        elif command[0] == "NUMEQUALTO":
            if len(command) != 2:
                print("command should be in format of NUMEQUALTO <VAL>")
            else:
                print(in_order(active_tree[-1]["tree"], command[1]))
        elif command[0] == "END":
            active_tree = None
            sys.exit(0)
        elif command[0] == "BEGIN":
            active_tree.append({"tree": clone_binary_tree(active_tree[-1]["tree"]), "val": active_tree[-1]["val"]})
        elif command[0] == "ROLLBACK":
            if len(active_tree) > 1:
                active_tree.pop()
            else:
                print("NO TRANSACTION")
        elif command[0] == "COMMIT":
            active_tree = [active_tree[-1]]
        else:
            print('Sorry it has to be either SET, GET, UNSET, NUMEQUALTO, END')
    except ValueError:
        print("Sorry, my only purpose is to work with SET <VAR> <NUM>, GET <VAR>, UNSET <VAR>, NUMEQUALTO <VAL>, END. "
              "Also please ensure it's separate by space")

