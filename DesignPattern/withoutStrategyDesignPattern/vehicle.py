from abc import abc
class Vehicle(abc):

    @abc.abstractmethod
    def drive(self):
        print("Normal capability")