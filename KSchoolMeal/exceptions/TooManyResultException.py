class TooManyResultException(Exception):
    def __init__(self, size:int):
        super().__init__('Too Many Results founded! Please enter more accurately! results size:' + str(size) )