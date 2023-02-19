class ArcaeaUnlimitedAPIError(RuntimeError):
    """see https://github.com/Arcaea-Infinity/ArcaeaUnlimitedAPI-Wiki#error-status"""

    def __init__(self, status: int, message: str):
        self.status = status
        self.message = message
