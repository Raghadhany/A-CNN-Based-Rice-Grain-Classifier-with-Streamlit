# A-CNN-Based-Rice-Grain-Classifier-with-Streamlit
A web-based image classifier built with Streamlit and TensorFlow to detect and classify different types of rice grains using a trained Convolutional Neural Network.

# 🌾 RiceGrainNet: A CNN-Based Rice Grain Classifier with Streamlit

RiceGrainNet is an interactive web app built using Streamlit and a Convolutional Neural Network (CNN) model. It allows users to upload an image of a rice grain and classifies it into one of several predefined types such as Arborio, Basmati, Jasmine, Karacadag, or Ipsala.

---

## 📌 Features

- 📷 Upload rice grain images (JPEG, PNG)
- ⚙️ Preprocess images (grayscale conversion and resizing)
- 🤖 Predict rice type using a trained CNN model
- 🧠 Five-class classification:  
  - Arborio  
  - Basmati  
  - Jasmine  
  - Karacadag  
  - Ipsala
- ✅ Real-time predictions via a user-friendly web interface

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.7+
- TensorFlow
- Streamlit
- NumPy

### 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ricegrainnet.git
   cd ricegrainnet
2. Install dependencies:
   pip install -r requirements.txt

3.Run the app:
  streamlit run finalnueral.py

Make sure to update the model path in finalnueral.py with the correct relative or absolute path to your rice_cnn_model.h5 file.
