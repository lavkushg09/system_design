from persistence.persistence import Persistence
from persistence.filePersistence import FilePersistence
from document import Document
from documentElement.textElement import TextElement
from documentElement.imageElement import ImageElement
from documentElement.newlineElement import NewlineElement

class DocumentEditor:
   
    def __init__(self, persistence:Persistence, document:Document):
        """
        Initialize the DocumentEditor with a persistence strategy and optional document elements.
        :param persistence: An instance of Persistence for saving data.
        :param document_elements: Optional list of DocumentElement instances.
        """
        self.persistence = persistence
        self.document = document



    def add_text_element(self, text):
        """
        Add a text element to the document.
        :param text: The text to be added as a TextElement.
        """
        text_element = TextElement(text)
        self.document.add_text_element(text_element)

    def add_newline_element(self):
        """
        Add a newline element to the document.
        This method creates a NewlineElement and adds it to the document.
        """
        newline_element = NewlineElement()
        self.document.add_text_element(newline_element)

    def add_image_element(self, image_path):
        """
        Add an image element to the document.
        :param image_path: The path to the image to be added as an ImageElement.
        """
        image_element = ImageElement(image_path)
        self.document.add_image_element(image_element)

    def render_document(self):
        """
        Render the document by rendering each element.
        This method returns a string representation of the document.
        """
        return self.document.render()
    
    def save_document(self):
        """
        Save the document using the persistence strategy.
        This method calls the save method of the persistence instance.
        """
        self.persistence.save(self.document.render())





def main():
    # Example usage
    persistence = FilePersistence()
    document = Document()
    editor = DocumentEditor(persistence, document)

    editor.add_text_element("Hello, World!")
    editor.add_newline_element()
    editor.add_text_element(" This is a test document.")
    editor.add_text_element(" Here is an image:")
    editor.add_newline_element()
    editor.add_image_element("path/to/image.png")
    
    rendered_document = editor.render_document()
    print(rendered_document)  # Output the rendered document

    editor.save_document()  # Save the document

if __name__ == "__main__":
    main()