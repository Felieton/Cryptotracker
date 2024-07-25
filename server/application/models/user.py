from safrs import SAFRSBase, jsonapi_rpc
from application.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from application.const import *


class User(SAFRSBase, db.Model):
    """
        description: This is User
    """
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    tracked_currencies = db.Column(db.String)     # colon separated codes of tracked cryptocurrencies

    @classmethod
    @jsonapi_rpc()
    def register(cls, **kwargs):
        """
        description: Register new user
        args:
            nickname: User's nickname
            email: User's email address
            password: User's password
        """
        nickname = kwargs['nickname']
        email = kwargs['email']
        password = kwargs['password']

        user = db.session.query(User).filter(User.email == email).first()
        if user is not None:
            return {RESULT: REGISTER_EMAIL_USED}

        new_user = User(
            nickname=nickname,
            email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return {RESULT: REGISTER_SUCCESS}

    @classmethod
    @jsonapi_rpc()
    def authenticate(cls, **kwargs):
        """
        description: Authenticate user
        args:
            email: User's email address
            password: User's password
        """
        email = kwargs['email']
        password = kwargs['password']

        user = db.session.query(User).filter(User.email == email).first()
        if user is None:
            return {RESULT: LOGIN_WRONG_EMAIL}

        if user.check_password(password):
            return {RESULT: LOGIN_SUCCESS}
        else:
            return {RESULT: LOGIN_WRONG_PASSWORD}

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
