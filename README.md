<!--

ECO-LENS: AI WASTE CLASSIFIER - PROFESSIONAL README Updated to use HTML tables for guaranteed rendering and professional look.

-->

<h1 align="center">♻️ EcoLens: AI Waste Audit & Recycling Advisor 🔍</h1>

<p align="center">
<img src="[https://www.google.com/search?q=https://img.shields.io/badge/Status-MVP%2520Complete%2520(90%2520Min%2520Execution)-brightgreen%3Fstyle%3Dfor-the-badge" alt="Status Badge](https://img.freepik.com/premium-vector/green-badge-with-shield-check-mark-right-mark-with-protect-shield-shield-with-check-mark-vector-illustration_561158-4159.jpg)"/>
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Tech-Python%2520%257C%2520TensorFlow%2520%257C%2520Flask%2520%257C%2520HTML%252FCSS-0077B6%3Fstyle%3Dfor-the-badge%26logo%3Dpython" alt="Tech Stack Badge"/>
</p>

<p align="center">
<strong>The fast, effective solution to recycling contamination, leveraging Computer Vision.</strong>
</p>

🚀 Executive Summary: The Recruiter Pitch

EcoLens is a full-stack Proof-of-Concept (POC) application that solves a critical social and environmental problem: recycling contamination.

Instead of relying on outdated static lookup tables, EcoLens uses Artificial Intelligence (Computer Vision) to instantly classify uploaded images of waste (e.g., plastic, cardboard, general trash) and provide localized disposal guidance.

This project demonstrates proficiency in:

AI/ML Pipeline Development: From model loading (MobileNetV2) to prediction serving.

Full-Stack Engineering: Integrating a Python ML backend (Flask) with a modern web frontend (HTML/CSS).

Problem-Solving & Speed: Rapid development, achieving a functional MVP in under 90 minutes.

🌍 The Problem: Contamination Crisis

Recycling facility operations are severely hampered by incorrect sorting. When non-recyclable materials are placed in the wrong bins, entire batches can be contaminated, forcing valuable recyclables into landfills. This inefficiency increases operational costs and reduces the environmental impact of recycling efforts.

✨ The Solution: EcoLens

EcoLens provides an intuitive, user-friendly interface to ensure items are recycled correctly, every time.

<table width="100%">
<thead>
<tr>
<th width="30%">Feature</th>
<th width="40%">Impact</th>
<th width="30%">Technology Showcase</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Real-Time Classification</strong></td>
<td>Users get instant feedback by simply uploading a photo.</td>
<td>Python, TensorFlow/Keras, Image Preprocessing.</td>
</tr>
<tr>
<td><strong>Accurate Disposal Advice</strong></td>
<td>Provides clear, step-by-step instructions specific to the material type.</td>
<td>Flask Backend Logic, Custom Classification Mappings.</td>
</tr>
<tr>
<td><strong>Rapid Feedback Loop</strong></td>
<td>High-speed response time, crucial for consumer application usability.</td>
<td>Optimized MobileNetV2 architecture.</td>
</tr>
</tbody>
</table>

🛠 Technical Architecture

EcoLens is built around a scalable microservice architecture, allowing the AI and Web components to operate independently.

Tech Stack

<table width="100%">
<thead>
<tr>
<th width="20%">Component</th>
<th width="20%">Technology</th>
<th width="60%">Role</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>AI Model</strong></td>
<td><strong>TensorFlow / Keras</strong></td>
<td>Core machine learning library. Uses the efficient <strong>MobileNetV2</strong> architecture (simulated transfer learning) for rapid deployment.</td>
</tr>
<tr>
<td><strong>Backend API</strong></td>
<td><strong>Flask (Python)</strong></td>
<td>Lightweight framework responsible for handling HTTP requests, file uploads, and calling the AI prediction module.</td>
</tr>
<tr>
<td><strong>Frontend</strong></td>
<td><strong>HTML, CSS, Jinja2</strong></td>
<td>Simple, clean, and responsive user interface for image submission and display of results.</td>
</tr>
</tbody>
</table>

⚡ 90-Minute Execution: From Concept to MVP

This project was developed under a strict 90-minute time constraint to showcase rapid prototyping and efficient pipeline construction. The focus was on architectural integrity and demonstrating the complete AI workflow, rather than exhaustive training.

Phase

Duration

Achievement

Phase 1: AI Logic & Setup

30 min

Environment setup, integration of MobileNetV2, and creation of the predict_waste_type function with simulation logic.

Phase 2: Flask API Development

30 min

Creation of app.py, implementing secure file upload handling, and API routing to link the web request to the AI model.

Phase 3: Frontend & Deployment

30 min

Design of a clean, responsive index.html interface and successful server launch (POC delivered).

This execution demonstrates an ability to rapidly deliver a functional product and integrate cutting-edge technologies under pressure.

⚙️ Quick Start (Local Installation)

To run EcoLens locally:

Clone the Repository:

git clone [https://github.com/YOUR_USERNAME/EcoLens-AI-Waste-Advisor.git](https://github.com/YOUR_USERNAME/EcoLens-AI-Waste-Advisor.git)
cd EcoLens-AI-Waste-Advisor


Setup Environment & Dependencies:

python3 -m venv venv
source venv/bin/activate  # Use `venv\Scripts\activate` on Windows
pip install flask numpy tensorflow


Run the Application:

python app.py


The app will be accessible at http://127.0.0.1:5000/

Test: Upload an image (e.g., a photo of a bottle, paper, or box) and observe the AI classification and advice.
