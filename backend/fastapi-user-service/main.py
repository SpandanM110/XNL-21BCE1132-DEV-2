from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from UnleashClient import UnleashClient
import strawberry
from strawberry.fastapi import GraphQLRouter
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Change this for production
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Feature Flags with Unleash
unleash = UnleashClient(url="http://unleash:4242/api", app_name="user-service", instance_id="123")
unleash.initialize_client()

@app.get("/")
async def root():
    feature_enabled = unleash.is_enabled("new-user-feature")
    logger.info(f"Feature Flag Status: {feature_enabled}")
    
    if feature_enabled:
        return {"message": "Feature is enabled!"}
    return {"message": "Feature is disabled."}

# Health Check Endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# GraphQL Schema
@strawberry.type
class User:
    id: int
    name: str

@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> list[User]:
        return [User(id=1, name="Alice"), User(id=2, name="Bob")]

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")

