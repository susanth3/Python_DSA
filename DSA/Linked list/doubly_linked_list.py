class Node:
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Doublylinkedlist:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,data):
        if self.head is None:
            node = Node(data,self.head,None)
            self.head = node
        else:
            node = Node(data,self.head,None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data,None,None)
            self.head = node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = Node(data,None,temp)

    def get_length(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    def last_node(self):
        temp = self.head
        
        while temp.next:
            temp = temp.next
        return temp

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self,index,data):
            if index == 0:
                self.insert_at_begining(data)
            if index < 0 or index > self.get_length():
                raise Exception ("Invalid Input")
            
            count = 0
            temp = self.head

            while temp:
                if count == index - 1:
                    node = Node(data,temp.next,temp)
                    if temp.next:
                        temp.next.prev = node
                    temp.next = node
                    break

                temp = temp.next
                count += 1 

    def remove_at(self,index,data):
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        if index < 0 or index > self.get_length():
            raise Exception ("Invalid Input")
        
        count = 0
        temp = self.head

        while temp:
            if count == index:
                temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                break

            temp = temp.next
            count += 1   

    def print_forward(self):
            if self.head is None:
                print('Linked list is empty')
                return
            
            temp = self.head
            llstring = ''
            while temp:
                llstring += str(temp.data) + " --> "
                temp = temp.next

            print(llstring) 

    def print_backward(self):
            if self.head is None:
                print('Linked list is empty')
                return
            
            last_node = self.last_node()
            temp = last_node
            llstring = ''
            while temp:
                llstring += str(temp.data) + " --> "
                temp = temp.prev

            print(llstring) 


if __name__ == '__main__':
    ll = Doublylinkedlist()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()
        
