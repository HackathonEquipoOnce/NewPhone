import sqlite3


class Contact:
    def __init__(self, id, first_name, last_name, email, phone):
        self.id= id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def full_name(self):
        return self.first_name + '' + self.last_name

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "full_name": self.full_name(),
            "email": self.email,
            "phone": self.phone,
            }


class ContactRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists contacts(
                id varchar,
                first_name varchar,
                last_name varchar,
                email varchar,
                phone vachar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()

    def get_all(self):
        sql = """select * from contacts"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()
        contacts = []
        for item in data:
            each_contact = Contact(
                id= item["id"],
                first_name = item["first_name"],
                last_name = item["last_name"],
                email= item["email"],
                phone= item["phone"]
            )
            contacts.append(each_contact)


        return contacts

    def get_by_id(self, id):
        sql = """select * from contacts where id=:id"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})

        data = cursor.fetchone()
        contact = Contact(**data)

        return contact
        

    
    def remove_contact_by_id(self, id):
        sql = """
            DELETE FROM contacts
            WHERE contacts.id = :id
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"id": id})
        conn.commit()
        cursor.close()


    def save(self, contact):
        sql = """insert into contacts (id, first_name, last_name, email, phone) values (
            :id, :first_name, :last_name, :email, :phone
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, contact.to_dict())
        conn.commit()
        cursor.close()
