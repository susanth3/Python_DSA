class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def get_length(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next
        return count

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        
        temp = self.head
        llstring = ''
        while temp:
            llstring += str(temp.data) + " --> "
            temp = temp.next

        print(llstring)

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data,None)

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
                node = Node(data,temp.next)
                temp.next = node
                break

            temp = temp.next
            count += 1 

    def remove_at(self,index,data):
        if index == 0:
            self.head = self.head.next
            return

        if index < 0 or index > self.get_length():
            raise Exception ("Invalid Input")
        
        count = 0
        temp = self.head

        while temp:
            if count == index - 1:
                temp.next = temp.next.next
                break

            temp = temp.next
            count += 1    

    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        temp = self.head
        while temp:
            if temp.data == data_after:
                temp.next = Node(data_to_insert,temp.next)
                break
            temp = temp.next 

    def remove_by_value(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next:
            if temp.next == data:
                temp.next = temp.next.next
                break
            temp = temp.next     


if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple")
    ll.print()
    ll.remove_by_value("orange")
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()


