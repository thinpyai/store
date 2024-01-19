"""
URL data types
"""
from typing import List

import strawberry


@strawberry.type
class HistoryOutput():
    """History output"""
    original_url: str
    short_url: str
    date: str


@strawberry.type
class HistoryListOutput():
    """History list output"""
    history_list: List[HistoryOutput] = None
