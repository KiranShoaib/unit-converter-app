import streamlit as st

st.set_page_config(page_title="🔄 Unit Convertor", layout="centered")
st.markdown("""
    <style>
        .stTextInput, .stSelectbox, .stNumberInput {
            text-align: center;
        }
        .formula-box {
            background-color: #f8f9fa;
            padding: 10px;
            border-radius: 5px;
            border-left: 4px solid #ff9800;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔄 Unit Convertor")
st.write("Convert between different units easily!")

# Unit dictionaries
length_units = {"meter": 1, "kilometer": 1000, "centimeter": 0.01, "mile": 1609.34, "yard": 0.9144, "foot": 0.3048}
weight_units = {"kilogram": 1, "gram": 0.001, "pound": 0.453592, "ounce": 0.0283495}
area_units = {"square meter": 1, "square kilometer": 1e6, "square mile": 2.59e6, "acre": 4046.86, "hectare": 10000}
time_units = {"seconds": 1, "minutes": 60, "hours": 3600, "days": 86400, "weeks": 604800}
speed_units = {"km/h": 1, "mph": 1.60934, "m/s": 3.6, "knots": 1.852}
volume_units = {"liter": 1, "milliliter": 0.001, "gallon": 3.78541, "cup": 0.24, "tablespoon":  0.0147868, "teaspoon": 0.00492892}

def convert(value, from_unit, to_unit, unit_dict):
    if from_unit == to_unit:
        return value, "1 (no conversion needed)"
    factor = unit_dict[from_unit] / unit_dict[to_unit]
    return value * factor, f"Multiply by {factor:.5f}"

def temperature_converter(value, from_unit, to_unit):
    conversions = {
        ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
        ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
        ("Celsius", "Kelvin"): lambda x: x + 273.15,
        ("Kelvin", "Celsius"): lambda x: x - 273.15,
        ("Fahrenheit", "Kelvin"): lambda x: ((x - 32) * 5/9) + 273.15,
        ("Kelvin", "Fahrenheit"): lambda x: ((x - 273.15) * 9/5) + 32,
    }
    formula_text = "Custom formula applies"
    return conversions.get((from_unit, to_unit), lambda x: x)(value), formula_text

st.subheader("📏 Unit Convertor")
unit_type = st.selectbox("Select Unit Type", ["Length", "Weight", "Temperature", "Area", "Time", "Speed", "Volume"])
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

unit_dicts = {
    "Length": length_units, "Weight": weight_units, "Area": area_units,
    "Time": time_units, "Speed": speed_units, "Volume": volume_units
}

col1, col2, col3 = st.columns([3, 1, 3])
with col1:
    if unit_type in unit_dicts:
        from_unit = st.selectbox("From", list(unit_dicts[unit_type].keys()))
    elif unit_type == "Temperature":
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])

with col3:
    result = ""
    formula_text = ""
    if unit_type in unit_dicts:
        to_unit = st.selectbox("To", list(unit_dicts[unit_type].keys()))
    elif unit_type == "Temperature":
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    
    if st.button("Convert"):
        if unit_type in unit_dicts:
            result, formula_text = convert(value, from_unit, to_unit, unit_dicts[unit_type])
        elif unit_type == "Temperature":
            result, formula_text = temperature_converter(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.5f} {to_unit}")

st.markdown(f'<div class="formula-box">🔢 Formula: {formula_text}</div>', unsafe_allow_html=True)
