# creating a class for the ticket
class ticket:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.stock = quantity

    #method for updating ticket quantity

    def updateQuantity (self, quantity):
        self.quantity = quantity

    def buyfromQuantity(self):
        if self.quantity == 0:
            # raise not item exception
            pass
        self.stock -= 1

# create class fot ticket machine

class ticketMachine:
    def __init__(self):
        self.amount = 0
        self.tickets = []

    def addTicket(self, ticket):
        self.tickets.append(ticket)

    def showTickets(self):
        print("\nTickets available \n*******************")

        # looping through list of tickets to see if there is any with quantity 0
        for ticket in self.tickets:
            if ticket.quantity == 0:
                self.tickets.remove(ticket) #if there is, remove that ish
        for ticket in self.tickets:
            print (ticket.name, ticket.price)

        print ('**************\n')

    def addCash(self, money):
        self.amount = self.amount + money # add money to account

    def buyTicket(self, ticket):
        if self.amount < ticket.price:
            print("Enter more money boss")
        else:
            self.amount -= ticket.price
            print ("You got " + ticket.name)
            print ("You got " + str(self.amount) + " cash left.")

    def containsTicket(self, wanted):
        ret = False
        for ticket in self.tickets:
            if ticket.name == wanted:
                ret = ticket
                break
        return ret

    def getTicket(self, wanted):
        ret = None
        for ticket in self.tickets:
            if ticket.name == wanted:
                ret = ticket
                break
        return ret

    def insertAmountForTicket(self, ticket):
        price = ticket.price
        while self.amount < price:
            self.amount = self.amount + float(input('insert' + str(price - self.amount) + ': '))

    def checkRefund(self):
        if self.amount > 0:
            print(str(self.amount) + " refunded.")
            self.amount = 0

def tick():
    machine = ticketMachine()
    ticket1 = ticket ("Rome", 1500, 5)
    ticket2 = ticket ("Geneva", 1522, 3)
    ticket3 = ticket ("Amsterdamn", 1533, 3)

    machine.addTicket(ticket1)
    machine.addTicket(ticket2)
    machine.addTicket(ticket3)
    

