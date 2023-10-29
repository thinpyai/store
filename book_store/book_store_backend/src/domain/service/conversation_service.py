from infra.repository.conversation_repository import ConversationRepository


class ConversationService:
    def __init__(self, conversation_repository: ConversationRepository) -> None:
        self.__conversation_repository = conversation_repository

    def ask_question(self, question):
        return None

    def generate_gpt_content(self):
        pass

    def store_conversation(self):
        pass
