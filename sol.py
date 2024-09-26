from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Класс для меча
class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

# Класс для лука
class Bow(Weapon):
    def attack(self):
        print("Боец стреляет из лука.")


# Класс для бойца
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None  # По умолчанию оружие не выбрано

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает новое оружие.")

    def attack(self):
        if self.weapon:
            self.weapon.attack()
        else:
            print(f"{self.name} не вооружен!")

# Класс для монстра
class Monster:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def take_damage(self):
        self.is_alive = False
        print(f"Монстр {self.name} побежден!")

# Пример работы программы

# Создаем бойца и монстра
fighter = Fighter("Воин")
monster = Monster("Дракон")

# Боец выбирает меч и атакует монстра
sword = Sword()
fighter.changeWeapon(sword)
fighter.attack()
monster.take_damage()

# Боец выбирает лук и атакует другого монстра
monster = Monster("Гоблин")  # Новый монстр
bow = Bow()
fighter.changeWeapon(bow)
fighter.attack()
monster.take_damage()
