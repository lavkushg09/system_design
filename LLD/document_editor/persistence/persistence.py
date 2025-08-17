from abc import ABC, abstractmethod


class Persistence(ABC):
    """
    Abstract base class for persistence operations.
    """

    @abstractmethod
    def save(self, data):
        """
        Save the data to a persistent storage.
        This method should be implemented by subclasses.
        """
        pass