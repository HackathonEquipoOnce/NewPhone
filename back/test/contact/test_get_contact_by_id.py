import email
from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.contact import ContactRepository, Contact


def test_should_return_contact_by_id():
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

    response = client.get("/api/contact/contact-1")
    assert response.json == {
        "id": "contact-1",
        "first_name": "Jores ",
        "last_name": "Vince",
        "full_name": "Jores Vince",
        "email": "joresatte@exemple.com",
        "phone": "62654662656"
    }
    

