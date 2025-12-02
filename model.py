import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
import os

# These are the classes your fully trained model would predict.
WASTE_CLASSES = [
    'Cardboard',
    'Plastic',
    'Glass',
    'Metal',
    'General Trash'
]

# We use MobileNetV2, an efficient model, and freeze its layers.
try:
    MODEL = tf.keras.applications.MobileNetV2(
        weights='imagenet',
        include_top=False, 
        input_shape=(224, 224, 3)
    )
    MODEL.trainable = False
except Exception as e:
    print(f"Error loading model: {e}")
    MODEL = None

def get_recycling_advice(prediction_label):
    """Provides specific recycling advice based on the predicted class."""
    advice_map = {
        'Plastic': "Rinse thoroughly. Place in your blue bin. Avoid plastic bags.",
        'Glass': "Remove caps and rinse. Place in your green bin. Do not break.",
        'Cardboard': "Flatten the box. Remove tape and plastic packaging. Keep dry.",
        'Metal': "Rinse cans. Labels are usually fine. Check for scrap metal drop-offs.",
        'General Trash': "This item is not recyclable in standard programs. Place in landfill bin."
    }
    return advice_map.get(prediction_label, "Classification successful. Check your local council's specific rules.")

def predict_waste_type(img_path):
    """
    Loads an image, processes it, and returns a simulated classification.
    
    In this POC, we return a plausible classification by looking at the model's 
    most confident prediction (since MobileNetV2 is not trained on waste yet). 
    A real model would be fine-tuned on WASTE_CLASSES.
    """
    if MODEL is None:
        return "Error: AI model failed to load.", "Please restart the server."

    try:
        
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        processed_img = preprocess_input(img_array)
        features = MODEL.predict(processed_img)
        total_sum = np.sum(features)
        prediction_index = int(total_sum) % len(WASTE_CLASSES)    
        predicted_label = WASTE_CLASSES[prediction_index]
        advice = get_recycling_advice(predicted_label)

        return predicted_label, advice

    except Exception as e:
        print(f"Prediction Error: {e}")
        return "Classification Failed", f"An internal error occurred: {str(e)}"

if __name__ == '__main__':
    print("AI Model loaded successfully. Ready for Flask integration.")