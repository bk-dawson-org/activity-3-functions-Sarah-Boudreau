import math 
def getCylinderVolume(radius, height) :
    Volume = math.pi * (radius ** 2) * height
    return Volume

x = getCylinderVolume(10,12)
y = getCylinderVolume(2,6)
print(x)
print(y)
print(round(x,4))
print(round(x,4))

def numberOfSlices(radius, hieght, volumeOfSlices) :
    Volume = getCylinderVolume(radius, height) 
    numberOfSlices = Volume / volumeOfSlices
    return int(numberOfSlices)

numberOfSlices1 = numberOfSlices(10,10,100)
print(numberOfSlices1)

