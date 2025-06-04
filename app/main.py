from fastapi import FastAPI
from app.database.database import engine, Base
from app.routes import student as student_router 
from app.models import student, class_, student_class
from app.routes import class_ as class_router
from app.routes import student_class as student_class_router
from app.routes import auth as auth_router
from app.models import user
from app.routes import instructor as instructor_router
from app.models import instructor 
from fastapi.openapi.utils import get_openapi

app = FastAPI()

# Create tables automatically (for now)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Welcome to Dance Academy API"}
app.include_router(student_router.router)
app.include_router(class_router.router)
app.include_router(student_class_router.router)
app.include_router(auth_router.router)
app.include_router(instructor_router.router)

#for pasting access token to implement authorize 
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Dance Academy API",
        version="1.0.0",
        description="API with JWT authentication",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for operation in path.values():
            operation["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi