"""
Test module for url_shorten_mutation_schema.py
"""
from .conf_test import test_client, test_db

URL_SHORTENER = '/service/url-shortener'


def test_shorten_url_normal(test_client, test_db):
    """
    Test shortenUrl endpoint in mormal pattern.

    Args:
        test_client (TestClient): Test client
        test_db (Generator): Generator
    """

    # prepare
    sample_long_url = 'https://url-shortener/services/123456789/asdfghjkl'
    query = '''
        mutation ShortenUrl {
            shortenUrl(originalUrl: "%s")
            {
                shortUrl
                originalUrl
            }
        }
    ''' % (sample_long_url)

    # execute
    response = test_client.post(URL_SHORTENER, json={'query': query})

    # verify
    actual_json_data = response.json()
    actual_short_url = actual_json_data.get('data', {}).get('shortenUrl', {})

    assert actual_short_url.get('shortUrl') == 'http://localhost:8080/shorten-url/cc31c447d17c30c7'
    assert actual_short_url.get('originalUrl') == sample_long_url
