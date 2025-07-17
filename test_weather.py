from weather import get_weather

def test_get_weather():
    assert "sunny" in get_weather("Delhi")
