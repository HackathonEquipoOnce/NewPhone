from flask import Flask, request
from flask_cors import CORS
from src.domain.contact import Contact

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/info", methods=["GET"])
    def info_get():
        info = repositories["info"].get_info()
        return object_to_json(info)

    @app.route("/api/contact", methods=["GET"])
    def contact_get_all():
        contacts = repositories["contact"].get_all()
        return object_to_json(contacts)

    @app.route("/api/contact", methods=["POST"])
    def contact_contact_post():
        body = request.json
        contact = Contact(**body)
        repositories["contact"].save(contact)
        return ''
        
    
    @app.route("/api/contact/<id>", methods=["GET"])
    def contact_get_by_id(id):
        contacts = repositories["contact"].get_by_id(id)
        return object_to_json(contacts)

    @app.route("/api/contact/<id>", methods=["DELETE"])
    def delete_contact_by_id(id):
        contact_removed = repositories["contact"].remove_contact_by_id(id)
        return ""

    return app
