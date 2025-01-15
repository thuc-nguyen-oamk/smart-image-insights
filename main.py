from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from flask import Flask, render_template, request, url_for
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv
import os, uuid

# Load environment variables
load_dotenv()

# Initialize Flask app
smart_image_insights = Flask(__name__)

# Azure credentials setup
azure_api_key = os.getenv('AZURE_COMPUTER_VISION_KEY')
azure_endpoint_url = os.getenv('AZURE_COMPUTER_VISION_ENDPOINT')

# Initialize Azure Computer Vision client
azure_vision_client = ComputerVisionClient(
    azure_endpoint_url,
    CognitiveServicesCredentials(azure_api_key)
)

def process_image(image_filepath):
    """Analyze the uploaded image using Azure Computer Vision API."""
    analysis_features = [
        VisualFeatureTypes.description,
        VisualFeatureTypes.tags,
        VisualFeatureTypes.categories,
        VisualFeatureTypes.objects
    ]
    
    with open(image_filepath, "rb") as image_data:
        analysis_results = azure_vision_client.analyze_image_in_stream(
            image_data, visual_features=analysis_features
        )
    
    image_analysis = {
        "description": analysis_results.description.captions[0].text if analysis_results.description.captions else "",
        "tags": [{"name": tag.name, "confidence": f"{tag.confidence:.2f}"} for tag in analysis_results.tags],
        "categories": [{"name": category.name, "confidence": f"{category.score:.2f}"} for category in analysis_results.categories],
        "objects": [{"name": detected_object.object_property, "confidence": f"{detected_object.confidence:.2f}"} for detected_object in analysis_results.objects]
    }
    
    return image_analysis

@smart_image_insights.route('/', methods=['GET', 'POST'])
def home_page():
    """Handle the main page where users can upload and analyze images."""
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('home.html', error='No file provided.')
        
        uploaded_file = request.files['file']
        
        if uploaded_file.filename == '':
            return render_template('home.html', error='No file selected.')
        
        if uploaded_file:
            # Generate a unique filename for the uploaded image
            unique_filename = f"{uuid.uuid4()}{os.path.splitext(uploaded_file.filename)[1]}"
            upload_path = os.path.join('static', 'uploads', unique_filename)
            uploaded_file.save(upload_path)
            
            # Analyze the image
            analysis_results = process_image(upload_path)
            
            return render_template(
                'analysis.html',
                image_url=url_for('static', filename=f'uploads/{unique_filename}'),
                analysis=analysis_results
            )
    
    return render_template('home.html')

if __name__ == '__main__':
    # Ensure the upload directory exists
    os.makedirs(os.path.join('static', 'uploads'), exist_ok=True)
    smart_image_insights.run(debug=True)
