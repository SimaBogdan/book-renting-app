class RepositoryException(Exception):

    def __init__(self, mesaj):
        self.__mesaj = mesaj

    def __str__(self):
        return self.__mesaj
    
class DuplicateIdException(RepositoryException):

    def __init__(self, mesaj):
        super().__init__(mesaj)
    
class InexistentIdException(RepositoryException):

    def __init__(self, mesaj):
        super().__init__(mesaj)