import pytest
from decode import decode


def test_raises_key_error():
    with pytest.raises(KeyError):
        decode('...........')


@pytest.mark.parametrize(
    'source_string, result',
    [
        ('-.-- .- -. .-', 'YANA'),
        ('.... -.--. .-.-.- ----.', 'H(.9'),
        # ('.....---', <class 'KeyError'>)
    ]
)
def test_decode(source_string, result):
    assert decode(source_string) == result
