import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image

# Load model
model = load_model('plant_disease_model.h5')

# Class names (ADD ALL YOUR 38 CLASSES HERE)
class_names = [
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___healthy"
    "Apple___Apple_scab", 
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew", 
    "Cherry_(including_sour)___healthy", 
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot", 
    "Corn_(maize)___Common_rust_", 
    "Corn_(maize)___Northern_Leaf_Blight", 
    "Corn_(maize)___healthy", 
    "Grape___Black_rot", 
    "Grape___Esca_(Black_Measles)", 
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)", 
    "Grape___healthy", 
    "Orange___Haunglongbing_(Citrus_greening)", 
    "Peach___Bacterial_spot", 
    "Peach___healthy", 
    "Pepper,_bell___Bacterial_spot", 
    "Pepper,_bell___healthy", 
    "Potato___Early_blight", 
    "Potato___Late_blight", 
    "Potato___healthy", 
    "Raspberry___healthy", 
    "Soybean___healthy", 
    "Squash___Powdery_mildew", 
    "Strawberry___Leaf_scorch", 
    "Strawberry___healthy", 
    "Tomato___Bacterial_spot", 
    "Tomato___Leaf_Mold", 
    "Tomato___Septoria_leaf_spot", 
    "Tomato___Spider_mites Two-spotted_spider_mite", 
    "Tomato___Target_Spot", 
    "Tomato___Tomato_mosaic_virus",

]

# Disease info (add more later)
disease_info = {
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "cause": "Virus spread by whiteflies",
        "cure": "Use resistant seeds and control insects"
    },
    "Tomato___Early_blight": {
        "cause": "Fungal infection",
        "cure": "Use fungicide and remove infected leaves"
    },
    "Tomato___Late_blight": {
        "cause": "Water mold (Phytophthora infestans)",
        "cure": "Apply fungicide and avoid excess moisture"
    },
    "Apple___Black_rot": {
        "cause": "Fungal pathogen",
        "cure": "Prune infected parts and apply fungicide"
    },
    "Corn___Common_rust": {
        "cause": "Fungal infection",
        "cure": "Use resistant hybrids and fungicide spray"
    },
    "Potato___Early_blight": {
        "cause": "Fungal infection",
        "cure": "Crop rotation and fungicide use"
    },
    "Potato___healthy": {
        "cause": "No disease",
        "cure": "No treatment required"
    },
    "Tomato___Leaf_Mold": {
        "cause": "Fungal pathogen",
        "cure": "Prune infected parts and apply fungicide"
    },
    
    "Apple___Apple_scab": {
    "cause": "Fungal infection caused by Venturia inaequalis",
    "cure": "Apply fungicides, remove infected leaves, ensure proper air circulation"
    },
    "Apple___Cedar_apple_rust": {
    "cause": "Fungal disease involving cedar and apple trees",
    "cure": "Remove nearby cedar trees and apply fungicide"
    },
    "Apple___healthy": {
    "cause": "No disease",
    "cure": "Maintain proper care and watering"
    },
    "Corn___Cercospora_leaf_spot Gray_leaf_spot": {
    "cause": "Fungal infection due to humid conditions",
    "cure": "Use resistant hybrids and apply fungicide"
    },
    "Corn___Northern_Leaf_Blight": {
    "cause": "Fungal pathogen Exserohilum turcicum",
    "cure": "Crop rotation and fungicide application"
    },
    "Corn___healthy": {
    "cause": "No disease",
    "cure": "Regular monitoring and balanced nutrition"
    },
    "Grape___Black_rot": {
    "cause": "Fungal infection Guignardia bidwellii",
    "cure": "Remove infected parts and apply fungicide"
    },
    "Grape___Esca_(Black_Measles)": {
    "cause": "Fungal disease affecting woody tissue",
    "cure": "Prune infected areas and avoid water stress"
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
    "cause": "Fungal infection",
    "cure": "Apply fungicide and improve air circulation"
    },
    "Grape___healthy": {
    "cause": "No disease",
    "cure": "Maintain vineyard hygiene"
    },
    "Peach___Bacterial_spot": {
    "cause": "Bacteria Xanthomonas campestris",
    "cure": "Use resistant varieties and copper sprays"
    },
    "Peach___healthy": {
    "cause": "No disease",
    "cure": "Proper irrigation and pruning"
    },
    "Pepper,_bell___Bacterial_spot": {
    "cause": "Bacterial infection",
    "cure": "Use disease-free seeds and copper sprays"
    },
    "Pepper,_bell___healthy": {
    "cause": "No disease",
    "cure": "Maintain proper nutrition"
    },
    "Potato___Late_blight": {
    "cause": "Water mold Phytophthora infestans",
    "cure": "Use fungicides and avoid overwatering"
    },
    "Strawberry___Leaf_scorch": {
    "cause": "Fungal infection",
    "cure": "Remove infected leaves and apply fungicide"
    },
    "Strawberry___healthy": {
    "cause": "No disease",
    "cure": "Ensure good air circulation"
    },
    "Tomato___Bacterial_spot": {
    "cause": "Bacterial infection",
    "cure": "Use copper sprays and disease-free seeds"
    },
    "Tomato___Septoria_leaf_spot": {
    "cause": "Fungal infection",
    "cure": "Remove infected leaves and apply fungicide"
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
    "cause": "Pest infestation",
    "cure": "Use neem oil or insecticidal soap"
    },
    "Tomato___Target_Spot": {
    "cause": "Fungal infection",
    "cure": "Apply fungicide and remove affected leaves"
    },
    "Tomato___Tomato_mosaic_virus": {
    "cause": "Viral infection",
    "cure": "Remove infected plants and sanitize tools"
    },
    "Tomato___healthy": {
    "cause": "No disease",
    "cure": "Maintain proper watering and sunlight"
}

}

language = st.selectbox("🌐 Select Language", ["English", "Hindi"])

translations = { 
    "English": { 
        "title": "🌱 PlantPal - Plant Disease Detector", 
        "upload": "Upload a plant leaf image", 
        "disease": "Disease", 
        "cause": "Cause", 
        "cure": "Cure", 
        "confidence": "Confidence" 
    }, 
    "Hindi": { 
        "title": "🌱 प्लांटपाल - पौधों की बीमारी पहचान", 
        "upload": "पौधे की पत्ती की फोटो अपलोड करें", 
        "disease": "बीमारी", 
        "cause": "कारण", 
        "cure": "इलाज", 
        "confidence": "विश्वास स्तर" 
        } 
        } 
text = translations[language]

# UI
st.title(text["title"])
uploaded_file = st.file_uploader(text["upload"], type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = image.load_img(uploaded_file, target_size=(224, 224))
    st.image(img, caption="Uploaded Image", use_container_width=True)

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)
    disease = class_names[predicted_class]

    clean_name = disease.replace("___", " → ").replace("_", " ")
    
    info = disease_info.get(disease, {})
    cause = info.get("cause", "Not available") 
    cure = info.get("cure", "Not available")

    confidence = np.max(prediction) * 100
      

    st.success(f"🌿 Disease: {clean_name}")
    st.info(f"Confidence: {confidence:.2f}%") 

    st.warning(f"{text['cause']}:{cause}")
    st.success(f"{text['cure']}:{cure}")

    
