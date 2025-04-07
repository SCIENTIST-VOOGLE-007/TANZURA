
---

### 🌊 **TANZURA: Microplastic Detection Platform**

```markdown
# TANZURA 🌊 Microplastic Detection Platform

> Safeguarding water, pixel by pixel.
```
## 💡 Overview

TANZURA is a FastAPI-powered web app that uses deep learning to detect microplastics in water. Built on U-Net architecture, it provides actionable health safety insights by classifying water into risk levels: Safe, Moderate, or High.

## 🔍 Features

- 🔬 U-Net model for semantic segmentation of microplastic particles.
- 🚦 Risk Classification System:
  - **Safe**: Minimal contamination
  - **Moderate**: Use with caution
  - **High**: Unsafe for consumption
- 🌐 FastAPI for efficient backend performance.
- 🧪 OpenCV-based preprocessing of microscopic water sample images.
- 🗂️ MongoDB for storing and retrieving historical test data.

## 🔧 Tech Stack

- **Model**: U-Net (Keras/PyTorch)
- **Backend**: FastAPI, Python
- **Image Processing**: OpenCV
- **Database**: MongoDB

## 📦 Installation
```bash
git clone https://github.com/your-username/TANZURA.git
cd TANZURA
pip install -r requirements.txt
```

🚀 Usage
Start the FastAPI server:

```bash
uvicorn app:app --reload
Upload a microscopic image of water.
```

Get real-time microplastic analysis with risk level prediction.

🧠 Model Info
Architecture: U-Net
Accuracy: 80% on test data
Input: 256x256 grayscale microscopic images
Output: Mask highlighting microplastic regions

📊 Example Input
Upload sample images in PNG or JPG format:
/samples/sample1.jpg
/samples/sample2.jpg


🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request with clear commit messages.
