class BaseService:
    def response(self, status: bool = True, message: str = "Success", code: int = 200, data=None):
        if data is None:
            data = {}

        return {
            "status": status,
            "code": code,
            "message": message,
            "data": data
        }

    def error_response(self, message: str = "Error", code: int = 500):
        return self.response(False, message, code)

    def success_response(self, message: str = "Success", code: int = 200, data=None):
        return self.response(True, message, code, data)