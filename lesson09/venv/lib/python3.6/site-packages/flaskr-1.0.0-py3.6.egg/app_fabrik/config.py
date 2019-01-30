import os


class Config:
    TEST_VARIABLE = "Config"


class DevConfig(Config):
    TEST_VARIABLE = "Dev Config"


class TestConfig(Config):
    TEST_VARIABLE = "Test Config"


def runtime_config():
    env = os.environ.get("ENV")
    if env == "DEV":
        return DevConfig
    if env == "TEST":
        return TestConfig
    else:
        return Config