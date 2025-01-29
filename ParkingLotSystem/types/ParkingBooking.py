import datetime
from enum import Enum
import ParkingLotSystem.types.Vehicle as Vehicle

class TxnStatus(Enum):
    PENDING = 1
    COMPLETE = 2

class ParkingBooking:
    def __init__(self, parking_id, vehicle_number, vehicle_type):
        self.parking_id = parking_id
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.start_time = datetime.datetime.now()
        self.end_time = None
        self.total_amount = None
        self.txn_status = TxnStatus.PENDING
    
    def get_parking_id(self):
        return self.parking_id
    
    def get_txn_status(self):
        return self.txn_status
    
    def calculate_and_set_amount(self):
        end_time = datetime.datetime.now()
        hrs = ((end_time - self.start_time).min)//60
        hrs += 1
        self.total_amount = Vehicle.get_cost(self.vehicle_type, hrs)
        self.end_time  = end_time
    
    def close_txn(self):
        self.txn_status = TxnStatus.COMPLETE
