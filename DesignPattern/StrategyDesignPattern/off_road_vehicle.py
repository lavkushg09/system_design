import vehicle

class OffRoadVehicle(vehicle.Vehicle):

    def __init__(self, drive_strategy):
        super().__init__(drive_strategy)
