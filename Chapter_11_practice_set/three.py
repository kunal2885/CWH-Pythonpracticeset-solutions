class Employee:
    _salary = 10000
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def increment(self,value):
        self._salary += value

kunal = Employee()
print(kunal.salary)
kunal.increment = 5000
print(kunal.salary)