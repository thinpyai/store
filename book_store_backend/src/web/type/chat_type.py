from typing import Optional

import strawberry


@strawberry.type
class ConversationType():
    """Conversation schema object type"""
    id: str
    question: Optional[str] = None
    answer: Optional[str] = None


@strawberry.input
class QuestionInput():
    """Book detail input schema object type"""
    question: Optional[str] = None
