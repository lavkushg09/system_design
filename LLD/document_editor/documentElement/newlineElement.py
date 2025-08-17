from .DocumentElement import DocumentElement

class NewlineElement(DocumentElement):
    """
    A test element that extends DocumentElement.
    This class provides a concrete implementation of the render method.
    """

    def render(self):
        """
        Render the test element.
        This method returns a simple string representation.
        """
        return f"{'\n'}"
