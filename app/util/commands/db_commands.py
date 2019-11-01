import click
from flask.cli import with_appcontext

from app.database.seeder import seed_db

@click.command('seed-db')
@with_appcontext
def seed_db_command():
  seed_db()