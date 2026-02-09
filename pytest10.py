import pytest
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "start"

def test_vehicle():
    c = Car()
    assert c.start() == "start"
    with pytest.raises(TypeError):
        Vehicle()