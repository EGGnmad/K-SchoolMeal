class RequestsException(Exception):
    def __init__(self, status_code):
        super().__init__('Error occurred while requests! ' + str(status_code))