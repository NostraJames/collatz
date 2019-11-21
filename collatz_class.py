class CollatzClass:
    
    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i
        print('')
        print('')
        print('===========================')
        print('======Collatz Sequence =======')
        print('===========================\n')
        
    def collatz(self) -> None:
        print(self.val)
        while self.val >1:
            if  self.val % 2 == 0:
                self.val  = self.val//2
                print(self.val)
            else:
                self.val % 2 == 1
                self.val = self.val * 3 + 1
                print(self.val)
        print('')
        print('')
        print('----------------------------------------------------------------------------------------------------------------')
        print('|||||||||||||||||||||||   The Final Number Will ALWAYS be ', self.val, ' |||||||||||||||||||||||||||||')
        print('----------------------------------------------------------------------------------------------------------------')
        print('')
        print('')
        
    def __repr__(self) -> str:
        return str(self.val)
       
