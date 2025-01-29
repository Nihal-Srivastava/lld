import ParkingLotSystem.types.ParkingBooking as ParkingBooking
class ParkingBookings:
    def __init__(self):
        self.booking_list = []
    
    def add_booking(self, parking_booking : ParkingBooking.ParkingBooking):
        self.booking_list.append(parking_booking)
    
    def close_the_txn(self, parking_id):
        for booking in self.booking_list:
            if booking.get_parking_id() == parking_id and booking.get_txn_status == ParkingBooking.TxnStatus.PENDING:
                booking.calculate_and_set_amount()
                # recive payment
                booking.close_txn()
                return
    