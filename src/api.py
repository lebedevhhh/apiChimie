##in the name of the most merciful
##the all merciful
##GOAL: create a rest api
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///databases/database.db"
db = SQLAlchemy(app)

##classe definissant l'atome
class AtomeModel(db.Model):
    ###id represantant son nombre de protons xd
    id = db.Column(db.Integer, primary_key = True)
    ###name of atome
    name = db.Column(db.String(50), nullable = False)
    ###valence electron
    val_e = db.Column(db.Integer, nullable = False)
    ###EN
    e_negativity = db.Column(db.Float, nullable = False)
    ###MASSE_Molaire, 4 CS
    Masse_Molaire = db.Column(db.Float, nullable = False) 
    ###config, electronique (quick)
    config_e_quick = db.Column(db.String(80), nullable = False)
    ###config, electronique (full)
    config_e_full = db.Column(db.String(150), nullable = False)
    ###Charges:
    charges = db.Column(db.String(50), nullable = False)

    ###def : les choses importantes seulement
    def __repr__(self):
        return f"Atome : {self.name}, number of electrons = {self.id}"


###for the PUT HTTP method
atome_put_args = reqparse.RequestParser()
atome_put_args.add_argument(
    "name", type = str, help = "Name of the atome is required", required = True
)
atome_put_args.add_argument(
    "val_e", type = int, help = "Electron de valence of the atome is required", required = True
)
atome_put_args.add_argument(
    "e_negativity", type = float, help = "electro-negativity of the atome is required", required = True
)
atome_put_args.add_argument(
    "Masse_Molaire", type = float, help = "Masse Molaires of the atome is required", required = True
)
atome_put_args.add_argument(
    "config_e_quick", type = str, help = "configuration electro. abgreger of the atome is required", required = True
)
atome_put_args.add_argument(
    "config_e_full", type = str, help = "configuration electro. full of the atome is required", required = True
)
atome_put_args.add_argument(
    "charges", type = str, help = "Les charges of the atome is required", required = True
)

###for the update HTTP method
atome_update_args = reqparse.RequestParser()
atome_update_args.add_argument(
    "name", type = str, help = "Name of the atome is required", required = True
)
atome_update_args.add_argument(
    "val_e", type = int, help = "Electron de valence of the atome is required", required = True
)
atome_update_args.add_argument(
    "e_negativity", type = float, help = "electro-negativity of the atome is required", required = True
)
atome_update_args.add_argument(
    "Masse_Molaire", type = float, help = "Masse Molaires of the atome is required", required = True
)
atome_update_args.add_argument(
    "config_e_quick", type = str, help = "configuration electro. abgreger of the atome is required", required = True
)
atome_update_args.add_argument(
    "config_e_full", type = str, help = "configuration electro. full of the atome is required", required = True
)
atome_update_args.add_argument(
    "charges", type = str, help = "Les charges of the atome is required", required = True
)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'val_e': fields.Integer,
    "e_negativity": fields.Float,
    "Masse_Molaire": fields.Float,
    "config_e_quick": fields.String,
    "config_e_full": fields.String,
    "charges": fields.String
}


###class pr les HTTPS request
class Atome(Resource):
    @marshal_with(resource_fields)
    
    ##defining the GET method 
    def get(self, num_protons):
        result = AtomeModel.query.filter_by(id = num_protons).first()

        if not result:
            abort(404, message = "atome not found") 
        
        return result
    
    @marshal_with(resource_fields)
    ##defining the PUT request
    def put(self, num_protons):
        ###get the args from the user
        args = atome_put_args.parse_args()
        result = AtomeModel.query.filter_by(id = num_protons).first()
        
        ###the atome is already in the db
        if result:
            abort(409, message = "Atome already in the database")
        
        ###makes sense now
        atome = AtomeModel(
            id = num_protons,
            name = args['name'],
            val_e = args['val_e'],
            e_negativity = args["e_negativity"],
            Masse_Molaire = args['Masse_Molaire'],
            config_e_quick = args["config_e_quick"],
            config_e_full = args["config_e_full"],
            charges = args["charges"]
        )

        db.session.add(atome)
        db.session.commit()

        return result

    @marshal_with(resource_fields)

    ###its updtae function P A T C H
    def patch(self, num_protons):
        args = atome_update_args.parse_args()
        result = AtomeModel.query.filter_by(id = num_protons).first()

        if not result:
            abort(404, message = "atome doesnt exist in the db")
        
        ### VERIFIER si ces elements sont presents dans request
        if args['name']:
            result.name = args['name'] 
        if args['val_e']:
            result.val_e = args['val_e'] 
        if args['e_negativity']:
            result.e_negativity = args['e_negativity']
        if args['Masse_Molaire']:
            result.Masse_Molaire = args['Masse_Molaire']
        if args['config_e_quick']:
            result.config_e_quick = args['config_e_quick']
        if args['config_e_full']:
            result.config_e_fullname = args['config_e_full']
        if args['charges']:
            result.charges = args['charges'] 
        
        db.session.commit()

        return result

    
    ###DELETE ELEMENT
    def delete(self, num_protons):
        result = AtomeModel.query.filter_by(id = num_protons).first()

        if not result:
            abort(404, "atome not found")

        result.delete()
        db.session.commit()

        return result, "DELETED"


###the URL wiht the respective endPOINTS
api.add_resource(Atome, "/atome/<int:num_protons>")


if __name__ == "__main__":
    app.run(debug = True)