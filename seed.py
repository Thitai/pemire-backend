from app import app 
from models import Admin, Motor, db
import random

def seed_database():
    with app.app_context():
        # db.drop_all()
        

        # Seed Admins
        admin1 = Admin(username='dev', password='dev123')
        db.session.add(admin1)
        db.session.commit()
    
        
       

        # Seed Motors
        descriptions = [
        'Best quality, good infotainment system. Petrol engine, automatic.',
        'Reliable and efficient. Great fuel economy. Perfect for city driving.',
        'Luxurious interior, powerful engine. Perfect for long trips.',
        'Sleek design, advanced technology features. Hybrid engine for fuel efficiency.',
        'Sporty exterior, comfortable interior. Manual transmission for enthusiasts.'
            ]

# List of random prices (assuming price is a numeric field)
        prices = [
            '1,200,000',
            '1,500,000',
            '900,000',
            '1,800,000',
            '1,300,000'
            ]

        # List of random models
        models = [
            'Model A',
            'Model B',
            'Model C',
            'Model D',
            'Model E'
        ]

        # List of random mileages
        mileages = [
            5000,
            10000,
            20000,
            30000,
            40000
        ]

        # List of random engine sizes
        engine_sizes = [
            '2.0L',
            '2.5L',
            '3.0L',
            '1.6L',
            '1.8L'
        ]

        # List of random fuel types
        fuel_types = [
            'Petrol',
            'Diesel',
            'Hybrid',
            'Electric',
            'Plug-in Hybrid'
        ]

        # Modify the seed to include random values for missing elements
        motor1 = Motor(name='Motor 1', image='https://i.ibb.co/282z92m/Screenshot-2024-03-08-100519.png', type='Subaru', description=random.choice(descriptions), price=random.choice(prices), model=random.choice(models),engine_number=1, mileage=random.choice(mileages), images='image1.jpg', engine_size=random.choice(engine_sizes), fuel_type=random.choice(fuel_types))
        motor2 = Motor(name='Motor 2', image='https://i.ibb.co/282z92m/Screenshot-2024-03-08-100519.png', type='Subaru', description=random.choice(descriptions), price=random.choice(prices), model=random.choice(models),engine_number=2, mileage=random.choice(mileages), images='image2.jpg', engine_size=random.choice(engine_sizes), fuel_type=random.choice(fuel_types))
        motor3 = Motor(name='Motor 3', image='https://i.ibb.co/282z92m/Screenshot-2024-03-08-100519.png', type='Subaru', description=random.choice(descriptions), price=random.choice(prices), model=random.choice(models),engine_number=3, mileage=random.choice(mileages), images='image3.jpg', engine_size=random.choice(engine_sizes), fuel_type=random.choice(fuel_types))
        motor4 = Motor(name='Motor 4', image='https://i.ibb.co/282z92m/Screenshot-2024-03-08-100519.png', type='Subaru', description=random.choice(descriptions), price=random.choice(prices), model=random.choice(models),engine_number=4, mileage=random.choice(mileages), images='image4.jpg', engine_size=random.choice(engine_sizes), fuel_type=random.choice(fuel_types))
        motor5 = Motor(name='Motor 5', image='https://i.ibb.co/282z92m/Screenshot-2024-03-08-100519.png', type='Subaru', description=random.choice(descriptions), price=random.choice(prices), model=random.choice(models),engine_number=5, mileage=random.choice(mileages), images='image5.jpg', engine_size=random.choice(engine_sizes), fuel_type=random.choice(fuel_types))

        # Add all motors to the session
        db.session.add_all([motor1, motor2, motor3, motor4, motor5])

        # Commit changes to the database
        db.session.commit()

    print("Seed complete")

# Call the function to seed the database
seed_database()
