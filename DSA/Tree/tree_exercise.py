class TreeNode:    
    def __init__(self,name):
        self.name = name
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

    def print_tree_level(self,level):
        if self.get_level() <= level:
            spaces = " " * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.name)
            if len(self.children) > 0:
                for child in self.children:
                    child.print_tree_level(level)
        else:
            return

def build_product_tree():
    root = TreeNode("Global")

    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root

if __name__ == '__main__':
    root = build_product_tree()
    # print(root.get_level())
    # root.print_tree('name')
    # root.print_tree('designation')
    # root.print_tree('both')
    root.print_tree_level(1)

  
