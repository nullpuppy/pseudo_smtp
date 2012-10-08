from sqlalchemy import Column, Integer, String, DateTime, UnicodeText, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Message(Base):
    __tablename__ = u'message'
    __table_args__ = {'useexisting': True, 'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)
    subject = Column(String(128), nullable=False)
    body_text = Column(UnicodeText, nullable=False)
    body_html = Column(UnicodeText, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)

    def __init__(self, subject, body_text, body_html):
        self.subject = subject
        self.body_text = body_text
        self.body_html = body_html
        self.created_at = datetime.now()

class Address(Base):
    __tablename__ = u'address'
    __table_args__ = (
            UniqueConstraint('local', 'domain', name='_local_domain_uc'),
            {'useexisting': True, 'mysql_engine': 'InnoDB'}
    )

    id = Column(Integer, primary_key=True)
    local = Column(String(64), nullable=False)
    domain = Column(String(255), nullable=False)

    def __init__(self, local, domain):
        self.local = local
        self.domain = domain

class Recipient(Base):
    __tablename__ = u'message_recipients'
    __table_args__ = {'useexisting': True, 'mysql_engine': 'InnoDB'}

    address_id = Column(Integer, ForeignKey('address.id'), primary_key=True)
    message_id = Column(Integer, ForeignKey('message.id'), primary_key=True)

    def __init__(self, message_id, address_id):
        self.message_id = message_id
        self.address_id = address_id

class Sender(Base):
    __tablename__ = u'message_sender'
    __table_args__ = {'useexisting': True, 'mysql_engine': 'InnoDB'}

    address_id = Column(Integer, ForeignKey('address.id'))
    message_id = Column(Integer, primary_key=True)

    def __init__(self, message_id, address_id):
        self.message_id = message_id
        self.address_id = address_id

