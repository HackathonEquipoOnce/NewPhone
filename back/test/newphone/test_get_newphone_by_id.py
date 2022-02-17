from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.newphone import NewphoneRepository, Newphone


def test_should_return_contact_by_id():
    contact_repository = NewphoneRepository(temp_file())
    app = create_app(repositories={"newphone": contact_repository})
    client = app.test_client()

    Xiaomi = Newphone(
        id= "1",
        nombre= "xiaomi redmi 10",
        precio= "230 $",
        caracteristicas= "camera 64MP",
    )

    Samsung = Newphone(
        id= "2",
        nombre= "xiaomi popofone",
        precio= "250 $",
        caracteristicas= "camera 64MP",
    )

    contact_repository.save(Xiaomi)
    contact_repository.save(Samsung)

    response = client.get("/api/newphone/1")
    assert response.json == {
        "id": "1",
        "nombre": "xiaomi redmi 10 ",
        "precio": "230 $",
        "caracteristicas": "camera 64MP",
    }
    

