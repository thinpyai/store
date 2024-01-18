from dataclasses import dataclass


@dataclass
class Url:
    id: str
    shortened_url: str
    long_url: str
    is_valid: bool = False
