from flask import Flask
from flask_cors import CORS
from src.domain.newphone import Newphone

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"


    @app.route("/api/newphone", methods=["GET"])
    def newphone_get_all():
        newphones = repositories["newphone"].get_all()
        return object_to_json(newphones)

    #@app.route("/api/newphone", methods=["POST"])
    #def newphone_post():
        #body = request.json
        #newphone = Newphone(**body)
        #repositories["newphone"].save(newphone)
        #return ''
        
    
    @app.route("/api/newphone/<id>", methods=["GET"])
    def newphone_get_by_id(id):
        newphones = repositories["newphone"].get_by_id(id)
        return object_to_json(newphones)

    #@app.route("/api/newphone/<id>", methods=["DELETE"])
    #def delete_contact_by_id(id):
       # contact_removed = repositories["newphone"].remove_contact_by_id(id)
        #return ""

    return app
