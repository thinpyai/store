"""
Conversation repository

Author: Thin Pyai Win
Date:  7 October 2023
"""

from sqlalchemy.orm import Session


class ConversationRepository:
    """Conversation repository"""

    def __init__(self, db: Session) -> None:
        self.db = db
