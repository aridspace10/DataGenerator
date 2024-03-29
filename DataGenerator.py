import random

AVAILABLE_TYPES = ['fname', 'lname', 'full_name']
class DataGenerator():
    def __init__(self):
        pass
    """
    Generates an array of data based on the given type and number of items.
    Args:
        type (str): The type of data to generate.
        n (int): The number of items to generate.
        duplicate (bool, optional): Whether to allow duplicate items. Defaults to False.
    Returns:
        list: A list of processed data based on the given type and number of items.
    """
    def simple_generate(self, type: str, n: int, duplicate: bool = False) -> list:
        type = type.lower()
        processed_data = []
        if type not in AVAILABLE_TYPES:
            raise ValueError("Type must be in " + str(AVAILABLE_TYPES))
        else:
            if type != 'full_name':
                with open(type + ".txt", "r") as f:
                    raw_data = [x.strip() for x in f.readlines()]     
                    if n > len(raw_data):
                        raise ValueError("n must be less than " + str(len(raw_data)))       
                    while len(processed_data) < n:
                        data = (random.choice(raw_data))
                        if not duplicate or data not in processed_data:
                            processed_data.append(data)
            else:
                fname = self.simple_generate('fname', n)
                lname = self.simple_generate('lname', n)
                for i in range(n):
                    processed_data.append(fname[i] + ' ' + lname[i])
            return processed_data

dataGenerator = DataGenerator()
print(dataGenerator.simple_generate('full_name', 10))