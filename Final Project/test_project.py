from project import get_states, get_districts, get_main_basins, get_sub_basins

mock_data = [
    {
        "state": "Selangor",
        "district": "Petaling",
        "main_basin": "Klang River",
        "sub_basin": "Subang River",
        "water_level_current": 3.5,
        "water_level_normal_level": 2.0,
        "water_level_danger_level": 4.0,
        "water_level_trend": "RISING",
        "water_level_indicator": "ALERT",
        "water_level_update_datetime": "2023-12-05T14:30:00Z"
    }
]

def test_get_states():
    assert get_states(mock_data, user_input=1) == "Selangor"

def test_get_districts():
    assert get_districts(mock_data, user_input=1) == "Petaling"
    assert get_districts(mock_data, user_input="b") == "back"

def test_get_main_basins():
    assert get_main_basins(mock_data, user_input=1) == "Klang River"
    assert get_main_basins(mock_data, user_input="b") == "back"

def test_get_sub_basins():
    assert get_sub_basins(mock_data, user_input=1) == "Subang River"
    assert get_main_basins(mock_data, user_input="b") == "back"



