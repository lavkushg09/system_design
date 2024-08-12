from observable.observable_base import ObservableBase

class MobileProduct(ObservableBase):
    def __init__(self):
        super().__init__()
        self.observers = []

    def add(self, value):
        self.observers.append(value)

    def remove(self, value):
        self.observers.remove(value)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def set_data(self, observer):
        self.observers.append(observer)