from main import load_config

def test_config_load():
    config = load_config() 
    assert config["nodeID"] == "test"