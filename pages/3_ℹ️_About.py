import streamlit as st



st.write("""
**About This App**

This tool is designed to help users predict mushroom characteristics based on various attributes. Using machine learning, the app analyzes features like cap diameter, cap shape, gill attachment, gill color, stem height, stem width, stem color, and ring type to make predictions about mushrooms.

**How It Works:**
This app leverages a trained machine learning model, which was built using a dataset of mushroom characteristics. The prediction process involves several steps, including data preprocessing (encoding categorical features, scaling numerical inputs) and then feeding this data into a Random Forest model for predictions.

**Features:**
- Input fields to enter mushroom characteristics, such as cap diameter, stem height, and other visual features.
- The app preprocesses user inputs and applies scaling and encoding to ensure accurate predictions.
- Outputs the prediction results in an easy-to-understand format.

**Note:** This app is intended for educational and experimental purposes, allowing users to explore how machine learning models can predict mushroom characteristics. Always handle mushrooms with caution in real-world scenarios!
""")

