"""
Chat conversation.

Author: Thin Pyai Win
Date:  7 October 2023
"""
from dataclasses import dataclass


@dataclass
class Conversation:
    """ Chat conversation """
    question: str = None
    answer: str = None
