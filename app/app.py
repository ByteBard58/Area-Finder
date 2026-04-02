from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from area_finder import area_sc
from .schema.validation import coords_val
import numpy as np
import os

app = FastAPI(title="Area Finder", version="2.0 (FastAPI)")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def index():
    html_path = os.path.join(os.path.dirname(__file__), "..", "templates", "index.html")
    return FileResponse(html_path)

@app.get("/health")
def health():
    return JSONResponse(status_code=200, content={"message": "Area Finder API is alive."})

@app.post("/calculate", status_code=201)
def calculate(incoming: coords_val):
    incoming = incoming.model_dump(mode="json")
    incoming["coord_list"] = np.array(incoming["coord_list"])
    assume_unordered: bool = incoming["assume_unordered"]
    target: np.ndarray = incoming["coord_list"]

    try:
        area = area_sc(target=target, assume_unordered=assume_unordered)
        area = float(area)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    msg = {
        "success": True,
        "message": "calculated successfully",
        "result_in_square_units": area,
        "area": area,
        "provided_coords": target.tolist()
    }
    return JSONResponse(status_code=201, content=msg)
