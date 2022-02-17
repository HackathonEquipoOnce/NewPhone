import sys

sys.path.insert(0, "")


from src.domain.info import InfoRepository, Info
from src.domain.contact import ContactRepository, Contact

database_path = "data/database.db"

info_repository = InfoRepository(database_path)
info_repository.save(Info(app_name="contact-list"))

contact_repository = ContactRepository(database_path)
Jores = Contact(
    id= "contact-1",
    first_name= "Jores",
    last_name= "Vince",
    email= "joresatte@exemple.com",
    phone= "62654662656"
)
Ibrahim = Contact(
    id= "contact-2",
    first_name= "Ibrahim",
    last_name= "Diomande",
    email= "ibrahim@exemple.com",
    phone= "62654662657"
)
contact_repository.save(Jores)
contact_repository.save(Ibrahim)