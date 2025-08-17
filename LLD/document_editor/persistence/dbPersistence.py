from .persistence import Persistence

class DbPersistence(Persistence):
    """
    Concrete implementation of Persistence that saves data to a database.
    """

    def save(self, data):
        """
        Save the data to a database.
        :param data: The data to be saved.
        """
        # Here you would implement the logic to save data to a database
        # For demonstration purposes, we'll just print the data
        print(f"Saving data to database: {data}")