import strawberry
from strawberry.fastapi import GraphQLRouter

import context
from web.schema import book_schema


@strawberry.type
class Query(book_schema.Query):
    ...


@strawberry.type
class Mutation(book_schema.Mutation):
    ...


schema = strawberry.Schema(query=Query, mutation=Mutation)
book_app = GraphQLRouter(schema,
                         context_getter=context.get_book_context)
