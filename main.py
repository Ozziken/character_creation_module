from random import randint
# from graphic_arts.start_game_banner import run_screensaver

default_attack = 5
default_defence = 10
default_stamina = 80


class Character:
    brief_desc_char_class = 'отважный любитель приключений'
    range_value_attack = (1, 3)
    range_value_defence = (1, 5)
    special_skill = 'удача'
    special_buff = 15

    def __init__(self, name):
        """Определяем родительский класс"""
        self.name = name

    def attack(self):
        # Метод атаки
        value_attack = default_attack + randint(*self.range_value_attack)
        return (f'{self.name} нанес противнику урон '
                f' равный {value_attack}')

    def defence(self):
        # Метод блокирования
        value_defence = default_defence + randint(*self.range_value_defence)
        return (f'{self.name} нанес противнику урон '
                f' равный {value_defence}')

    def special(self):
        # Метод специального действия
        return (f'{self.name} приенил специальное умение '
                f'{special_skill}{special_buff}')


class Warrior(Character):
    brief_desc_char_class = ('дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    range_value_attack = (3, 5)
    range_value_defence = (5, 10)
    special_buff = default_stamina + 25
    special_skill = 'Выносливость'

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return (f'{__class__.__name__} - {Warrior.brief_desc_char_class}')


class Mage(Character):
    brief_desc_char_class = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    range_value_attack = (5, 10)
    range_value_defence = (-2, 2)
    special_buff = default_attack + 40
    special_skill = 'Атака'

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return (f'{__class__.__name__} - {Mage.brief_desc_char_class}')


class Healer(Character):
    brief_desc_char_class = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    range_value_attack = (-3, -1)
    range_value_defence = (2, 5)
    special_buff = default_defence + 30
    special_skill = 'защита'

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return (f'{__class__.__name__} - {Mage.brief_desc_char_class}')


warrior = Warrior('Евпатий_Коловрат')
print(warrior)
print(warrior.attack())
