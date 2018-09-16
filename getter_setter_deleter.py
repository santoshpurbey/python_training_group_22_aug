class Employee:
    __Tax = 0.2
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def salary(self):
        tax_amount = self._salary * (Employee.__Tax)
        return self._salary - tax_amount

    @salary.setter
    def salary(self, value):
        self._salary = value

    @salary.deleter
    def salary(self):
        del self._salary

    @classmethod
    def set_tax(cls, value):
        cls.Tax = value

if __name__ == "__main__":
    e = Employee('santosh', 100000)
    print(e._name, e.salary)
    e.salary = 200000
    print(e._name, e.salary)
    del e.salary
    print(e._name, e.salary)
