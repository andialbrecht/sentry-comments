from raven import Client


def generate_event(msg, dsn):
    client = Client(dsn)
    client.captureMessage(msg)
