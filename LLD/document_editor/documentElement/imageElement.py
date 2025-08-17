from .DocumentElement import DocumentElement

class ImageElement(DocumentElement):
    """
    A test element that extends DocumentElement.
    This class provides a concrete implementation of the render method.
    """

    def __init__(self, image_path):
        self.image_path = image_path

    def render(self):
        """
        Render the test element.
        This method returns a simple string representation.
        """
        return f"[Image: {self.image_path}]"
