
class VersioningEvent:

    def __init__(self, event_type, message, created_at):
        self.type = event_type
        self.message = message
        self.created_at = created_at