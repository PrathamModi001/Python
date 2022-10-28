class RailwayForm:
    def printData(self):
        print(f"The name of the attendee is: {self.name}")
        print(f"The train of their choice is: {self.train}")

form = RailwayForm()
form.name = "Harry"
form.train = "Rajdhani Express"
form.printData()