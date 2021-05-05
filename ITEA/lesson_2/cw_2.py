"""
2 урок.

ДОМАШНЕЕ ЗАДАНИЕ:

1. Реализуйте базовый класс Car.
У класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Реализовать метод для user-friendly вывода информации об автомобиле.

2. Давайте представим, что мы занимаемся проектированием CRM для сервисного центра по обслуживанию и ремонту техники.
Реализуйте класс Заявка. Каждая заявка должна иметь следующие поля: уникальный идентификатор (присваивается в момент)
создания заявки автоматически, дата и время создания заявки (автоматически), имя пользователя, серийный номер
оборудования, статус (активная заявка или закрытая например, статусов может быть больше). Id заявки сделать приватным
полем.
У заявки должны быть следующие методы:
- метод, возвращающий, сколько заявка находится в активном статусе (если она в нём)
- метод, изменяющий статус заявки
- метод, возвращающий id заявки

3. Реализовать класс матрицы произвольного типа. При создании экземпляра передаётся вложенный список. Для объектов
класса реализовать метод сложения и вычитания матриц, а также умножения, деления матрицы на число и user-friendly вывода
матрицы на экран.
"""

#############################################################
############################ PEP8 ###########################
#############################################################

# Это золотой стандарт написания кода на Python
# подробности - https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html


#############################################################
######################## Правило LEGB #######################
#############################################################

# имя переменной, в которой лежит функция print. Пример built-it области видимости (B - built-it)
from copy import copy

print
list
sorted

# какая-то константа в глобальной области видимости (G - global)
CONST = 0


def my_func():
    # функция имеет доступ к глобальной переменной "на чтение", но если попробуем изменить значение
    # переменной относительно самой себя: CONST += 1, то получим ошибку!
    print(CONST)


def my_func_2():
    # global позволяет нам подвязаться к глобальной переменной. Теперь можно изменить её значение относительно
    # самой себя
    global CONST
    CONST += 1


my_func()
my_func_2()
my_func_2()
my_func()


def my_func_3():
    # пример переменной в локальной области видимости объемлющей функции (E - enclosing)
    a = 1

    def my_func_4():
        nonlocal a  # без nonlocal изменить относительно самой себя не получится, доступ будет только на чтение
        print(a)
        a += 100

    my_func_4()
    print(a)


my_func_3()

#############################################################
######################## Декораторы #########################
#############################################################

# Декоратор в целом - паттерн проектирования, который позволяет повлиять на поведение функции
# без её изменения. Идея состоит в том, что функция это тоже объект, который можно передавать
# в другую функцию в качестве аргумента и возвращать в качестве результата работы другой
# функции

# Декоратор в Python - синтаксический сахар, который позволяет нам обернуть одну функцию другой


def my_test_func():
    print("Я тестовая функция")


def my_simple_func(f):
    """Функция, которая на вход принимает другую функцию и вызывает её внутри себя и
    возвращает результат её исполнения"""
    print(f"Я функция my_simple_func и я приняла на вход функцию {f}. Сейчас вызову её.")
    res = f()
    print("Вызов переданной функции завевршён")
    return res


my_simple_func(my_test_func)


# давайте представим, что теперь наша передаваемая функция должна иметь аргументы:
def my_test_func_args(a, b):
    print("Я тестовая функция")
    return a + b


def my_simple_func_2(f):
    """Функция, которая на вход принимает другую функцию. Далее внутри себя она собирает новую функцию,
    которая использует в себе ту, которую мы прокинули. Собранная фукция возвращается как результат работы"""

    def inner(a, b):
        print(f"Я функция my_simple_func и я приняла на вход функцию {f} с аргументами {a, b}. Сейчас вызову её.")
        res = f(a, b)
        print("Вызов переданной функции завевршён")
        return res

    return inner


my_simple_func_2(my_test_func_args)(1, 2)

# В примере выше a и b - прописаны жёстко, а теперь давайте представим, что мы хотим иметь возможность передавать
# функцию с любым количеством аргументов:


def my_simple_func_3(f):
    """Функция, которая на вход принимает другую функцию. Далее внутри себя она собирает новую функцию,
    которая использует в себе ту, которую мы прокинули. Собранная фукция возвращается как результат работы"""

    def inner(*fargs, **fkwargs):
        print(f"Я функция my_simple_func и я приняла на вход функцию {f} с аргументами {fargs, fkwargs}. "
              f"Сейчас вызову её.")
        res = f(*fargs, **fkwargs)
        print("Вызов переданной функции завевршён")
        return res

    return inner


