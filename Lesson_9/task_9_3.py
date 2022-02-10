class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position)
        self._income = {'wage': wage, 'bonus': bonus}

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())


worker_1 = Position('Иван', 'Таранов', 'сборщик', 14000, 10000)
print(worker_1.get_full_name())
print(worker_1.get_total_income())
