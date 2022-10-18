from versioning_event import VersioningEvent
from versioning_event_facade import VersioningEventFacade

def test():
    versioning_events = VersioningEventFacade.get_versioning_events()
    for versioning_event in versioning_events:
        assert isinstance(versioning_event, VersioningEvent)