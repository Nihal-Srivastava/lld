from fastapi import FastAPI, Request
import ParkingLotSystem.types.ParkingBookings as ParkingBookings
import ParkingLotSystem.types.ParkingSpots as ParkingSpots
import ParkingLotSystem.types.ParkingSpot as ParkingSpot

# Create a FastAPI app instance
app = FastAPI()
parking_booking = ParkingBookings.ParkingBookings()
parking_spots = ParkingSpots.ParkingSpots()

# Define a basic endpoint
@app.get("/")
def home():
    return {"message": "Hello, Uvicorn!"}

@app.post("/add/parking")
async def add_parking(request : Request):
    data = await request.json()
    parking_spot = ParkingSpot.ParkingSpot(**data)
    print(parking_spot)
    parking_spots.add_parking(parking_spot)
    return parking_spot

@app.get("/all/parkings")
async def get_all_parkings():
    return parking_spots.get_all_parkings()
