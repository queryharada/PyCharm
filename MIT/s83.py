# -*- coding:utf-8 -*-


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')


class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')


tesla_car = TeslaCar()
print(tesla_car.enable_auto_run)


class NoProperty(object):
    def __init__(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def set_x(self, v):
        self._x = abs(v)

    def del_x(self):
        self._x = None


nopro = NoProperty(100)
print(nopro.get_x())  # 100

nopro.set_x(-200)
print(nopro.get_x())  # 200

nopro.del_x()
print(nopro.get_x())  # None


class MyProperty(object):
    def __init__(self, x):
        self._x = x

    @property  # propertyの時は　x.getterと同義
    def x(self):
        return self._x

    @x.setter
    def x(self, v):
        self._x = abs(v)  # 更新前に何らかの処理をはさめる

    @x.deleter
    def x(self):
        self._x = None


mypro = MyProperty(100)
print(mypro.x)  # 100

mypro.x = -200
print(mypro.x)  # 200

del mypro.x
print(mypro.x)  # None

'''Item クラス'''


class Item(object):
    '''初期化メソッド'''

    def __init__(self, name, price):
        self.__data = {"name": name, "price": price}  # 辞書型のインスタンス

    '''get_name メソッドを作ります。'''

    def get_name(self):
        return self.__data["name"]

    '''set_name メソッドを作ります。'''

    def set_name(self, value):
        self.__data["name"] = value

    '''get_price メソッドを作ります。'''

    def get_price(self):
        return self.__data["price"]

    '''property()関数でプロパティ化します。'''
    name = property(get_name, set_name)  # 二つのメソッドを name プロパティ化します。
    price = property(get_price)  # インスタンス変数priceに関しては、get_priceのみプロパティ化します。


item = Item()
item.name = "AAAA"
item.price = 51
item.price = 70
