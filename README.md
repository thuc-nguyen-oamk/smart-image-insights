# Smart Image Insights WebApp

## Overview

**Smart Image Insights** is a web application designed to provide users with detailed analysis of their images by leveraging the power of Azure AI Services (formerly Azure Cognitive Services). The app allows users to upload images and receive detailed insights, including image descriptions, tags, categories, and detected objects, all through an intuitive web interface.

## Key Features

- **Simple and Intuitive Interface**: Easy-to-use design for uploading and analyzing images.
- **Azure Integration**: Seamlessly connects to Azure's Computer Vision API for robust image analysis.
- **Detailed Insights**: Provides comprehensive results, including:
  - Image descriptions
  - Tags
  - Categories
  - Detected objects
- **Responsive Design**: Optimized for both desktop and mobile devices.

## Technologies

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **API Integration**: Azure Computer Vision API

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/thuc-nguyen-oamk/smart-image-insights
   cd smart-image-insights/
   ```

2. **Install Dependencies**:
   (Optional for this demo)
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Azure API Credentials**:
   - Create a `.env` file in the root directory of the project.
   - Add your Azure API key and endpoint:
     ```env
     AZURE_COMPUTER_VISION_KEY=your_subscription_key
     AZURE_COMPUTER_VISION_ENDPOINT=your_endpoint_url
     ```

4. **Run the Application**:
   ```bash
   python main.py
   ```

5. Open your browser and navigate to `http://localhost:5000/` to start analyzing images.

---

## How to Use

1. Upload an image via the "Choose File" button on the homepage.
2. Click "Analyze Image" to send the image for analysis.
3. View the detailed analysis results, including descriptions, tags, categories, and detected objects.
4. To analyze another image, use the "Analyze Another Image" button to reset the page.

---

## Project Structure

```
smart-image-insights/
├── main.py
├── .env
├── static/
│   ├── styles.css
│   └── uploads/
├── templates/
│   ├── home.html
│   └── analysis.html
└── requirements.txt
```

- **`main.py`**: The core Flask application file.
- **`.env`**: Stores Azure API credentials (ignored by Git for security).
- **`requirements.txt`**: Lists all Python dependencies.
- **`static/`**: Contains static files like CSS and uploaded images.
- **`templates/`**: HTML templates for rendering the web pages.

---

## Contribution Guidelines

We welcome contributions to the **Smart Image Insights** project! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Submit a Pull Request for review.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- [Azure AI Services (Computer Vision API)](https://azure.microsoft.com/en-us/services/cognitive-services/)
- [Flask Framework](https://flask.palletsprojects.com/)

---
