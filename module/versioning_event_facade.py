from module.github_request import GithubRequest
from module.versioning_event import VersioningEvent

class VersioningEventFacade:

    @staticmethod
    def get_versioning_events() -> [VersioningEvent]:
        list_events = GithubRequest.get_events()

        versioningEventslist = [VersioningEvent(event_type=event['type'],
                                                message=event['payload'],
                                                created_at=event['created_at'])
                                for event in list_events.content]
        return versioningEventslist
