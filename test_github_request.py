from module.response import Response
from module.github_request import GithubRequest


def test_github_request():
    events = GithubRequest.get_events()
    assert isinstance(events, Response)
