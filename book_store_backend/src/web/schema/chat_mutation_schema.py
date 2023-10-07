"""
Live chat schema

Author: Thin Pyai Win
Date:  7 October 2023
"""

import strawberry
from strawberry.types import Info

from domain.model.conversation import Conversation
from web.type.chat_type import ConversationType, QuestionInput


@strawberry.type(name='ChatMutation')
class Mutation:
    """ Chat Mutation class """

    @strawberry.field
    def ask_question(self, info: Info, question_input: QuestionInput) -> ConversationType:
        """Ask the question.

        Args:
            info (Info): FastAPI info data context
            question_input (QuestionInput): Questin to ask

        Returns:
            BookType: Resulted book information object
        """
        book = Conversation(**question_input.__dict__)
        registered_book = info.context.book.register_book(book)
        return registered_book
