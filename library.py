from exceptions import TitleError, AuthorError, PubliserError, YearError, StatusError, EditionError, PagesError
from datetime import datetime

class Book:
    def __init__(self):
        self._title = "book"
        self._publisher = "publisher"
        self._author = "author"
        
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise TitleError("O título deve ser um texto unico")
        
        if len(title) == 0:
            raise TitleError("O título não pode ser vazio")
    
    @property
    def publisher(self):
        return self._publisher
    @publisher.setter
    def publisher(self, publisher):
        if isinstance(publisher, str):
            self._publisher = publisher
        else:
            raise PubliserError("O nome da editora deve ser um texto unico")
        
        if len(publisher) == 0:
            raise PubliserError("O nome da editora não pode ser vazio")
    
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        if isinstance(author, list) or isinstance(author, str):
            self._author = author
        else:
            raise AuthorError("O autor deve ser um texto unico ou uma lista de textos")
            
        if len(author) == 0:
            raise AuthorError("O autor não pode ser vazio")
    

class CopyBook(Book):
    def __init__(self, book):
        self._title = book.title
        self._publisher = book.publisher
        self._author = book.author
        self._year = datetime.now().year
        self._edition = 1 
        self._pages = 137
        self._status = "em catalogo"
        
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year):
        if year <= datetime.now().year:
            self._year = year
        else:
            raise YearError("O ano não pode ser futuro")
        
    @property
    def edition(self):
        return self._edition
    
    @edition.setter
    def edition(self, edition):
        if isinstance(edition, int):
            self._edition = edition
        else:
            raise EditionError("A edição deve ser um número inteiro")
    
    @property
    def pages(self):
        return self._pages
    @pages.setter
    def pages(self, pages):
        if isinstance(pages, int):
            self._pages = pages
        else:
            raise PagesError("A quantidade de páginas deve ser um número inteiro")
    
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        if status in ["em catalogo", "emprestado", "indisponível"]:
            self._status = status
        else:
            raise StatusError("O status deve ser 'em catalogo', 'emprestado' ou 'indisponível'")
    
    def emprestar(self):
        if self.status == "em catalogo":
            self.status = "emprestado"
        else:
            raise StatusError("O livro não está em catalogo")
    
    def devolver(self):
        if self.status == "emprestado":
            self.status = "em catalogo"
        else:
            raise StatusError("O livro não está emprestado")