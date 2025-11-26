from sqlalchemy                 import Column, String, Boolean, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class AuthHistory(Base):
    __tablename__ = 'authentification_authhistory'

    id              = Column(BigInteger, primary_key=True, autoincrement=True)
    phone           = Column(String(15), nullable=False, index=True)
    otp             = Column(String(5), nullable=False)
    token           = Column(String(256), nullable=False)
    verified        = Column(Boolean, nullable=False)
    active          = Column(Boolean, nullable=False, index=True)
    create_date     = Column(DateTime, nullable=False)
    updated_date    = Column(DateTime, nullable=False)
    device_model    = Column(String(50), nullable=True)
    device_os       = Column(String(20), nullable=True)
    device_ip       = Column(String(15), nullable=True)

    def __repr__(self):
        return (
            f"<AuthHistory(id={self.id}, phone='{self.phone}', otp='{self.otp}', "
            f"verified={self.verified}, active={self.active}, create_date={self.create_date})>"
        )
