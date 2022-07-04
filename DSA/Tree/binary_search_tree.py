class BinaryTree:
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            print ("Node already exist")
            return None
        
        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTree(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTree(data)

    def search(self,data):
        if data == self.data:
            return True
        
        elif data < self.data:
            if self.left :
                return self.left.search(data)
            else:
                return False

        else:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def preorder_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.preorder_traversal()
        if self.right:
            elements += self.right.preorder_traversal()

        return elements

    def postorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.postorder_traversal()
        if self.right:
            elements += self.right.postorder_traversal()

        elements.append(self.data)

        return elements

    def delete(self,val):
        if val < self.data:
            self.left = self.left.delete(val)
        
        elif val > self.data:
            self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None :
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

            # max_val = self.left.find_max()
            # self.data = max_val
            # self.left = self.left.delete(max_val)

        return self

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum    
            

def build_tree(elements):
    root = BinaryTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root


if __name__ == "__main__":
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(numbers)
    print("Input numbers:",numbers)
    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.inorder_traversal())
    print("Pre order traversal:", numbers_tree.preorder_traversal())
    print("Post order traversal:", numbers_tree.postorder_traversal())
    numbers_tree.delete(20)
    print("After deleting 20 ",numbers_tree.inorder_traversal())