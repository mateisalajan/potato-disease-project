from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from keras.src.export import TFSMLayer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Later replace * with your frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MODEL = TFSMLayer("../saved_models/1", call_endpoint="serving_default")
MODEL = tf.keras.models.load_model("../saved_models/1.keras")
CLASS_NAMES = ["Early Blight","Late Blight","Healthy"]

@app.get("/")
async def ping():
    return "Hello Sir"


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.post("/predict")
async def predict(
        file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    # image = image.astype(np.float32) / 255.0 # For TFSMLayer
    img_batch = np.expand_dims(image, 0 )
    prediction = MODEL.predict(img_batch)
    # prediction = MODEL(img_batch, training=False) # For TFSMLayer

    # output = prediction['output_0'] # because the prediction with TFSMLayer look like
    # Prediction: {'output_0': <tf.Tensor: shape=(1, 3), dtype=float32, numpy=array([[0.37526917, 0.20424291, 0.42048794]], dtype=float32)>}

    predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = float(np.max(prediction[0]))

    # predicted_class = CLASS_NAMES[np.argmax(output[0])] # For TFSMLayer
    # confidence = float(np.max(output[0])) # For TFSMLayer

    return {'class': predicted_class, 'confidence': confidence}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
    # uvicorn.run(app, host='localhost', port=8001)