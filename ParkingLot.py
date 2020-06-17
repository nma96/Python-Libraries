import time
from enum import Enum

class TicketStatus (enum.Enum) :
    ACTIVE = 1
    COMPLETE = 2
class VehicleType (enum.Enum) :
    CAR = 1
    BIKE = 2
class SpotType (enum.Enum) :
    FREE = 1
    TAKEN = 2

class ParkingLot :
    def __init__(self, name, address) :
        self.name = name
        self.address = address
        self.level = []
    def addLevel(self, floor):
        self.level.append(floor)
    def processEntry(self, ticket) :
        for eachlevel in self.level :
            if eachlevel.spots[ticket.veh.type][SpotType.FREE] :
                ticket.spot = eachlevel.assignSpot(ticket)
                print('Entry Completed For : ', ticket.veh.num)
                break;
    def processExit(self, ticket) :
        for eachlevel in self.level :
            if ticket.spot in eachlevel.spots[ticket.veh.type][SpotType.TAKEN] :
                eachlevel.unassignSpot(ticket)
                break;
        ticket.outTime  = time.time()
        ticket.spots    = None
        ticket.status   = TicketStatus.COMPLETE
        ticket.payment  = Payment(ticket.inTime, ticket.outTime)
        print('Exit Completed For  : ', ticket.veh.num, ' Pay : ', int(ticket.payment.amount))

class ParkingLevel :
    def __init__(self, name) :
        self.name = name
        self.spots = {VehicleType.CAR : {SpotType.FREE : [], SpotType.TAKEN : []}, 
                        VehicleType.BIKE : {SpotType.FREE : [], SpotType.TAKEN : []} }
    def assignSpot(self, ticket) :
        if self.spots[ticket.veh.type][SpotType.FREE] != [] :
            spot = self.spots[ticket.veh.type][SpotType.FREE].pop()
            ticket.spot = spot
            self.spots[ticket.veh.type][SpotType.TAKEN].append(spot)
            return ticket.spot
        return False
    def unassignSpot(self, ticket) :
        self.spots[ticket.veh.type][SpotType.FREE].append(ticket.spot)
        self.spots[ticket.veh.type][SpotType.TAKEN].remove(ticket.spot)
    def addSpot(self, type, num) :
        for eachnum in range(num) :
            spot = Spot(type)
            self.spots[type][SpotType.FREE].append(spot)            

class Vehicle :
    def __init__(self, num) :
        self.id     = self.generateID()
        self.num    = num
    def generateID(self) :
        yield range(100)

class Car (Vehicle) :
    def __init__(self, num) :
        super().__init__(num)
        self.type   = VehicleType.CAR

class Bike (Vehicle) :
    def __init__(self, num) :
        super().__init__(num)
        self.type   = VehicleType.CAR

class Spot :
    def __init__(self, type) :
        self.id     = self.generateID()
        self.type   = type
    def generateID(self) :
        yield range(100)

class Payment :
    def __init__(self, inTime, outTime) :
        self.mode   = None
        self.rate   = [30, 20, 10]
        self.amount = self.calAmount(inTime, outTime)
    def getRate(self) :
        return self.rate
    def setRate(self, rate) :
        self.rate = rate
    def calAmount(self, inTime, outTime) :
        amount =  (outTime - inTime) * self.getRate()[0]
        amount += (outTime - inTime - 60 ) * self.getRate()[1] if outTime - inTime - 60 > 0 else 0
        amount += (outTime - inTime - 120 ) * self.getRate()[2] if outTime - inTime - 120 > 0 else 0
        return amount        

class Ticket :
    def __init__(self, veh) :
        self.veh     = veh
        self.status  = TicketStatus.ACTIVE
        self.inTime  = time.time()
        self.outTime = None
        self.payment = None
        self.spot    = None
    def generateID(self) :
        # some ID generation mechanism
        return ID

class DisplayBoard :
    def show(self, P) :
        for eachlevel in P.level :
            print(P.name , '-' , eachlevel.name, '- Available Parking Spots')
            print('Car  : ', len(eachlevel.spots[VehicleType.CAR][SpotType.FREE]))
            print('Bike : ', len(eachlevel.spots[VehicleType.BIKE][SpotType.FREE]))


P = ParkingLot('Google Parking Lot', '123, Fort, Mumbai')
F1 = ParkingLevel('F1')
F1.addSpot(VehicleType.CAR, 3)
F1.addSpot(VehicleType.BIKE, 3)
P.addLevel(F1)

Board = DisplayBoard()
Board.show(P)

T1 = Ticket(Car('MH05 AB 5454'))
P.processEntry(T1)

T2 = Ticket(Bike('MH05 AB 9000'))
P.processEntry(T2)

time.sleep(2)  
P.processExit(T2)

Board = DisplayBoard()
Board.show(P)