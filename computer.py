class Computer:
    """Attributes:"""
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    """This class creates a computer and its attributes. It also allows the computer to change its price and update its OS"""

    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?

    def update_price(self, new_price:int):
        self.price = new_price

    def update_os(self, new_os:str):
        self.operating_system = new_os
    

