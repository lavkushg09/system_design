from strategy.drive_strategy import DriveStrategy


class NormalDriveStrategy(DriveStrategy):

    def drive(self):
        print("Normal drive strategy")


if __name__ == "__main__":

    n=NormalDriveStrategy()
    n.drive()