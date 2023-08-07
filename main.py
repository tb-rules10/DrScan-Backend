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


@app.post("/api/copdPrediction")
async def predict_Emotion(req: Request):
    data:PatientModel = json.loads(await req.body())
    # print(data)
    # print(predictGoldGrade(data))
    data['Gold Grade'] = predictGoldGrade(data)
    # data['Gold Grade'] = random.randint(1, 4)
    # print(data['Gold Grade'])
    return { "status": True, "data": data }

@app.get("/api/fetchData")
async def download_file():
    file_path = "data_output.xlsx" 

    if os.path.exists(file_path):
        return FileResponse(file_path, filename="patient_data.xlsx")
    else:
        return {"error": "File not found"}




# uvicorn main:app --reload --host 0.0.0.0 --port 5000