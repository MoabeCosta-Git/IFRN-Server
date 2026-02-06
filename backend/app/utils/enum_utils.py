from app.models.enums import StatusTarefa

def parse_status(status_url):
    if status_url:
        return StatusTarefa[status_url]
    return None

def enum_keys(enum_class):
    return [e.name for e in enum_class]