# А вот и синтаксический сахар!!!
@my_simple_func_3
def test_func_zero():
    print("Я функция без аргументов и без особенного возвращаемого результата")


@my_simple_func_3
def test_func_args(a, b, c, d):
    print("Я функция с кучей аргументов и возвращаемым результатом")
    return [a, b, c, d]


print(test_func_zero)
print(test_func_args)
# ХОЗЯЙКЕ НА ЗАМЕТКУ: наши функции test_func_zero и test_func_args теперь на самом деле содержат внутри
# функцию inner!!!!

# Последний шаг - я хочу, чтобы функция-декоратор тоже принимала параметр:


def my_simple_func_5(some_param):
    """Эта функция принимает на вход параметр, который используется для формирования функции, которая
    будет возвращена в качестве результата вызова и которая уже В СВОЮ ОЧЕРЕДЬ ЗАДЕКОРИРУЕТ ДРУГУЮ!"""
    def my_simple_func_4(f):
        print(f"Ого! Кто-то задал для функции-декоратора параметр: {some_param}!")

        def inner(*fargs, **fkwargs):
            print(f"Я функция my_simple_func и я приняла на вход функцию {f} с аргументами {fargs, fkwargs}. "
                  f"Сейчас вызову её.")
            res = f(*fargs, **fkwargs)
            print("Вызов переданной функции завевршён")
            return res

        return inner
    return my_simple_func_4


@my_simple_func_5(some_param=1010101010)
def test_func_args(a, b, c, d, *args, **kwargs):
    print("Я функция с кучей аргументов и возвращаемым результатом")
    return [a, b, c, d, args, kwargs]


print(test_func_args(1, 2, 3, 4, 'sdfasdfasdfasd', k=500, m=700))

# ещё подробности вот тут - https://www.youtube.com/playlist?list=PLlKID9PnOE5h8VJyEiEd_Uv_-tt9KX7MD


#############################################################
#################### Рекурсивные функции ####################
#############################################################

# Рекурсивная функция - функция, которая вызывает саму себя. Классический пример для новичков - вычисление факториала.
# Более интеллектуальный пример - поиск в глубину в графе. 5! = 1 * 2 * 3 * 4 * 5 = 120
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


print(fact(5))

# достоинства рекурсии - позволяет быстрее писать код. Недостатки - можно переполнить стек вызовов и рекурсию труднее
# продумывать.

# ПОДРОБНОСТИ: Книга "Грокаем алгоритмы", глава 3.

# ХОЗЯЙКЕ НА ЗАМЕТКУ: любой цикл можно перекроить под рекурсию и наоборот.


#############################################################
########## Объявление класса и создание экземпляра ##########
#############################################################


class MyShinyClass:
    """Просто класс, который ничего не делает"""
    pass


# создание экземпляра производится с помощью () - сюда прокидываем параметры при необходимости
my_class_ex = MyShinyClass()


# Класс с инициализатором и методом-создавателем объекта
class MyShinyClassWithFields:
    """В целом это ещё один класс-бездельник, но с полями для экземпляра

    ХОЗЯЙКЕ НА ЗАМЕТКУ: когда вас спрашивают про то, что является конструктором объекта, правильнее будет сказать,
    что это методы __init__ и __new__ вместе. Сначала new собирает по 'чертежу' (то есть классу) сам объект,
    а затем уже init всё это дело инициализирует"""
    def __init__(self, param_1, param_2):  # тут прокинули значения нашего экземпляра
        """
        Этот метод инициализирует значения полей объекта.
        self - это уже сам объект нашего класса! его сюда автоматически передал метод __new__! Поэтому на
        первой позиции стоил self - это и есть этот самый уже созданный экземпляр, который мы с вами будем шатать!
        """
        self.field_1 = param_1  # объявили первое поле у экземпляра и присвоили ему значение
        self.field_2 = param_2  # объявили второе поле у экземпляра и присвоили ему значение

    def __new__(cls, *args, **kwargs):
        """Отвечает за создание объекта в памяти.
        Этот метод собирает 'болванку' экземпляра! И отдает её потом в метод __init__, чтобы проинициализировать.
        Про то, что тут написано ещё поговорим, пока просто подебажьтесь тут и убедитесь, что данный метод
        запускается ПЕРВЫМ и отдает результат своего выполнения в __init__.

        Вы спросите, что такое cls? Отвечу вам - это ЭКЗЕМПЛЯР класса type, которым является любой
        кастомный (пользовательский класс). То есть как функция является объектом, так и сам класс, по
        которому вы потом будете собирать свой объект тоже является объектом! И 'болванку' мы собираем на его основе

        ВНИМАНИЕ! ОБЫЧНО ПЕРЕОПРЕДЕЛЯТЬ ЭТОТ МЕТОД НЕ НУЖНО! ТОЛЬКО В ИСКЛЮЧИТЕЛЬНЫХ СЛУЧАЯХ (например при
        использовании паттерна SINGLETONE)"""
        return super().__new__(cls)


