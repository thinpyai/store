"""Book query schema file."""

from typing import List

import strawberry
from strawberry.types import Info

from api.type.history_type import HistoryOutput


@strawberry.type(name='HistoryQuery')
class Query:
    """ Query """

    @strawberry.field
    def get_history(self, info: Info) -> List[HistoryOutput]:
        return None
