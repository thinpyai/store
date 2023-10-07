from infra.repository.conversation_repository import ConversationRepository


class ConversationService:
    def __init__(self, conversation_repository: ConversationRepository) -> None:
        self.__conversation_repository = conversation_repository
