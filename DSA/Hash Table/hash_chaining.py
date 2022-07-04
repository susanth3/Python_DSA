class Hashtable:
    def __init__(self):
        self.limit = 100
        self.arr = [[] for i in range(self.limit)]

    def get_hash(self,key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.limit

    # def add(self,key,val):
    #     h = self.get_hash(key)
    #     self.arr[h] = val

    # def get(self,key):
    #     h = self.get_hash(key)
    #     return self.arr[h]

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for idx,element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))
            
    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]    
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for index,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
        # self.arr[h] = None;


def stock_pair():
    stock_prices = {}
    with open("stock_prices.csv","r") as f:
        for line in f:
            tokens = line.split(",")
            day = tokens[0]
            price = float(tokens[1])
            stock_prices[day] = price



if __name__ == '__main__':
    t = Hashtable()

    t['march 6'] = 130
    t['march 6'] = 78
    t['march 30'] = 260
    t['march 12'] = 67

    print(t['march 12'])
    print(t['march 6'])
    # print(t.get_hash('march 6'))
    # print(t.get_hash('march 12'))
    # print(t.get_hash('march 30'))

