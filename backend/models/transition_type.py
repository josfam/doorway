from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class TransitionType(Base):
    """Represents whether the user transition was an entrance or an exit"""

    __tablename__ = 'transitionTypes'

    id = Column(Integer, autoincrement=True, primary_key=True)
    number = Column(Integer, autoincrement=True)
    type = Column(String(60), nullable=False)  # entry or exit

    # relationship with entry_exit_times
    entry_exit_times = relationship(
        'EntryExitTime', back_populates='transition_type'
    )
