class hashtable:
    def __init__(self):
        self.limit = 10
        self.arr = [None for i in range(self.limit)]
    
    def get_hash(self,key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.limit
    
    def probe_range(self,index):
        return [*range(index, len(self.arr)) + [*range(0,index)]]

    def probe_slot(self,key,index):
        pro_range = self.probe_range(index)
        for pro_index in pro_range:
            if self.arr[pro_index] is None:
                return pro_index
            if self.arr[pro_index][0] == key:
                return pro_index
        else:
            raise Exception("Hashmap Full")
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,val)
        else:
            new_h = self.probe_slot(key,h)
            self.arr[new_h] = (key,val)

    def __getitem__(self,key):
        h = self.get_hash(key)
        pro_range = self.probe_range(h)
        for index in pro_range:
            element = self.arr[index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __delitem__(self,key):
        h = self.get_hash(key)
        pro_range = self.probe_range(h)
        for index in pro_range:
            element = self.arr[index]
            if element is None:
                return
            if element[0] == key:
                self.arr[index] = None
