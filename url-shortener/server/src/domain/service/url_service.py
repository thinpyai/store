import hashlib

DOMAIN_VALUE = "localhost"
PROTOCOL = "http"


class UrlService:
    """
    Url service class
    """
    def __init__(self) -> None:
        """
        Initialization
        """
        pass

    def shorten_url(self, original_url: str) -> str:
        """
        Shorten url

        Args:
            original_url (str): Orignal url

        Returns:
            str: Shortened url
        """
        shortened_code = self.generate_shortened_code(original_url)
        shortened_url = f"{PROTOCOL}://{DOMAIN_VALUE}/{shortened_code}"
        return shortened_url

    def generate_shortened_code(self, original_url: str) -> str:
        """
        Generate shortened code from original url.

        Args:
            original_url (str): Orignal url

        Returns:
            str: Shortened code
        """
        hash_algorithm = hashlib.sha256()
        hash_algorithm.update(original_url.encode())
        hash_value = hash_algorithm.hexdigest()
        shortened_code = hash_value[:8]
        return shortened_code

