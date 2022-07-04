class Solution:
    def profession(self, level, pos):
        self.level = level
        self.pos = pos

        if self.level == 1:
            return 'e'

        par = self.profession(level-1,(pos+1//2))
        
        if (self.pos % 2 == 1):
            return par
        
        if par == 'e':
            return 'd'
        else:
            return 'e'  

        # if (self.profession(level-1,(pos+1)//2) == 'd'):
        #     if ((self.pos) % 2) == 1:
        #         return 'd'
        #     else:
        #         return 'e'
                
        # else:
        #     if ((self.pos) % 2) == 1:
        #         return 'e'
        #     else:
        #         return 'd'

if __name__ == '__main__':
    level = 970889615
    pos = 201184807
    ob = Solution()
    if(ob.profession(level, pos) == 'e'):
        print("Engineer")
    else:
        print("Doctor")