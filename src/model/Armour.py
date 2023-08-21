
# class with constructor and methods for Armour
# Armour has a name, type, quality, blocking and requirements and an image path

class Armour:
    def __init__(self, name: str, armourType: str, quality: int, blocking: int, requirements: dict, imagePath: str):
        self.name = name
        self.armourType = armourType
        self.quality = quality
        self.blocking = blocking
        self.requirements = requirements
        self.imagePath = imagePath


    def getArmourType(self) -> str:
        return self.armourType

    def getName(self) -> str:
        return self.name
    
    def getQuality(self) -> int:
        return self.quality
    
    def getBlocking(self) -> int:
        return self.blocking
    
    def getRequirements(self) -> dict:
        return self.requirements
    
    def getImagePath(self) -> str:
        return self.imagePath

    def __str__(self) -> str:
        return self.name + " " + self.armourType + " " + self.quality + " " + self.blocking + " " + self.requirements + " " + self.imagePath
    

class LegArmour(Armour):
    pass

class ChestArmour(Armour):
    pass

class HeadArmour(Armour):
    pass

class CapeArmour(Armour):
    pass