# Создаём экземпляр нашего класса:
my_class_ex_with_fields = MyShinyClassWithFields(param_1=1, param_2=2)

# обратимся к полям (картинка с полем и рожью):
print(my_class_ex_with_fields.field_1)
print(my_class_ex_with_fields.field_2)


# теперь давайте напишем класс, у которого помимо полей для экземпляра есть ещё и методы для использования
# через экземпляр, а также поля самого класса. Чтобы было более приближённо к реальности, пусть это будет
# класс двумерной точки
class Point2D:
    """Класс двумерной точки, которая ещё и следит за тем, сколько её экземпляров было создано!"""
    total_2d_point_counter = 0  # это поле КЛАССА!

    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x  # это поле ЭКЗМПЛЯРА!
        self.coord_y = coord_y

    def my_shiny_method(self):
        result = self.coord_x + self.coord_y
        if result > 0:
            return result
        else:
            raise ValueError("Result is ZERO!")

    def __new__(cls, *args, **kwargs):
        cls.total_2d_point_counter += 1  # увеличиваем счетчик экземпляров на единицу
        return super().__new__(cls)


# создаем парочку экземпляров и потом пробуем запустить метод одного из них и ещё проверить счетчик экземпляров
point_1 = Point2D(1, 2)
point_2 = Point2D(3, 4)
print("Результат работы метода: ", point_1.my_shiny_method())
print("Количество экземпляров класса во Вселенной: ", point_1.total_2d_point_counter)


###################################################################################
########## Принципы ООП (подражание, инкапсуляция, полиморфизм) в Python ##########
###################################################################################

# Во первых эти 3 слова вы должны произнести, когда вас попросят сказать, на каких понятиях стоит ООП.

# ПОДРАЖАНИЕ - оно же НАСЛЕДОВАНИЕ есть концепция объектно-ориентированного
# программирования, согласно которой абстрактный тип данных может наследовать данные и функциональность некоторого
# существующего типа, способствуя повторному использованию компонентов программного обеспечения.
# Наследование это очень прикольно, когда есть не только копипаста кода из класса в класс, но и когда появляется
# возможность декомпозировать логику нескольких классов и вынести что-то общее в класс-родитель.

# ПРИМЕР ИЗ РАБОТЫ: Например у нас может быть общий класс для исполнения задач, которые требуют ограничения по RPS
# (количеству запросов к сервису в секунду) и мы выносим эту логику в родительский класс (он же "суперкласс").

# Давайте отнаследуемся от нашего класса Point2D
class Point3D(Point2D):
    """Дочерний класс. Вся логика работы родительского всязывается с ним. Теперь мы можем добавить новые методы,
    а также переопределить поведение старых родительских для наследника"""

    def __init__(self, coord_x, coord_y, coord_z):
        """Ключевое слово super означает, что мы обращаемся к родительскому методу! В нашей постановке задачи
        мы хотим докинуть новое поле в наш класс, а именно третью координату в пространстве!"""
        super().__init__(coord_x, coord_y)
        self.coord_z = coord_z


# давайте еще напишем функцию, которая будет возвращать нам строку с информацией по тому, что такое точка
def help_info_func():
    return """Одно из фундаментальных понятий математики, абстрактный объект в пространстве, не имеющий никаких 
    измеримых характеристик (нульмерный объект).
    
    В евклидовой геометрии точка — это неопределяемое понятие, на котором строится геометрия, то есть точка не может
    быть определена в терминах ранее определённых объектов. Иными словами, точка определяется только некоторыми 
    свойствами, называемыми аксиомами, которым она должна удовлетворять. В частности, геометрические точки не 
    имеют никакой длины, площади, объёма или какой-либо другой размерной характеристики. Распространённым толкованием
    является то, что понятие точки предназначено для обозначения понятия уникального местоположения 
    в евклидовом пространстве.

    Физический смысл точки — материальная точка."""

