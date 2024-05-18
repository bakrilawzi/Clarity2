from abc import ABC,abstractmethod
class authenticates:
    def __init__(self) -> None:
        pass
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def oauth2_auth(self):
        pass

    @abstractmethod
    def send_emails(self):
        pass