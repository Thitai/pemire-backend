import click 
from flask.cli import with_appcontext
from models import  db, Admin, Motor, Images

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()