class Treenode:    
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level   

    def print_tree(self):
        spaces = " " * self.get_level() * 2
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = Treenode('Electronics')

    laptop = Treenode('Laptop')
    laptop.add_child(Treenode('Mac'))
    laptop.add_child(Treenode('Surface'))
    laptop.add_child(Treenode('Thinkpad'))

    mobile = Treenode('Mobile')
    mobile.add_child(Treenode('iPhone'))
    mobile.add_child(Treenode('Samsung'))
    mobile.add_child(Treenode('Pixel'))

    tv = Treenode('Tv')
    tv.add_child(Treenode('Samsung'))
    tv.add_child(Treenode('LG'))

    root.add_child(laptop)
    root.add_child(tv)
    root.add_child(mobile)

    return root

if __name__ == '__main__':
    root = build_product_tree()
    # print(root.get_level())
    root.print_tree()
  
