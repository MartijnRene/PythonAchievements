import time
import os

factory = ['car']
distribution = []
shop = []

def factory_to_distribution():
    distribution.extend(factory)
    factory.clear()

def distribution_to_shop():
    shop.extend(distribution)
    distribution.clear()
    
def printlist():
    print("factory = " + str(factory))
    print("distribution = " + str(distribution))
    print("shop = " + str(shop))

def nextprint():
    time.sleep(2)
    os.system('cls')

printlist()
nextprint()
factory_to_distribution()
printlist()
nextprint()
distribution_to_shop()
printlist()
