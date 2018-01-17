class Fruit(object):
    _name = 'fruit'

    @property
    def name(self):
        return self._name


class Orange(Fruit):
    _name = 'Orange'


if __name__ == '__main__':
    fruit = Orange()

    print(fruit.name)

