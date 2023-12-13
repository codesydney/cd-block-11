from app.main import app, db

@app.cli.command("create_db")
def create_db():
    db.create_all()
    print("Database created.")

if __name__ == "__main__":
    app.cli()
