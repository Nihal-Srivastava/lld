import ParkingLotSystem.types.Vehicle as Vehicle

class ParkingSpot:
    def __init__(self, floor_number, parking_type: Vehicle, parking_spot_id):
        self.floor_number    : str     = floor_number
        self.parking_type    : Vehicle = parking_type
        self.is_empty        : bool    = False
        self.parking_spot_id : int     = parking_spot_id

    def get_is_slot_available(self):
        return self.is_empty
    
    def can_fit_this_vehicle(self, vehicle: Vehicle.Vehicle):
        return self.parking_type > vehicle
    
    def get_parking_id(self):
        return self.parking_spot_id
    
    def set_parking_availability(self, status:bool):
        self.is_empty = status
        