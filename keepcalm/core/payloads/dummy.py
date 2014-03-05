from django.conf import settings
from . import Payload


class LogPayload(object):

    def run(signal):
        print("Running log payload")
        file_path = getattr(settings, "KEEPCALM_LOG_PAYLOAD_PATH", "/tmp/keepcalm_alerts.log")
        with open(file_path, 'a') as f:
            f.write("Signal {} has expired\n".format(signal.name))

Payload.register(LogPayload)
