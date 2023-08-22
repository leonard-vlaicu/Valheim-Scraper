"""Armour module that contains the Armour class and its subclasses"""


class Armour:
    """Armour class that contains the attributes of the armour"""

    def __init__(
        self,
        name: str,
        armour_type: str,
        quality: int,
        blocking: int,
        requirements: dict,
        image_path: str,
    ):
        self.name = name
        self.armour_type = armour_type
        self.quality = quality
        self.blocking = blocking
        self.requirements = requirements
        self.image_path = image_path

    def get_armour_type(self) -> str:
        """returns the armour type"""
        return self.armour_type

    def get_name(self) -> str:
        """returns the name of the armour"""
        return self.name

    def get_quality(self) -> int:
        """returns the quality of the armour"""
        return self.quality

    def get_blocking(self) -> int:
        """returns the blocking of the armour"""
        return self.blocking

    def get_requirements(self) -> dict:
        """returns the requirements of the armour"""
        return self.requirements

    def get_image_path(self) -> str:
        """returns the image path of the armour"""
        return self.image_path

    def __str__(self) -> str:
        """returns the string representation of the armour"""
        return (
            self.name
            + " "
            + self.armour_type
            + " "
            + str(self.quality)
            + " "
            + str(self.blocking)
            + " "
            + str(self.requirements)
            + " "
            + self.image_path
        )
