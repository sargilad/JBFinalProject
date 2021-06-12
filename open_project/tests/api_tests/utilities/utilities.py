import random
import string


class CommonUtilities:

    def get_random_string(self, str_length: int = 10, str_type: string = string.ascii_lowercase,
                          prefix: str = '') -> str:
        letters = str_type
        return prefix + ''.join(random.choice(letters) for i in range(str_length))
