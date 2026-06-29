import typer
from app.database import create_db_and_tables, get_cli_session, drop_all
from app.models import *
from fastapi import Depends
from sqlmodel import select
from sqlalchemy.exc import IntegrityError
from app.utilities import encrypt_password

cli = typer.Typer()

@cli.command()
def initialize():
    names = (
        'Bob','Kwasi','Edward','Daniel', 'Smith', 'Sergio', 'Zainab','Kris','Nicholas'
    )

    with get_cli_session() as db:
        drop_all() 
        create_db_and_tables() 
        for name in names:
            user = UserBase(username=name.lower(), email=f'{name.lower()}@mail.com', password=encrypt_password(f"{name.lower()}pass"))
            user_db = User.model_validate(user)
            db.add(user_db)
        db.commit()        
        print("Database Initialized")

@cli.command()
def test():
    pass

if __name__ == "__main__":
    cli()