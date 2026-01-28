from app.database import db
from app import bcrypt
from datetime import datetime,timezone
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(200),unique=True,nullable=False)
    password_hash = db.Column(db.Text,nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.now(timezone.utc))

    admin_id = db.Column(UUID(as_uuid=True),db.ForeignKey('admins.id'),nullable=False)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    
    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at.isoformat()
        }

    def __repr__(self):
        return f"<User {self.name} - {self.email}>"