# так вот, чтобы эта функция никуда не потерялась, хорошо бы засунуть её прямо в КЛАСС! Как вы можете видеть,
# она не требует для своего выполнения наличия экземпляра. Поэтому для таких "косметических" ситуаций люди
# придумали декоратор @staticmethod.

# ХОЗЯЙКЕ НА ЗАМЕТКУ: использование статического метода внутри класса дело сугубо декоративное и это лишь вопрос
# вкуса. Никаким образом это не влияет ни на производительность кода, ни на то, как он будет выглядеть аритектурно.


# пересоздадим наш класс трехмерной точки и запихнём туда нашу функцию
class Point3Dv2(Point2D):
    """Дочерний класс. Вся логика работы родительского всязывается с ним. Теперь мы можем добавить новые методы,
    а также переопределить поведение старых родительских для наследника"""

    # А теперь я хочу сделать так, чтобы моё поле нельзя было вызывать напрямую. Для этого можем воспользоваться
    # приватным модификатором доступа (картинка с приватом) - двойное нижнее подчёркивание. Теперь это поле будет
    # доступно ТОЛЬКО в пределах класса
    __total_3d_point_counter = 0

    def __init__(self, coord_x, coord_y, coord_z):
        """Ключевое слово super означает, что мы обращаемся к родительскому методу! В нашей постановке задачи
        мы хотим докинуть новое поле в наш класс, а именно третью координату в пространстве!"""
        super().__init__(coord_x, coord_y)
        self.coord_z = coord_z

    @staticmethod  # обязательно покрываем декоратором
    def help_info_func():
        return """
        Одно из фундаментальных понятий математики, абстрактный объект в пространстве, не имеющий никаких 
        измеримых характеристик (нульмерный объект).
    
        В евклидовой геометрии точка — это неопределяемое понятие, на котором строится геометрия, то есть точка не может
        быть определена в терминах ранее определённых объектов. Иными словами, точка определяется только некоторыми 
        свойствами, называемыми аксиомами, которым она должна удовлетворять. В частности, геометрические точки не 
        имеют никакой длины, площади, объёма или какой-либо другой размерной характеристики. Распространённым толкованием
        является то, что понятие точки предназначено для обозначения понятия уникального местоположения 
        в евклидовом пространстве.
    
        Физический смысл точки — материальная точка.
        """

    def __new__(cls, *args, **kwargs):
        cls.__total_3d_point_counter += 1
        return super().__new__(cls)

    # Поскольку моё поле класса теперь запривачено я могу написать специальный метод, который будет возвращать
    # значение этого поля пользователю при необходимости. Таким образом мы организуем контроль доступа к
    # элементам нашего класса (поялм и методам)
    @classmethod
    def get_total_3d_points_total_count(cls):
        """Поскольку наш счетчик никак не привязан к конкретному экземпляру, а привязан к классу, то мы можем
        использовать сам класс для того, чтобы получить значение общего количества созданных трехмерных точек.
        Обратите внимание, что в качестве аргумента прокидывается класс, а метод в таком случае покрывается
        декоратором @classmethod"""
        return cls.__total_3d_point_counter


point_3 = Point3Dv2(5, 6, 7)
print(point_3.help_info_func())
print(point_3.get_total_3d_points_total_count())

# То, что мы опробовали выше является частью т.н. инкапсуляции - механизмом связывания данных с методами класса, которые
# с этими данными работают, а также сокрытием внутренней реализации от пользователя.

# А теперь поговорим о полиморфизме. В буквальном значении полиморфизм означает множество форм.
# Полиморфизм — очень важная идея в программировании. Она заключается в использовании единственной
# сущности(метод, оператор или объект) для представления различных типов в различных сценариях использования.
# ниже представлен полиморфизм оператора сложения
print(1 + 2)
print("first" + " second")
print([1, 2, 3] + [4, 5, 6])


# а теперь давайте создадим 2 класса с одинаковым названием метода:
class FirstClass:
    def info(self):
        return "Информация о первом классе"


class SecondClass:
    def info(self):
        return "Информация о втором классе"


# нагенерим лист с ними
ls = [FirstClass() for _ in range(3)] + [SecondClass() for _ in range(3)]

# а теперь в цикле обратимся к методу info у каждого из элементов
for el in ls:
    print(el.info())

