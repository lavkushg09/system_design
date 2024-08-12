from abc import ABC, abstractmethod
from observable.observable_base import ObservableBase

class ObserverBase(ABC):
    def __init__(self, observable:ObservableBase):
        self.observable = observable
    @abstractmethod
    def update(self, observable):
        pass