import os
import v20
import yaml
from pathlib import Path

class ConfigPathError(Exception):
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return f"{self.path} is invalid path"

class Config:

    def __init__(self):
          self.hostname = None
          self.streaming_hostname = None
          self.port = 443
          self.ssl = True
          self.token = None
          self.username = None
          self.accounts = []
          self.active_account = None
          self.path = None
          self.datetime_format = "UNIX"

    def load(self):
        if os.environ.get("FLASK_ENV", None) == "development":
            path = Path(__file__).parent.parent / "secret" / "oanda_api_practise.yml"
        elif os.environ.get("FLASK_ENV", None) == "production":
            path = Path(__file__).parent.parent / "secret" / "oanda_api.yml"
        try:
            with open(path) as f:
                y = yaml.load(f, Loader=yaml.FullLoader)
                self.username = y.get("username", self.username)
                self.token = y.get("token", self.token)
                self.accounts = y.get("accounts", self.accounts)
                self.active_account = y.get("active_account", self.active_account)
                self.hostname = y.get("hostname", self.hostname)
                self.streaming_hostname = y.get("streaming_hostname", self.streaming_hostname)
                self.port = y.get("port", self.port)
                self.ssl = y.get("ssl", self.ssl)
                self.datetime_format = y.get("datetime_format", self.datetime_format)
        except:
            raise ConfigPathError(path)

    def create_context(self):
        ctx = v20.Context(
                self.hostname,
                self.port,
                self.ssl,
                token=self.token,
                datetime_format=self.datetime_format)
        return ctx 

    def __str__(self):
        s = ""
        s += "hostname: {}\n".format(self.hostname)
        s += "streaming_hostname: {}\n".format(self.streaming_hostname)
        s += "port: {}\n".format(self.port)
        s += "ssl: {}\n".format(str(self.ssl).lower())
        s += "token: {}\n".format(self.token)
        s += "username: {}\n".format(self.username)
        s += "datetime_format: {}\n".format(self.datetime_format)
        s += "accounts:\n"
        for a in self.accounts:
            s += "- {}\n".format(a)
        s += "active_account: {}".format(self.active_account)
        return s





