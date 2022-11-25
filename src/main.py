from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class InputSchema(BaseModel):
    track: str
    mentor: str
    cost: float
    company: str

    class Config:
        schema_extra = {
            "example": {
                "track": "Data Science",
                "mentor": "Chineidu",
                "cost": 350_000.0,
                "company": "Stutern",
            }
        }


@app.get("/")
def root():
    """This is the root."""
    return {"message": "This is the homepage."}


@app.post("/signup")
def signup(input_: InputSchema):
    return input_ # OR  return {"message": input_.track, "mentor": input_.mentor, "cost": input_.cost}
   


if __name__ == "__main__":
    import uvicorn

    # uvicorn.run(app=app, host="localhost", port=8000, log_level="debug")
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
