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


fake_db = {
    1: {
        "track": "Data Science",
        "mentor": "Chineidu",
        "cost": 350_000.0,
        "company": "Stutern",
    },
    2: {
        "track": "Software Engineering",
        "mentor": "Olamide",
        "cost": 380_000.0,
        "company": "Stutern",
    },
}


@app.get("/")
def root():
    """This is the root."""
    return {"message": "This is the homepage."}

@app.get("/fetch-all/")
def fetch_all():
    """This is used to fetch all the tracks."""
    return fake_db


@app.get("/fetch-one/{id}")
def fetch_one(id: int):
    for idx, val in fake_db.items():
        if idx == id:
            return val


if __name__ == "__main__":
    import uvicorn

    # uvicorn.run(app=app, host="localhost", port=8000, log_level="debug")
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
