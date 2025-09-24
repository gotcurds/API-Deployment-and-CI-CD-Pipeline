from app import create_app
from config import ProductionConfig

# Pass the ProductionConfig class directly to the factory
app = create_app(ProductionConfig)