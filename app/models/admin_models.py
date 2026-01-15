from app import db, bcrypt
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(200),unique=True,nullable=False)
    password_hash = db.Column(db.Text,nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.now(timezone.utc))
    users = db.relationship('User',backref='admin')

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<Admin {self.name} - {self.email}>"


