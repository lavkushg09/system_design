class Vehicle:

    def __init__(self, drive_strategy):
        self.drive_strategy = drive_strategy

    def drive(self):
        self.drive_strategy.drive()