import configparser


class EnvironmentRead:
    def __init__(self, env="TEST"):
        config = configparser.ConfigParser()
        config.read('application.properties')
        self._ENV = env
        self._config = config
        
    def get_all(self):
        return self._ENV, self._config
