from fastapi import FastAPI, UploadFile, File
from google.cloud import storage
import tensorflow as tf
from PIL import Image
import numpy as np
import io

BUCKET_NAME = "pdc-models-europe-west1"
class_names = ["Early Blight", "Late Blight", "Healthy"]

model = None

app = FastAPI()

def download_blob(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

@app.on_event("startup")
async def load_model():
    global model
    download_blob(BUCKET_NAME, "models/1.keras", "/tmp/1.keras")
    model = tf.keras.models.load_model("/tmp/1.keras")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB").resize((256, 256))
    image = np.array(image) / 255.0
    img_array = tf.expand_dims(image, 0)

    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = float(np.max(predictions[0]))

    return {"class": predicted_class, "confidence": confidence}
