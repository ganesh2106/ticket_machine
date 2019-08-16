# creating a class for the ticket
class ticket:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # method for updating ticket quantity
    def updateQuantity (self, quantity):
        self.quantity = quantity

    # method to reduce quantity
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

    # add ticket option to machine
    def addTicket(self, ticket):
        self.tickets.append(ticket)

    # show ticket options
    def showTickets(self):
        print("\nTickets available \n*******************")

        # looping through list of tickets to see if there is any with quantity 0
        for ticket in self.tickets:
            if ticket.quantity == 0:
                self.tickets.remove(ticket) #if there is, remove that ish
        for ticket in self.tickets:
            print (ticket.name, ticket.price)

        print ('**************\n')

    # method to allow user to enter money
    def addCash(self, money):
        self.amount = self.amount + money # add money to account


    # method to deduct right amount from user
    def buyTicket(self, ticket):
        if self.amount < ticket.price:
            print("Enter more money boss")
        else:
            self.amount -= ticket.price
            print ("You got " + ticket.name)
            print ("You got " + str(self.amount) + " cash left.")


    # method to check for users requested tickets in machine
    def containsTicket(self, wanted):
        ret = False
        for ticket in self.tickets:
            if ticket.name == wanted:
                ret = ticket
                break
        return ret

    # method to get users requested ticket
    def getTicket(self, wanted):
        ret = None
        for ticket in self.tickets:
            if ticket.name == wanted:
                ret = ticket
                break
        return ret

    # method to get correct amount from user
    def insertAmountForTicket(self, ticket):
        price = ticket.price
        while self.amount < price:
            self.amount = self.amount + float(input('insert ' + str(price - self.amount) + ': '))

    # method to reflect users balance
    def checkRefund(self):
        if self.amount > 0:
            print(str(self.amount) + " refunded.")
            self.amount = 0

def tick():
    # creating ticket machine
    machine = ticketMachine()

    # creating ticket types
    ticket1 = ticket ("Rome", 1500, 5)
    ticket2 = ticket ("Geneva", 1522, 3)
    ticket3 = ticket ("Amsterdamn", 1533, 3)

    # adding tickets to machine
    machine.addTicket(ticket1)
    machine.addTicket(ticket2)
    machine.addTicket(ticket3)

    # main logic
    continueToBuy = True
    while continueToBuy == True:
        machine.showTickets()
        selected = input("Select ticket: ")
        if machine.containsTicket(selected):
            ticketChoice = machine.getTicket(selected)

            machine.insertAmountForTicket(ticketChoice)
            machine.buyTicket(ticketChoice)

            a = input('Buy another ticket? (y/)n: ')
            if a == 'n':
                continueToBuy = False
                machine.checkRefund()
            else:
                continue

        else:
            print("ticket not available. Select another ticket: ")
            continue
tick()

