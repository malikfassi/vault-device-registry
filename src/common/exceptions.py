from ledgercommon.exceptions import CommonException


class ModelAlreadyExistException(CommonException):
    def __init__(self, model):
        message = f"Model {model} already exists"
        super().__init__(message)


class ModelDoesNotExistException(CommonException):
    def __init__(self, model):
        message = f"Model {model} does not exist"
        super().__init__(message)
