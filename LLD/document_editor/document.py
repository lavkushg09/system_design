from documentElement.newlineElement import NewlineElement
from documentElement.textElement import TextElement
from documentElement.imageElement import ImageElement
class Document:
    def __init__(self):
        self.elements = []


    def add_text_element(self, element):
        """
        Add a text element to the document.
        :param element: An instance of TextElement.
        """
        if isinstance(element, (TextElement,NewlineElement)):
            self.elements.append(element)
        else:
            raise TypeError("Expected a TextElement instance.")
        

    def add_image_element(self, element):
        """
        Add an image element to the document.
        :param element: An instance of ImageElement.
        """
        if isinstance(element, ImageElement):
            self.elements.append(element)
        else:
            raise TypeError("Expected an ImageElement instance.")
        
    def render(self):
        """
        Render the document by rendering each element.
        This method returns a string representation of the document.
        """
        rendered_elements = [element.render() for element in self.elements]
        return ''.join(rendered_elements)