class BandBooster:
    def __init__(self,name):
        self.__name=name
        self.__boxesSold=0
    def getName(self):
        return self.__name
    def getSales(self):
        return self.__boxesSold
    def updateSales(self,update):
        self.__update=update
        self.__boxesSold+=self.__update
def main():
    band1=BandBooster("ONE")
    band2=BandBooster("TWO")
    for i in range (0,3):
        inputSale=int(input("Enter the new sale for "+ band1.getName()+" sold this week: "))
        band1.updateSales(inputSale)
        inputSale=int(input("Enter the new sale for "+ band2.getName()+" sold this week: "))
        band2.updateSales(inputSale)
    print(band1.getName(), band1.getSales())
    print(band2.getName(), band2.getSales())
main()
