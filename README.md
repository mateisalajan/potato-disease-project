
Potato Disease Detection Project

This project aims to detect and classify potato plant diseases using machine learning algorithms. It provides an easy-to-use interface for farmers and agriculture professionals to diagnose and manage potato plant health. The system is built using Python, TensorFlow (for machine learning), and FastAPI for backend, with a React frontend.

Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Deployment](#deployment) (To be added)

Introduction

Potato plants are vital for food security, but they are susceptible to a variety of diseases. This project focuses on the development of a system that can identify diseases in potato plants using images of their leaves. The goal is to assist farmers in early detection, allowing for more effective treatment and better yield.

Features
- Disease Detection: Upload an image of the potato leaf, and the system will classify it as one of several common potato diseases.
- Web Interface: A user-friendly React frontend where users can interact with the application.
- Machine Learning Model: A deep learning model trained to recognize different potato diseases.
- API Integration: FastAPI serves as the backend to handle requests and serve the model for disease prediction.

Tech Stack

- Frontend: React.js
- Backend: FastAPI
- Machine Learning: TensorFlow, Keras
- Version Control: Git, GitHub

Setup and Installation

To run the Potato Disease Detection project locally, follow these steps:

Prerequisites
- Install Python 3.8 or higher
- Install Node.js and npm
- Install Docker (for containerization, optional)
- Install Git

Clone the Repository

Clone the project to your local machine:

```bash
git clone https://github.com/mateisalajan/potato-disease-project.git
cd potato-disease-project
```

Backend Setup (FastAPI)

1. Navigate to the `api` directory:
   ```bash
   cd api
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

   The API will be running at `http://127.0.0.1:8000`.

Frontend Setup (React)

1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Install the required npm dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

   The frontend will be running at `http://localhost:3000`.

Usage

1. Open your web browser and go to `http://localhost:3000` (for the frontend).
2. Upload a potato leaf image to the system.
3. The system will classify the disease and show the results.

Contributing

We welcome contributions to the Potato Disease Detection project! If you'd like to contribute, please fork the repository and create a pull request with your changes. Before contributing, ensure that the code works as expected and passes all tests.

Steps to contribute:
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test your changes.
5. Push the changes to your fork.
6. Create a pull request to the main repository.

License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Deployment

To be added once the deployment feature is implemented.
