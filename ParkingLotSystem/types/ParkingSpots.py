import ParkingLotSystem.types.ParkingSpot as ParkingSpot
import ParkingLotSystem.types.Vehicle as Vehicle
from typing import List
import ParkingLotSystem.types.ParkingBookings as ParkingBookings
import ParkingLotSystem.types.ParkingBooking as ParkingBooking

class ParkingSpots:
    def __init__(self):
        self.parking_spot_list : List[ParkingSpot.ParkingSpot] = []
    
    def add_parking(self, parking_spot: ParkingSpot.ParkingSpot):
        self.parking_spot_list.append(parking_spot)
    
    def find_the_parking(self, vehicle_type: Vehicle.Vehicle):
        for parking in self.parking_spot_list:
            if parking.get_is_slot_available() and parking.can_fit_this_vehicle(vehicle_type):
                return parking.get_parking_id()
        return "Not Found"
    
    def book_the_parking(self, parking_bookings:ParkingBookings.ParkingBookings, vehicle_type: Vehicle.Vehicle, vehicle_number, parking_id):
        for parking in self.parking_spot_list:
            if parking.get_parking_id() == parking_id:
                parking.set_parking_availability(False)
                break

        parking_booking = ParkingBooking.ParkingBooking(parking_id, vehicle_number, vehicle_type)
        parking_bookings.add_booking(parking_booking)
    
    def exit_vehicle(self, parking_bookings:ParkingBookings.ParkingBookings, parking_number):
        parking_bookings.close_the_txn(parking_number)
        for parking in self.parking_spot_list:
            if parking.get_parking_id() == parking_number:
                parking.set_parking_availability(True)
                return
    
    def get_all_parkings(self):
        return self.parking_spot_list