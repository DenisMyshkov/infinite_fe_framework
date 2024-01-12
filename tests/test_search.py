import pytest
from utils.credentials import TEXT_FOR_SEARCH, TEST_URL


@pytest.mark.parametrize("url", TEST_URL)
def test_search(app, url):
    app.open_URL(url)
    app.search_the_text(TEXT_FOR_SEARCH)
    assert TEXT_FOR_SEARCH in app.get_first_result_link_text()
