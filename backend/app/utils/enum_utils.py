from app.models.enums import StatusTarefa

def enum_values(enum_class):
    return [e.value for e in enum_class]

def parse_status(status_url):
    if status_url:
        return StatusTarefa[status_url]
    return None