# по сути у нас получается, что мы просто реализовали интерфейс info для обоих классов.
# с помощью dir можно посмотреть какие методы вообще есть у нашего объекта (в т.ч. служебные):
print(dir(FirstClass()))

###################################################################################
########################## MRO - Method Resolution Order ##########################
###################################################################################

# в Python возможно множественное наследоание - это когда у одного класса может быть несколько родителей


class ThirdClass(FirstClass, SecondClass):
    pass


class FourthClass(SecondClass, FirstClass):
    pass


third_class_ex = ThirdClass()
fourth_class_ex = FourthClass()

# порядок наследования имеет значение! вызовется метод класса, который был первее
print(third_class_ex.info())
print(fourth_class_ex.info())

# ХОЗЯЙКЕ НА ЗАМЕТКУ: старайтесь избегать множественного наследования! При глубокой иерархии наследования
# это может сыграть с вами очень злую шутку! Ситуация, когда оно действительно оправдано:
# у вас есть неободимость создать "примесной" класс на основе какого-то из базовых без
# переписывания логики базового класса.


###################################################################################
################################ Магические методы ################################
###################################################################################

# Магические методы - это интерфейсы, которые реализуются для того, чтобы класс мог поддерживать различные виды оперций
# например сравнение, сложение, умножение и так далее.

#  Вернёмся к классу 2D точки:
#  Задача: хочу иметь возможность сравнивать между собой точки, складывать, вычитать, умножать на число.
class Point2Dv2:
    """Класс двумерной точки"""

    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __add__(self, other: 'Point2Dv2'):  # такая штука называется аннотированием типа, делается для удобства
        """Метод для реализации интерфейса сложения двух объектов типа Point2Dv2"""
        return Point2Dv2(self.coord_x + other.coord_x,
                         self.coord_y + other.coord_y)

    def __iadd__(self, other):
        """Метод для реализации интерфейса сложения двух объектов типа Point2Dv2 на месте (сложение с присваиванием)"""
        return Point2Dv2(self.coord_x + other.coord_x,
                         self.coord_y + other.coord_y)

    def __sub__(self, other):
        """Метод для реализации интерфейса вычитания двух объектов типа Point2Dv2"""
        return Point2Dv2(self.coord_x - other.coord_x,
                         self.coord_y - other.coord_y)

    def __isub__(self, other):
        """Метод для реализации интерфейса вычитания двух объектов типа Point2Dv2 на месте
        (вычитание с присваиванием)"""
        return Point2Dv2(self.coord_x - other.coord_x,
                         self.coord_y - other.coord_y)

    def __str__(self):
        """User-friendly выыод информации об объекте"""
        return f"Точка с координатами x: {self.coord_x}, y: {self.coord_y}"

    def __repr__(self):
        """Тоже вывод инфы об объекте, но для сервисных нужд"""
        return f"Точка с координатами x: {self.coord_x}, y: {self.coord_y}. Метод __repr__"

    def __eq__(self, other):
        """Операция сравнения на равенство двух объектов типа Point2Dv2"""
        return True if isinstance(other, Point2Dv2) and\
                       (self.coord_x == other.coord_x) and\
                       (self.coord_y == other.coord_y) else False

    def __call__(self, *args, **kwargs):
        """Метод, который позволяет вызывать объект, как функцию"""
        print("Я - точка! Меня вызвали как функцию!")

    def __hash__(self):
        """Позволяет сделать объекты класса хэшируемыми"""
        return self.coord_x * self.coord_y

    def __copy__(self):
        """Метод отвечает за создании копии экземпляра"""
        return Point2Dv2(self.coord_x, self.coord_y)


point_1 = Point2Dv2(1, 2)
point_2 = Point2Dv2(3, 4)
point_3 = Point2Dv2(5, 6)
point_4 = Point2Dv2(5, 6)
print(point_4)
print(point_1 + point_2 + point_3)
print(point_3 == point_2)
print(point_4 == point_3)
print(id(point_3), id(point_4))
print({point_4, point_1})
print({point_4: 1, point_2: 2})
copy_point = copy(point_4)

# адреса в памяти будут разными
print(id(copy_point), id(point_4))

# ХОЗЯЙКЕ НА ЗАМЕТКУ: когда вы реализовываете арифметические процедуры для ваших кастомных классов, следите за тем,
# чтобы результатом работы методов были новые объекты вашего класса!!!
