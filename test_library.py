import pytest
from library import Book, CopyBook
from exceptions import TitleError, AuthorError, PubliserError, YearError, StatusError, EditionError, PagesError

def test_create_book():
    book = Book()
    book.title = "Ordem Paranormal: RPG"
    book.publisher = "Jambo"
    book.author = "Cellbit"
    
    assert book.title == "Ordem Paranormal: RPG"
    assert book.publisher == "Jambo"
    assert book.author == "Cellbit"
    
def test_create_book_multiple_authors():
    book = Book()
    book.title = "Ordem Paranormal: Iniciação"
    book.publisher = "Jambo"
    book.author = ["Cellbit", "Fabio Yabu", "Aquila"]
    
    assert book.title == "Ordem Paranormal: Iniciação"
    assert book.publisher == "Jambo"
    assert book.author == ["Cellbit", "Fabio Yabu", "Aquila"]
    
def test_create_book_multiple_publisher():
    book = Book()
    
    book.title = "O principe"
    book.author = "Nicolau Maquiavel"
    
    assert book.title == "O principe"
    assert book.author == "Nicolau Maquiavel"
    
    with pytest.raises(PubliserError) as error:
        book.publisher = ["Penguin", "Carvalho"]
    assert error.value.message == "O nome da editora deve ser um texto unico"
    
def test_create_book_multiple_title():
    book = Book()
    
    with pytest.raises(TitleError) as error:
        book.title = ["Ordem Paranormal: RPG", "Livro de regras Ordem Paranormal"]
    assert error.value.message == "O título deve ser um texto unico"
    book.publisher = "Jambo"
    book.author = "Cellbit"
    
    assert book.publisher == "Jambo"
    assert book.author == "Cellbit"
    
def test_create_copybook():
    book = Book()
    book.title = "Ordem Paranormal: RPG"
    book.publisher = "Jambo"
    book.author = "Cellbit"
    
    copy = CopyBook(book)
    
    copy.year = 2021
    copy.edition = 2
    copy.pages = 413
    
    assert copy.year == 2021
    assert copy.edition == 2
    assert copy.pages == 413
    assert copy.status == "em catalogo"

def test_create_copybook_future_year():
    book = Book()
    book.title = "Ordem Paranormal: RPG"
    book.publisher = "Jambo"
    book.author = "Cellbit"
    
    copy = CopyBook(book)
    
    with pytest.raises(YearError) as error:
        copy.year = 2025
    assert error.value.message == "O ano não pode ser futuro"
    copy.edition = 3
    copy.pages = 413
    
    assert copy.edition == 3
    assert copy.pages == 413
    assert copy.status == "em catalogo"