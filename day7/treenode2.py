class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parents = set()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def is_root(self):
        return self.parents.__len__() == 0

    def is_leaf(self):
        return self.children == []

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parents else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parents.add(self)
        self.children.append(child)
