class A:

    def abc(self):
        print('I\'m from class A')

    def xyz(self):
        print('xyz method in  class A')

class B:
    def abc(self):
        print('i\'m from class B')

    def mno(self):
        print('mno method class B')


class C(B, A):
    def abc(self):
        print('im from class C ')
        # A().abc()
        super().abc()


if __name__ == "__main__":
    c = C()
    c.abc()
    c.xyz()
    c.mno()
