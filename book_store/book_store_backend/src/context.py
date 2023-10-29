"""
Book store context

Author: Thin Pyai Win
Date:  7 October 2023
"""

from fastapi import Depends
from strawberry.fastapi import BaseContext

from database import get_db
from domain.service.book_service import BookService
from domain.service.conversation_service import ConversationService
from infra.repository.book_repository import BookRepository
from infra.repository.conversation_repository import ConversationRepository


def get_book_repository(db=Depends(get_db)):
    return BookRepository(db)


def get_book_service(book_repository: BookRepository = Depends(get_book_repository)):
    return BookService(
        book_repository=book_repository)

def get_conversation_repository(db=Depends(get_db)):
    return ConversationRepository(db)


def get_conversation_service(conversation_repository: ConversationRepository = Depends(get_conversation_repository)):
    return ConversationService(
        conversation_repository=conversation_repository)


class StoreContext(BaseContext):
    def __init__(self, book_service: BookService, conversation_service: ConversationService):
        self.book_service: BookService = book_service
        self.conversation_service: ConversationService = conversation_service


# class ConversationContext(BaseContext):
#     def __init__(self, conversation_service: ConversationService):
#         self.conversation_service: ConversationService = conversation_service


async def get_store_context(
        book_service: BookService = Depends(get_book_service),
        conversation_service: ConversationService = Depends(get_conversation_service)
) -> StoreContext:
    return StoreContext(
        book_service=book_service,
        conversation_service=conversation_service
    )

# async def get_conversation_context(
#         conversation_service: ConversationService = Depends(get_conversation_service)
# ) -> ConversationContext:
#     return ConversationContext(
#         conversation_service=conversation_service
#     )
