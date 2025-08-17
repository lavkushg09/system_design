from .DocumentElement import DocumentElement

class TextElement(DocumentElement):
    """
    A test element that extends DocumentElement.
    This class provides a concrete implementation of the render method.
    """

    def __init__(self, text):
        self.text = text

    def render(self):
        """
        Render the test element.
        This method returns a simple string representation.
        """
        return self.text
