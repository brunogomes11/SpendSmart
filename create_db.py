from app import db, app

with app.app_context():
    db.create_all()


## RENDER.COM
# db.drop_all()
# db.create_all()
