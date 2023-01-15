class solution:
    
    def __init__(self,toRevNum):
        self.toRevNum = toRevNum
        
    def reverse(self):
        temp = 0
        while self.toRevNum >0:

            remainderOf10 = self.toRevNum%10
            multi = temp*10
            revNum = multi + remainderOf10
            temp = revNum
            self.toRevNum= int(self.toRevNum/10)
        print(revNum)

classVar = solution(1234)
classVar.reverse()