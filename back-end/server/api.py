from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "moonquakes.db")

origins = [
    "http://localhost:5173",
    "https://moonquake-map-front-end.vercel.app"
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World!"}

@app.get("/moonquakes")
async def read_items():
    with sqlite3.connect(db_path) as db:
        cur = db.cursor()
        cur.execute('SELECT * FROM moonquakes;')
        rows = cur.fetchall()

    return rows

@app.get("/moonquakes/show")
async def read_moonquake(moonquake_id: Optional[int] = None, 
                        type: Optional[str] = None,
                        sub_type: Optional[str] = None,
                        year: Optional[str] = None,
                        ):
    query = 'SELECT * FROM moonquakes WHERE 1 = 1 '

    if moonquake_id:
        query += f'AND id = "{moonquake_id}" '

    if type:
        query += f'AND type = "{type}" '
    
    if sub_type:
        query += f'AND sub_type = "{sub_type}" '

    if year:
        query += f'AND year = "{year}" '

    with sqlite3.connect(db_path) as db:
        cur = db.cursor()
        cur.execute(query)
        rows = cur.fetchall()

    return rows
