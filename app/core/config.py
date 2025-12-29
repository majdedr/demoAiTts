import os

ENV = os.getenv("ENV", "local")

IS_LOCAL = ENV == "local"
