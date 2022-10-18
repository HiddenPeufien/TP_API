from Response import Response
from GithubRequest import GithubRequest
import requests


def test_github_request():
    events = GithubRequest.get_events()
    assert isinstance(events, Response)
