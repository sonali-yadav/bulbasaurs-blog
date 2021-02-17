# here go the general utility functions
import base64
import uuid


def generate_short_guid_with_prefix(prefix=''):
    sguid = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode().replace('=', '')
    return f"{prefix}_{sguid}"
