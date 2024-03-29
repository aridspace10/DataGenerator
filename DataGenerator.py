import random

AVAILABLE_TYPES = ['fname']
class DataGenerator():
    def __init__(self):
        pass
    def simple_generate(self, type: str, n: int) -> list:
        if type not in AVAILABLE_TYPES:
            raise ValueError("Type must be in " + str(AVAILABLE_TYPES))
        else:
            with open(type + ".txt", "r") as f:
                raw_data = [x.strip() for x in f.readlines()]     
                if n > len(raw_data):
                    raise ValueError("n must be less than " + str(len(raw_data)))       
                processed_data = []
                while len(processed_data) < n:
                    data = (random.choice(raw_data))
                    if data not in processed_data:
                        processed_data.append(data)
            return processed_data

dataGenerator = DataGenerator()
print(dataGenerator.simple_generate('fname', 50))