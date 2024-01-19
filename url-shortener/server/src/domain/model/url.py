from dataclasses import dataclass


@dataclass
class Url:
    """
    Url class model
    """
    short_url: str
    long_url: str
    is_valid: bool
    id: str = None
