import logging
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from sqlalchemy import text
from sqlalchemy.orm import joinedload
from flask_migrate import Migrate
from server.models import db, Admin, Motor, Images
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from server.auth import Auth
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

logging.basicConfig(level=logging.INFO)

logging.info("Starting application setup")

CORS(app, resources={r"/*": {"origins": "*"}})

migrate = Migrate(app, db)

try:
    db.init_app(app)
    logging.info("Database initialized")
except Exception as e:
    logging.error(f"Error initializing database: {e}")

api = Api(app)
jwt = JWTManager(app)



class Home(Resource):
    def get(self):
        return "<h1>Premiere Group</h1>"
    
class Motors(Resource):
    def get(self):
        motors = Motor.query.all()
        response = [{'id':motor.id, 'name': motor.name, 'image': motor.image,'type': motor.type , 'description':motor.description , 'price': motor.price } for motor in motors]
        return make_response(jsonify(response))
    
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        admin = Admin.query.filter_by(username=current_user).first()
        if not admin:
            return jsonify({"message": "Unauthorized access"}), 403

        data = request.get_json()
        name = data.get('name')
        image = data.get('image')
        type = data.get('type')
        description = data.get('description')
        price= data.get('price')
        model=  data.get('model')
        mileage =  data.get('mileage')
        engine_size= data.get('engine_size')
        fuel_type= data.get('fuel_type')
        images= data.get('images')
        
        

        motor = Motor(name=name, image=image, type=type , description=description , price=price, model=model,images=images , mileage=mileage, engine_size=engine_size, fuel_type=fuel_type)
        db.session.add(motor)
        db.session.commit()

        return {"message": "Motor added successfully"}, 201


@app.route('/motors/<int:id>', methods=['GET'])
def get_car(id):
    motor = Motor.query.filter_by(id=id).options(joinedload(Motor.images)).first()
    if motor:
        images = [{'id': image.id, 'image_url': image.image_url} for image in motor.images]
        response = {
            'id': motor.id,
            'name': motor.name,
            'image': motor.image,
            'type': motor.type,
            'description': motor.description,
            'price': motor.price,
            'model': motor.model,
            'mileage': motor.mileage,
            'images': images,
            'engine_size': motor.engine_size,
            'fuel_type': motor.fuel_type
        }
        return jsonify(response), 200
    return jsonify({'error': 'Car does not exist in the database'}), 404

@app.route('/motors/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_car(id):
    current_user = get_jwt_identity() 
    admin = Admin.query.filter_by(username=current_user).first()
    if not admin:
        return jsonify({"message": "Unauthorized access"}), 403

    motor = Motor.query.filter_by(id=id).first()
    if motor:
        db.session.delete(motor)
        db.session.commit()
        return jsonify({'message':'motor deleted successfully!'}), 200
    return jsonify({'error': 'Car does not exist in the database'}), 404

@app.route('/motors/<int:id>', methods=['PATCH'])
@jwt_required()
def update_motor(id):
    current_user = get_jwt_identity()
    admin = Admin.query.filter_by(username=current_user).first()
    if not admin:
        return jsonify({'error': 'Unauthorized'}), 401

    motor = Motor.query.get(id)
    if not motor:
        return jsonify({'error': 'Motor not found'}), 404

    # Get the updated data from the request
    data = request.json
    categories = ['name', 'description', 'price', 'image', 'model', 'engine', 'fuel_type', 'engine_number', 'model']

    # Loop over the categories and update motor data
    for category in categories:
        if category in data:
            setattr(motor, category, data[category])

    # Commit changes to the database
    try:
        db.session.commit()
        return jsonify({'message': f'{category} updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    

@app.route('/motors/<int:motor_id>/images', methods=['GET'])
def get_motor_images(motor_id):
    # Retrieve the motor by its ID
    

    # Retrieve images associated with the motor
    images = Images.query.filter_by(motor_id=motor_id).all()
    
    # Serialize the images
    serialized_images = [{
        'id': image.id,
        'motor_id':image.motor_id,
        'image_url': image.image_url
    } for image in images]

    return jsonify({'images': serialized_images}), 200

    
@app.route('/motors/<int:motor_id>/images', methods=['POST'])
def add_motor_images(motor_id):
    motor = Motor.query.get_or_404(motor_id)  # Retrieve the motor by its ID or return a 404 error if not found

    data = request.json

    # Check if the 'image_urls' field is present in the request data
    if 'image_urls' not in data:
        return jsonify({'message': 'Image URLs are required'}), 400

    try:
        # Create new image objects and associate them with the motor
        images = [Images(motor_id=motor_id, image_url=image_url) for image_url in data['image_urls']]

        # Add the new image objects to the session
        db.session.add_all(images)

        # Commit the changes to the database
        db.session.commit()

        return jsonify({'message': 'Images added successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
@app.route('/images/<int:image_id>', methods=['DELETE'])
def delete_image(image_id):
    # Retrieve the image by its ID
    image = Images.query.filter_by(id=image_id).first()

    try:
        # Delete the image from the database
        db.session.delete(image)
        db.session.commit()

        return jsonify({'message': 'Image deleted successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500



     
class Admins(Resource):
    # @jwt.required()
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password') 
        if not username or not password:
            return {'error':'please provide a username and a password'}, 401      
        admin = Admin.query.filter_by(username=username).first()
        if admin and password:
                access_token = create_access_token(identity=admin.username)
                return {'access_token': access_token}, 200
        else:
                return {"message": "invalid credentials"}, 401

@app.route('/premiere/admin', methods=['POST'])
def token_admin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')       
    admin_instance = Admin(username=username, password=password)
    Auth.set_admin(admin_instance, password)
    db.session.add(admin_instance)
    db.session.commit()
    return {"message": "Admin registered successfully"}, 201

            


api.add_resource(Home, '/')
api.add_resource(Motors, '/motors')
api.add_resource(Admins, '/admin')




if __name__ == '__main__':
    app.run(port=5000, debug=True)


    
    