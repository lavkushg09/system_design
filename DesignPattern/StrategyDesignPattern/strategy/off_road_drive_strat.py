import strategy.drive_strategy as drive_strategy 

class OffRoadDriveStrategy(drive_strategy.DriveStrategy):

    def drive(self):
        print("Special drive strategy")