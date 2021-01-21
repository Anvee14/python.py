class Car(object):
    def __init__(self,model,color,company,speedLimit):
        self.color = color
        self.company = company
        self.model = model
        self.speedLimit = speedLimit

    def start(self):
        print('started')

    def stop(self):
        print('stop')
    
    def accelerate(self):
        print('accelerating...')

    def changeGear(self,gearType):
        print('gearChanged')
    
    def fast(self):
        if(self.speedLimit > 200):
            print('this car is superfast')
        else:
            print('speed is fine')



BMW = Car('BB22','red','BMW', 280)
auddi  = Car('AA11','blue','auddi',200)
print(auddi.speedLimit)
auddi.fast()