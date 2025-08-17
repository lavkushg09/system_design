from .persistence import Persistence


class FilePersistence(Persistence):
    """
    Concrete implementation of Persistence that saves data to a file.
    """

    def save(self, data):
        """
        Save the data to a file.
        :param data: The data to be saved.
        """
        file_path = 'document_data.txt'
        with open(file_path, 'w') as file:
            file.write(data)
