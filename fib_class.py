class Fib:
    def __init__(self, max):
        self.max = max
        print('init call')

    def __iter__(self):
        self.a = 0
        self.b = 1
        print('iter call')
        return self

    def __next__(self):
        fib = self.a
        print('next call')
        if fib > self.max:
            print('StopIteration')
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

if __name__ == "__main__":
    print([i for i in Fib(100)])
