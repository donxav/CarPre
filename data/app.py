import streamlit as st
import pandas as pd
import joblib
import os

# Page configuration
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Car Price Prediction App")
st.markdown("---")

# Load the complete pipeline (recommended approach)
try:
    if os.path.exists('car_price_pipeline.pkl'):
        # Load complete pipeline
        pipeline = joblib.load('car_price_pipeline.pkl')
        st.success("✅ Model loaded successfully!")
        use_pipeline = True
    elif os.path.exists('car_rf_model.pkl') and os.path.exists('preprocessor.pkl'):
        # Load separate files
        model = joblib.load('car_rf_model.pkl')
        preprocessor = joblib.load('preprocessor.pkl')
        st.success("✅ Model and preprocessor loaded successfully!")
        use_pipeline = False
    else:
        st.error("⚠️ Model files not found! Please train the model first.")
        st.stop()
        
except Exception as e:
    st.error(f"Error loading model: {str(e)}")
    st.stop()

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Basic Details")
    
    # Based on your dataset, get unique values or use common options
    brand = st.selectbox("Brand", 
        ['Maruti', 'Hyundai', 'Ford', 'Honda', 'Toyota', 'Tata', 'Mahindra', 
         'Renault', 'Chevrolet', 'Volkswagen', 'Nissan', 'Skoda'])
    
    model_name = st.text_input("Model", placeholder="e.g., Alto, i20, Ecosport")
    
    seller_type = st.selectbox("Seller Type", ['Individual', 'Dealer', 'Trustmark Dealer'])
    
    fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
    
    transmission_type = st.selectbox("Transmission Type", ['Manual', 'Automatic'])

with col2:
    st.subheader("🔧 Technical Specifications")
    
    vehicle_age = st.slider("Vehicle Age (years)", 0, 25, 5)
    
    km_driven = st.number_input("Kilometers Driven", 
                                 min_value=0, 
                                 max_value=500000, 
                                 value=20000, 
                                 step=5000)
    
    mileage = st.number_input("Mileage (kmpl)", 
                              min_value=5.0, 
                              max_value=50.0, 
                              value=19.0, 
                              step=0.5)
    
    engine = st.number_input("Engine (CC)", 
                            min_value=600, 
                            max_value=5000, 
                            value=1197, 
                            step=100)
    
    max_power = st.number_input("Max Power (bhp)", 
                                min_value=30.0, 
                                max_value=400.0, 
                                value=80.0, 
                                step=5.0)
    
    seats = st.selectbox("Number of Seats", [2, 4, 5, 6, 7, 8, 9, 10], index=2)

st.markdown("---")

# Prediction button
col_button, col_empty = st.columns([1, 3])
with col_button:
    predict_button = st.button("🔮 Predict Price", type="primary", use_container_width=True)

if predict_button:
    # Validate inputs
    if not model_name:
        st.warning("⚠️ Please enter a model name!")
    else:
        try:
            # Create input dataframe with EXACT column order from training
            input_data = {
                'brand': [brand],
                'model': [model_name],
                'vehicle_age': [vehicle_age],
                'km_driven': [km_driven],
                'seller_type': [seller_type],
                'fuel_type': [fuel_type],
                'transmission_type': [transmission_type],
                'mileage': [mileage],
                'engine': [engine],
                'max_power': [max_power],
                'seats': [seats]
            }
            
            input_df = pd.DataFrame(input_data)
            
            # Make prediction
            with st.spinner('Calculating price...'):
                if use_pipeline:
                    prediction = pipeline.predict(input_df)[0]
                else:
                    transformed_input = preprocessor.transform(input_df)
                    prediction = model.predict(transformed_input)[0]
            
            # Display result
            st.markdown("---")
            st.balloons()
            
            result_col1, result_col2, result_col3 = st.columns([1, 2, 1])
            with result_col2:
                st.success("### 💰 Estimated Selling Price")
                st.markdown(f"# ₹ {prediction:,.0f}")
                
                # Additional insights
                lower_bound = prediction * 0.9
                upper_bound = prediction * 1.1
                
                st.info(f"""
                **Price Range Estimate:**
                - Lower estimate: ₹ {lower_bound:,.0f}
                - Upper estimate: ₹ {upper_bound:,.0f}
                
                *Note: Actual price may vary based on vehicle condition and market factors*
                """)
                
                # Show input summary
                with st.expander("📝 Input Summary"):
                    st.write(input_df)
            
        except Exception as e:
            st.error(f"❌ Error making prediction: {str(e)}")
            st.info("Please check if all input values are valid.")
            st.code(str(e))

# Add footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>Built with ❤️ using Streamlit | Model: Random Forest Regressor</p>
</div>
""", unsafe_allow_html=True)