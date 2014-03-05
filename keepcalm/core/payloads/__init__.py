from importlib import import_module
from abc import ABCMeta, abstractmethod
from django.conf import settings


class Payload(metaclass=ABCMeta):
    """
    Abstract class to create new payloads
    """

    @staticmethod
    @abstractmethod
    def run(signal):
        """
        This is the payload's action
        """
        return True


def get_payloads():
    """
    Returns an iterable of payloads
    """
    payloads = getattr(settings, "KEEPCALM_PAYLOADS", [])

    for payload in payloads:
        module_path, payload_class = payload.rsplit('.', 1)
        yield getattr(import_module(module_path), payload_class)
