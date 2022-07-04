class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data,None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception ("Invalid Input")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        temp = self.head

        while temp:
            if count == index - 1:
                temp.next = temp.next.next
                break

            temp = temp.next
            count += 1

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception ("Invalid Input")
        
        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        temp = self.head

        while temp:
            if count == index-1:
                node = Node(data,temp.next)
                temp.next = node
                break
            
            temp = temp.next
            count += 1          

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        temp = self.head

        while temp:
            if temp.data == data_after:
                node = Node(data_to_insert,temp.next)
                temp.next = node
                break

            temp = temp.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        temp = self.head

        while temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                break

            temp = temp.next

    def get_length(self):
        count = 0
        temp = self.head

        while temp :
            count += 1
            temp = temp.next
        
        return count

    def print(self):
        if self.head is None:
            print ("Linked list is empty")
            return

        temp = self.head
        llstring = ''

        while temp:
            llstring += str(temp.data) + ' --> '
            temp = temp.next

        print(llstring)


if __name__ == '__main__':
    ll = Linkedlist()
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(11)
    # ll.insert_at_end(89)
    ll.insert_values(['Banana','Cucumber','Carrot','Apple','Radish'])
    ll.print()
    ll.remove_at(2)
    ll.print()
    ll.insert_at(2,'Guava')
    ll.print()
    ll.insert_after_value('Guava','Papaya')
    ll.print()
    ll.remove_by_value("Radish")
    ll.print()


