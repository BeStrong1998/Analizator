from datetime import datetime
from flask_login import UserMixin

from app import db, app, manager


# Создание и описание модели для пользователей
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(48), unique=True)
    login = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(64))

    # Поле для хранения статуса подтверждения email
    email_confirm = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'<User {self.id}: {self.email}>'


# Создание и описание модели для подтверждения email
class EmailConfirm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)
    code = db.Column(db.String(33), unique=True, nullable=False)


# Создание БД, добавить всё
with app.app_context():
    db.create_all()


# Загрузка пользователя из БД
@manager.user_loader
def load_user(user_id: int) -> int:
    """
        Выгрузка из БД

        Загрузка пользователя из БД;

        Args:
            user_id: int (первый параметр)

        Returns:
            int: id пользователя
    """
    return User.query.get(user_id)