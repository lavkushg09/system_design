from abc import ABC, abstractmethod
class ObservableBase(ABC):
    @abstractmethod
    def add(self, value):
        pass

    @abstractmethod
    def remove(self, value):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def set_data(self, observer):
        pass

    @abstractmethod
    def get_data(self):
        pass