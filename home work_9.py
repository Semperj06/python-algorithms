
class AMixin:
    """ Класс миксин для формирования цены и имени."""
    def __init__(self, name: str, price: (int | float)):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} {self.price}'


class Customer:
    """Класс покупатель, состоит из имени фамилии и номера телефона """
    def __init__(self, name: str, surname: str, number_phone: (int | float)):
        self.name = name
        self.surname = surname
        self.number_phone = number_phone

    def __str__(self):
        return f'Hello {self.name}, an order has been made by your number {self.number_phone}'


class Products(AMixin):
    """Класс продукты содержит в себе миксин цена и название продукта плюс описание и габориты """
    def __init__(self, name, price, description: str, dimensions: str):
        super().__init__(name, price)
        self.description = description
        self.dimensions = dimensions
    def __str__(self):
        return f'"Naming"- {self.name}\n"Price"- {self.price} uah\n"Description"- {self.description} {self.dimensions}'


class Order:
    """Класс заказ использует класс  пользователь, параметр продукты принимает в себя список"""
    def __init__(self, customer: Customer, product):
        self.customer = customer
        self.product = product

    def __str__(self):
        res = ""
        for i in self.product:
            res += " " + i.name

        return f'{self.customer} \nYour order:{res} \nAmount to pay: {self.sum()} grn'

    def sum(self):
        """Функция считает сумму списка продукты """
        suma = 0
        for s in self.product:
            suma += s.price
        return suma


if __name__ == "__main__":
    products_1 = AMixin("pan", 200)
    products_2 = AMixin("cups", 20)
    products_3 = AMixin("spoon", 45)
    products_4 = AMixin("fork", 40)
    product_information_1 = Products("pan", 200, "China manufacturer made of aluminum", "10 x 5")
    product_information_2 = Products("cups", 20, "Ceramic volume 0.5 milliliters", "1 x 1")
    product_information_3 = Products("spoon", 45, "set of 20", "2 x 2")
    product_information_4 = Products("fork", 40, "set of 20", "2 x 2")
    customer_1 = Customer("John", "Dennis", +358_44_9475_168)
    customer_2 = Customer("Jordan", "Robbins", +371_24_827_505)
    order_1 = Order(customer_1, [products_1, products_2])
    order_2 = Order(customer_2, [products_3, products_4])
####################


class Human:
    """Описываем человека его имя, фамилия, год рождения и отчество если есть"""
    def __init__(self, name: str, surname: str, date_birth: int):
        self.name = name
        self.surname = surname
        self.date_birth = date_birth

    def __str__(self):
        return f'{self.name} {self.surname[0]}.' '\n'f'Age: {self.age()} date of birth: {self.date_birth}'

    def age(self):
        """На основе года рождения считаем текущий возраст"""
        return 2021 - self.date_birth


class Student(Human):
    """Создаем под класс студент на основе класса человек, добавляем такие параметры как возраст и факультет"""
    def __init__(self, name, surname, date_birth, mobile_phone: int, faculty="math"):
        super().__init__(name, surname, date_birth)
        self.faculty = faculty
        self.mobile_phone = mobile_phone

    def __str__(self):
        res = super().__str__()
        return f'{res}'  '\n'f'faculty: {self.faculty}' '\n'f'mobile phone: {self.mobile_phone}'


class Group:
    """На базе класс студент создаем список студентов"""

    def __init__(self, student):
        self.student = student
        self.new_student = None
        self.student_magazine = []

    def __str__(self):

        return f'{self.student_magazine} '

    def append_student(self, new_student):
        """Функция добавляет студента в список"""
        """Если студент уже в списке или список состоит больше чем из 10 человек выводим о недопустимости действия"""
        if not new_student.surname in self.student_magazine and len(self.student_magazine) < 11:
           self.student_magazine.append(new_student.surname)
        else:
            print("Action is impossible")

    def delete_student(self, new_student):
        """Функция удаляет студента из списка"""
        if new_student.surname in self.student_magazine:
            self.student_magazine.remove(new_student.surname)
        else:
            print("No such student found")

    def find_student(self, new_student):
        """"Поиск студента в списке, если такой студент есть выведет информацию о нем, или выведет на экран что такого
        студента нет"""
        if new_student.surname in self.student_magazine:
            print(new_student)
        else:
            print("No such student found")


if __name__ == "__main__":
    oleh = Student("Oleh", "Olehov", 1998, 7657657)
    ivanov = Student("Ivan", "Ivanov", 2000, 7657657657)
    petrov = Student("Petr", "Petrov", 1999, 7657657657)
    alexandr = Student("Alexandr", "Alex", 1995, 32132133)
    group = Group([])
    group.append_student(ivanov)
    group.append_student(oleh)
    group.append_student(petrov)
    group.delete_student(petrov)
    group.append_student(alexandr)
    group.find_student(alexandr)



