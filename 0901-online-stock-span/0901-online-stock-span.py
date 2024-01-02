class StockSpanner:

    def __init__(self):
        self.stack = []  # Initialize an empty stack to store prices and spans

    def next(self, price: int) -> int:
        span = 1  # Initialize the span for the current price
        # Traverse the stack and pop the elements while the stack is not empty
        # and the previous prices are less than or equal to the current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]  # Add the span of the popped price to the current span

        self.stack.append((price, span))  # Push the current price and its span to the stack
        return span  # Return the span for the current price


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)