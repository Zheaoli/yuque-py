class RequestError(Exception):
    def __init__(self, status_code: int, response_body: str):
        message = f"Request for yuque failed, response_code:{status_code},response_body:{response_body}"
        super().__init__(message)
