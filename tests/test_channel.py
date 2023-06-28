from src.channel import Channel


def test_init():
    exp = Channel('channel')
    assert exp.channel_id == 'channel'


def test_print_info():
    exp = Channel('{"channel": "1"}')
    assert exp.channel_id == '{"channel": "1"}'