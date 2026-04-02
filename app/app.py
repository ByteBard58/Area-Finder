from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from area_finder import area_sc
from .schema.validation import coords_val
import numpy as np

app = FastAPI(title="Area Finder",version="2.0 (FastAPI)")

@app.get("/")
def home() -> dict:
  return JSONResponse(status_code=200,content={
    "message":"Welcome to Area Finder! "
    "This API will help you to find the area of any polygon using the Shoelace Formula"
  })

@app.post("/calculate",status_code=201)
def calculate(incoming:coords_val):
  incoming = incoming.model_dump(mode="json")
  incoming["coord_list"] = np.array(incoming["coord_list"])
  assume_unordered:bool = incoming["assume_unordered"]
  target:np.ndarray = incoming["coord_list"]
  try:
    area = area_sc(target=target,assume_unordered=assume_unordered)
    area = float(area)
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))
  
  msg = {"message":"calculated successfully","result_in_square_units":area, "provided_coords":target.tolist()}
  return JSONResponse(status_code=201, content=msg)
