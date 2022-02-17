import email
from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.contact import ContactRepository, Contact


def test_should_return_empty_contacts():
    contact_repository = ContactRepository(temp_file())
    app = create_app(repositories={"contact": contact_repository})
    client = app.test_client()

    response = client.get("/api/contact")
    assert response.json == []

def test_should_return_contacts_list():
    contact_repository = ContactRepository(temp_file())
    app = create_app(repositories={"contact": contact_repository})
    client = app.test_client()

    Jores = Contact(
        id= "contact-1",
        first_name= "Jores ",
        last_name= "Vince",
        email= "joresatte@exemple.com",
        phone= "62654662656"
    )

    Ibrahim = Contact(
        id= "contact-2",
        first_name= "Ibrahim ",
        last_name= "Diomande",
        email= "ibrahim@exemple.com",
        phone= "62654662657"
    )

    contact_repository.save(Jores)
    contact_repository.save(Ibrahim)

    response = client.get("/api/contact")
    assert response.json == [{
        "id": "contact-1",
        "first_name": "Jores ",
        "last_name": "Vince",
        "full_name": "Jores Vince",
        "email": "joresatte@exemple.com",
        "phone": "62654662656"
    },
    {
        "id": "contact-2",
        "first_name": "Ibrahim ",
        "last_name": "Diomande",
        "full_name": "Ibrahim Diomande",
        "email": "ibrahim@exemple.com",
        "phone": "62654662657"
    }
    ]

