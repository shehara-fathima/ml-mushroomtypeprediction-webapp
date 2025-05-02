import streamlit as st
import numpy as np
import pickle


# Load pre-trained model, encoder, and scaler
with open('model.sav', 'rb') as model_file:
    model = pickle.load(model_file)
with open('encoder.sav', 'rb') as encoder_file:
    encoder = pickle.load(encoder_file)
with open('scaler.sav', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Define options for each categorical feature with descriptive labels
# Cap Shape Options
cap_shape_options = {
    'x': 'Convex',
    'f': 'Flat',
    'p': 'Bell',
    'b': 'Bulbous',
    'c': 'Cone',
    's': 'Sunken',
    'o': 'Oval'
}

# Gill Attachment Options
gill_attachment_options = {
    'e': 'Free',
    'a': 'Attached',
    'd': 'Descending',
    's': 'Subdecurrent',
    'x': 'Mixed',
    'p': 'Partial',
    'f': 'Fused'
}

# Gill Color Options
gill_color_options = {
    'w': 'White',
    'n': 'Brown',
    'p': 'Pink',
    'u': 'Purple',
    'b': 'Black',
    'g': 'Gray',
    'y': 'Yellow',
    'r': 'Red',
    'e': 'Beige',
    'o': 'Orange',
    'k': 'Dark Brown',
    'f': 'Buff'
}

# Stem Color Options
stem_color_options = {
    'w': 'White',
    'y': 'Yellow',
    'n': 'Brown',
    'u': 'Purple',
    'b': 'Black',
    'l': 'Blue',
    'r': 'Red',
    'p': 'Pink',
    'e': 'Beige',
    'k': 'Dark Brown',
    'g': 'Gray',
    'o': 'Orange',
    'f': 'Buff'
}

# Ring Type Options
ring_type_options = {
    'g': 'Grooved',
    'p': 'Pendant',
    'e': 'Evanescent',
    'l': 'Large',
    'f': 'Flaring',
    'm': 'Membranous',
    'r': 'Ringed',
    'z': 'Zone'
}



# Reverse mapping for descriptive labels to single-character codes
cap_shape_map = {v: k for k, v in cap_shape_options.items()}
gill_attachment_map = {v: k for k, v in gill_attachment_options.items()}
gill_color_map = {v: k for k, v in gill_color_options.items()}
stem_color_map = {v: k for k, v in stem_color_options.items()}
ring_type_map = {v: k for k, v in ring_type_options.items()}

# Streamlit app layout
st.title("Let's check!")

# Input for numeric features
cap_diameter = st.number_input('Cap Diameter (cm)', min_value=0.0)
stem_height = st.number_input('Stem Height (cm)', min_value=0.0)
stem_width = st.number_input('Stem Width (cm)', min_value=0.0)

# Dropdowns for categorical features with descriptive labels
cap_shape = st.selectbox('Cap Shape', options=cap_shape_options.values())
gill_attachment = st.selectbox('Gill Attachment', options=gill_attachment_options.values())
gill_color = st.selectbox('Gill Color', options=gill_color_options.values())
stem_color = st.selectbox('Stem Color', options=stem_color_options.values())
ring_type = st.selectbox('Ring Type', options=ring_type_options.values())

# List of features, containing both categorical and numeric
features = [cap_diameter, stem_height, stem_width, cap_shape, gill_attachment, gill_color, stem_color, ring_type]

# List to store the transformed (encoded/scaled) features
encoded_features = []

for feature in features:
    # Check if the feature is categorical (assuming categorical features are strings)
    if isinstance(feature, str):
        if feature in encoder.classes_:
            # Encode the categorical feature
            encoded_feature = encoder.transform([feature])[0]  # Retrieve the encoded value
        else:
            # Handle unseen labels by setting to a default or raising an error
            print(f"Warning: Unseen label '{feature}' encountered. Setting to default value.")
            encoded_feature = encoder.transform([encoder.classes_[0]])[0]  # Use the first known class as default
    else:
        # Directly add numeric features without encoding
        encoded_feature = feature

    # Append encoded feature (numeric or encoded categorical)
    encoded_features.append(encoded_feature)

# Convert encoded_features to a 2D array to pass to the scaler
encoded_features = [encoded_features]  # Make it a 2D array with one sample
features_final = scaler.transform(encoded_features)

# Button to trigger prediction
pred = st.button('PREDICT')
if pred:
    prediction = model.predict(features_final)
    if prediction == 1:
        st.write('# YOUR MUSHROOM IS POISONOUS')
    else:
        st.write('# YOUR MUSHROOM IS EDIBLE')













