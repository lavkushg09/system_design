from abc import ABC, abstractmethod


class DocumentElement(ABC):
    """
    Abstract base class for all document elements.
    """

    @abstractmethod
    def render(self):
        """
        Render the document element.
        This method should be implemented by subclasses.
        """
        pass
