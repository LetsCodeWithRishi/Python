"""Classes model state and behaviour; inheritance can share an interface."""


class Animal:
    def speak(self) -> str:
        raise NotImplementedError


class Dog(Animal):
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return f"{self.name}: bark"


class Cat(Animal):
    def speak(self) -> str:
        return "Cat: meow"


for animal in (Dog("Bruno"), Cat()):
    print(animal.speak())
