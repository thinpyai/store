""" File for router definition. Query and Mutation schemas for GraphQLRouter are setup."""
import strawberry
from strawberry.fastapi import GraphQLRouter

import context
from web.schema import (book_mutation_schema, book_query_schema,
                        chat_mutation_schema)


@strawberry.type
class Query(book_query_schema.Query):
    """Query of book store

    Args:
        book_query_schema (Query): Book query schema
    """
    ...


@strawberry.type
class Mutation(book_mutation_schema.Mutation, chat_mutation_schema.Mutation):
    """Mutation of book store

    Args:
        book_mutation_schema (Mutation): Book mutation schema
    """
    ...


schema = strawberry.Schema(query=Query, mutation=Mutation)
book_app = GraphQLRouter(schema,
                         context_getter=context.get_book_context)
