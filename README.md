# 🚗 Car Price Prediction – CarDekho Dataset (with Streamlit)

Hey there! Welcome to my car price playground 😎

Now you don't just train models — you can predict car prices live with a click of a button thanks to Streamlit.

## 🔹 What's Inside

### Data Exploration (EDA)
Checked out trends, distributions, and correlations — because guessing a car's price blindly is boring.

### Preprocessing
- Numeric columns scaled with `StandardScaler`
- Categorical columns one-hot encoded
- Wrapped in a Pipeline so preprocessing + prediction is smooth

### Models Tried
- **Linear Regression** → simple baseline
- **Random Forest Regressor** → handles non-linear patterns like a champ

### Streamlit App
- Input features live: brand, model, fuel type, transmission, etc.
- Get instant predicted price
- Interactive sliders for numeric inputs and dropdowns for categorical

## 🔹 How to Run

### 1. Clone the repo:
```bash
git clone https://github.com/donxav/CarPre.git
cd car-price-prediction
```

### 2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Train the model:
```bash
python train_model.py
```

### 5. Run the Streamlit app:
```bash
streamlit run app.py
```

### 6. Open your browser:
Navigate to `http://localhost:8501` and start predicting! 🚀

## 📦 Requirements

```txt
pandas
numpy
scikit-learn
streamlit
joblib
matplotlib
seaborn
```

## 📊 Dataset

The dataset contains car details including:
- Brand and model
- Vehicle age
- Kilometers driven
- Seller type
- Fuel type
- Transmission type
- Mileage
- Engine capacity
- Max power
- Number of seats
- Selling price (target)

## 🎯 Model Performance

- **Linear Regression**: Baseline model
- **Random Forest**: Best performance with R² score on test set

## 🖼️ Screenshots

![Home page](image.png)
!![trial](image-2.png)
![predicted](image-1.png)


## 🤝 Contributing

Feel free to fork this repo and submit pull requests. All contributions are welcome!

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/donxav)
- LinkedIn: [Your Name](https://linkedin.com/in/don-xavier72)

---

Made with ❤️ and lots of ☕