from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

import typing as tp 
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
class DBSchema(BaseModel):
    key: tp.Dict[str, InputSchema]

fake_db = {
    "1": {
        "track": "Data Science",
        "mentor": "Chineidu",
        "cost": 350_000.0,
        "company": "Stutern",
    },
    "2": {
        "track": "Software Engineering",
        "mentor": "Olamide",
        "cost": 380_000.0,
        "company": "Stutern",
    },
}


@app.get("/")
def index(request: Request) -> tp.Any:
    """Basic HTML response."""

    body = ("""
            <html>
                <body style='padding: 15px;'>
                    <h1>Welcome to the API</h1>
                    <div>
                    Check the docs: <a href='/docs'>here</a>
                    </div>
                </body>
            </html>


            </html>
    """)

    return HTMLResponse(content=body)


@app.get("/fetch-all/", response_model=None)
def fetch_all() -> tp.Dict:
    """This is used to fetch all the tracks."""
    return fake_db


@app.get("/fetch-one/{id}/", response_model=InputSchema)
def fetch_one(id: int)-> tp.Dict:
    for idx, val in fake_db.items():
        if int(idx) == id:
            return val

@app.post("/add-track/{id}", response_model=InputSchema)
def add_track(id: int, data:InputSchema) -> tp.Dict:
    """This is used to add a new track and other details
    to the fake_db."""
    ids = fake_db.keys()
    ids = [int(idx) for idx in ids] # Convert to ids to int
    if id not in ids:
        # Add the new data
        fake_db[str(id)] = data
    return data


if __name__ == "__main__":
    import uvicorn

    # uvicorn.run(app=app, host="localhost", port=8000, log_level="debug")
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
