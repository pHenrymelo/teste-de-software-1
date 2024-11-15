class TitleError(Exception):
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return self.message

class AuthorError(Exception):
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return self.message
    
class PubliserError(Exception):
    def __init__(self, message):
        self.message = message
        
    def __str__(self):    
        return self.message
    
class YearError(Exception):
    def __init__(self, message):
        self.message = message
        
    def __str__(self):
        return self.message
    
class StatusError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message

class EditionError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message

class PagesError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message
    