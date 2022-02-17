import sys

sys.path.insert(0, "")



from src.domain.newphone import NewphoneRepository, Newphone

database_path = "data/database.db"

#info_repository = InfoRepository(database_path)
#info_repository.save(Info(app_name="contact-list"))

contact_repository = NewphoneRepository(database_path)
Xiaomi = Newphone(
    id= "1",
    nombre= "xiaomi redmi 10",
    precio= "230 $",
    caracteristicas= "camera 64MP",
)
xiaomi = Newphone(
    id= "2",
    nombre= "xiaomi popofone",
    precio= "250 $",
    caracteristicas= "camera 64MP",
)
Samsung = Newphone(
    id= "3",
    nombre= "samsung",
    precio= "230 $",
    caracteristicas= "camera 64MP",
)
samsung = Newphone(
    id= "4",
    nombre= "samsung galaxy M30",
    precio= "290 $",
    caracteristicas= "camera 64MP",
)
Iphone = Newphone(
    id= "5",
    nombre= "iphone 11",
    precio= "330 $",
    caracteristicas= "camera 90MP",
)
iphone = Newphone(
    id= "6",
    nombre= "iphone 12 S",
    precio= "350 $",
    caracteristicas= "camera 180MP",
)

contact_repository.save(Xiaomi)
contact_repository.save(xiaomi)
contact_repository.save(Samsung)
contact_repository.save(samsung)
contact_repository.save(Iphone)
contact_repository.save(iphone)