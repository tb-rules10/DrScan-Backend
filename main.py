import uvicorn
from fastapi import Request, FastAPI, Depends
import json
from Models import PatientModel
from CopdPrediction import *
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Gold Grade prediction route
@app.post("/api/copdPrediction")
async def predict_Emotion(req: Request):
    print("************************************");
    # Store data as per our model
    data:PatientModel = json.loads(await req.body())
    print("--> New Patient Added")
    print(data) 
    # Function to predict gold grade
    data['Gold Grade'] = predictGoldGrade(data)
    return { "status": True, "data": data }

# Dataset download route
@app.get("/api/fetchData")
async def download_file():
    file_path = "data_output.xlsx" 
    if os.path.exists(file_path):
        print("--> Data Download Req Successful")
        return FileResponse(file_path, filename="patient_data.xlsx")
    else:
        print("--> Data Download Req Failed")
        return {"error": "File not found"}




# uvicorn main:app --reload --host 0.0.0.0 --port 5000