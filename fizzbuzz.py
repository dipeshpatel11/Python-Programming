class Check_FizzBuzz:
    def __init__(self,n):
        self.n = n
        
    def fizzbuzz(self):
        if (self.n%3 == 0) and (self.n%5 == 0):
            print('FizzBuzz')
        elif self.n%3 == 0:
            print('Fizz')
        elif self.n%5 == 0:
            print('Buzz')
        else:
            print(self.n) 
            
if __name__ == '__main__':
    c = Check_FizzBuzz(15)
    c.fizzbuzz()