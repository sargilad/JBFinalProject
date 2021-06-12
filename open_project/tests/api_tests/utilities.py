import random
import string


class CommonUtilities:

    @staticmethod
    def get_random_string(str_length: int = 10, str_type: string = string.ascii_lowercase, prefix: str = '') -> str:
        letters = str_type
        return prefix + ''.join(random.choice(letters) for i in range(str_length))
