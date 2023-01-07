from typing import Optional
from slack_bolt import App
from slack_sdk import WebClient

_app: Optional[App] = None
_client: Optional[WebClient] = None

def set_app(app: App):
    """This function must be called before 'app.start()'"""
    global _app, _client
    _app = app
    _client = _app.client


def raise_uninitialized_error():
    raise RuntimeError("Please use set_app() to initialize slack2python")


def app() -> App:
    if _app is None:
        raise_uninitialized_error()
    return _app


def client() -> WebClient:
    if _client is None:
        raise_uninitialized_error()
    return _client
