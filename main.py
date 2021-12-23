#I did this code by myself
#The purpose of this code is for me to learn object oriented programming
class Gaming:
    #above is the class

    def __init__(self,console,years,):
        self.console = console
        self.years = years
        #above are attributes such as "console" and "years" these attributes serve as the type of console and how long someone has had said console.
        #above is a method which basically acts as a blueprint if I wanted to add another console to the class


    def get_years(self):
        return self.years

    def get_console(self):
        return self.console


g = Gaming('xbox',6)
g2 = Gaming('playstation', 4)

print(g.get_console())
print(g.get_years())
print(g2.get_console())
print(g2.get_years())

