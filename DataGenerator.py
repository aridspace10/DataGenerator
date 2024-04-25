import random
import string
import datetime

AVAILABLE_TYPES = ['fname', 'lname', 'full_name']
DOMAINS = ['@gmail.com', '@yahoo.com', '@outlook.com']
class DataGenerator():
    def __init__(self):
        self.types = []
        self.parameters = {}
        self.data = []
    def add(self, type: str, n: int, duplicate: bool = False, domain: str = "", minlen: int = 0, maxlen: int = 12) -> None:
        if minlen < 0:
            raise ValueError("minlen must be a positive integer")
        if maxlen < 0:
            raise ValueError("maxlen must be a positive integer")
        if maxlen < minlen:
            raise ValueError("maxlen must be greater than minlen")
        self.types.append(type)
        self.parameters[type] = {'n': n, 'duplicate': duplicate, 'domain': domain, 'minlen': minlen, 'maxlen': maxlen}
    """
    Generates an array of data based on the given type and number of items.
    Args:
        type (str): The type of data to generate.
        n (int): The number of items to generate.
        duplicate (bool, optional): Whether to allow duplicate items. Defaults to False.
    Returns:
        list: A list of processed data based on the given type and number of items.
    Raises:
        ValueError: If type is not in the list of available types or if n is not a positive integer less than the length of the data file.
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
                    if n > len(raw_data) and n < 1:
                        raise ValueError("n must be a positive integer less than " + str(len(raw_data)))       
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
    """
    Generates a random email address based on the provided first name, last name, and domain.
        Parameters:
            fname (str): The first name to be used in generating the email address.
            lname (str, optional): The last name to be used in generating the email address. Defaults to an empty string.
            domain (str, optional): The domain to be used in generating the email address. Defaults to "@gmail.com".
        Returns:
            list: A list containing the generated email address.
        Raises:
            ValueError: If any of the input parameters are not of type str.
    """
    def generate_email(self, fname: str, lname: str = "", domain: str = "@gmail.com") -> list:
        if not isinstance(fname, str) or not isinstance(lname, str) or not isinstance(domain, str):
            raise ValueError("fname, lname, and domain must be strings")
        email = ""
        if not lname:
            email += fname
        else:
            choice = random.randint(1, 6)
            if choice == 1:
                email += fname + lname
            elif choice == 2:
                email += lname + fname[0]
            elif choice == 3:
                email += fname[0] + lname
            elif choice == 4:
                email += fname + lname[0]
            elif choice == 5:
                email += lname[0] + fname
            elif choice == 6:
                email += fname[0] + lname[0]
        while random.randint(1, 2) == 1:
            email += str(random.randint(0, 9))
        if not domain:
            email += "@" + random.choice(DOMAINS)
        else:
            email += "@" + domain
        return email
    def generate_password(self, length: int = 0, randomized: bool = False, special_chars: bool = False, numbers: bool = False, uppercase: bool = False, keyword: str = "") -> str:
        if not isinstance(length, int) or (length < 4 and not length):
            raise ValueError("length must be an integer larger the 4")

        if not length:
            length = random.randint(8, 16)
        choices = {
                1: lambda: random.choice(string.ascii_lowercase)}
        if uppercase and not randomized:        
            choices[len(choices) + 1] = lambda: random.choice(string.ascii_uppercase)
        if special_chars:          
            choices[len(choices) + 1] = lambda: random.choice(('!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
            ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'))
        if numbers:
            choices[len(choices) + 1] = lambda: random.choice(string.digits)
        password = ""
        if randomized:
            while len(password) < length:
                password += choices[random.randint(1, len(choices))]()
        else:
            password = ""
            convert = {"s": ["$"], "a": ["&","@"]}
            for index, char in enumerate(keyword):
                if char in convert:
                    if special_chars:
                        if random.randint(1, 2) == 1:
                            password += random.choice(convert[char])
                            continue
                password += char
            if numbers:
                split = random.randint(1, length - len(password))
                prefix = ''.join([random.choice(string.digits) for _ in range(split)])
                postfix = ''.join([random.choice(string.digits) for _ in range(split, length - len(password))])
                return prefix + password + postfix
            return password

        return password

    def generate_DOB(self, range: list = [1,34675]) -> str:
        today = datetime.datetime.now()
        rand = today - datetime.timedelta(days=random.randint(range[0], range[1]))

        return rand.strftime("%d/%m/%Y")

dataGenerator = DataGenerator()
print(dataGenerator.simple_generate('full_name', 10))
print(dataGenerator.generate_email('John', 'Doe', 'yahoo.com'))
print(dataGenerator.generate_password(keyword="password", special_chars=True, numbers=True, length = 10))
print(dataGenerator.generate_DOB(range=[1,34675]))