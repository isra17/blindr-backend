from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, CHAR, TIMESTAMP, PrimaryKeyConstraint
from sqlalchemy.orm import relationship, backref

import config

class Match(config.Base):
    __tablename__ = 'matches'

    match_from_id = 	Column(String, ForeignKey('users.id'))
    match_to_id =	Column(String, ForeignKey('users.id'))
    mutual =		Column(Boolean)

    __table_args__ = (PrimaryKeyConstraint('match_from_id', 'match_to_id'),)
