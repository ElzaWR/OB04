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
