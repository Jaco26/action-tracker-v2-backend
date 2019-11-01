from app.main import create_app
from app.config import BaseConfig

app = create_app(BaseConfig)