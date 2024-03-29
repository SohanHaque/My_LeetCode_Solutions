class StockSpanner:

    def __init__(self):
        self.s=[]

    def next(self, price: int) -> int:
        a=1
        while self.s and self.s[-1][0] <= price:
            a+=self.s.pop()[1]
        self.s.append((price,a))
        return a