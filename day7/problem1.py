from day7.treenode import TreeNode


def main():

    with open("input.txt", "r+") as file:
        content = [line.strip().strip('.').replace('bags', 'bag') for line in file.readlines()]

    tree_dict = {}
    root = TreeNode('root')

    for line in content:
        parent_name = line.split('contain')[0].strip()

        parent = get_node(parent_name, tree_dict)

        for child_name in line.split('contain')[1].split(','):
            child_name = child_name.strip()
            if child_name.strip != 'no other bag':
                child_name = child_name[2:]
            child = get_node(child_name, tree_dict)
            parent.add_child(child)

    for node in tree_dict.values():
        if node.is_root():
            root.add_child(node)

    parents = set()
    get_parents_for_node(root, 'shiny gold bag', parents)

    for parent in list(parents):
        get_parents_for_node(root, parent.data, parents)

    for parent in list(parents):
        get_parents_for_node(root, parent.data, parents)

    for parent in list(parents):
        get_parents_for_node(root, parent.data, parents)

    for parent in list(parents):
        get_parents_for_node(root, parent.data, parents)

    for parent in list(parents):
        get_parents_for_node(root, parent.data, parents)

    for parent in list(parents):
        get_parents_for_node(root, parent.data, parents)

    for parent in list(parents):
        get_parents_for_node(root, parent.data, parents)

    print(parents.__len__()-1)


def get_parents_for_node(root, node_name, parents):
    # if this is the node we're looking for, add all parents to set
    if root.data == node_name:
        for parent in root.parents:
            parents.add(parent)

    # else, continue search through tree
    else:
        for child in root.children:
            get_parents_for_node(child, node_name, parents)


def get_node(node_name, tree_dict):
    if node_name in tree_dict:
        node = tree_dict[node_name]
    else:
        node = TreeNode(node_name)
        tree_dict[node_name] = node
    return node


if __name__ == "__main__":
    main()
