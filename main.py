from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from json import dumps, loads

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy database of marks
with open("q-vercel-python.json", "r") as f:
    data = f.read()
    student_marks: list[dict[str, int | str]] = loads(data)
    student_marks_refined = {
        student["name"]: student["marks"] for student in student_marks
    }  # Convert to dictionary for easier access
    print(student_marks_refined)


@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    marks = [
        student_marks_refined.get(n, 0) for n in name
    ]  # Default to 0 if name not found
    return {"marks": marks}
