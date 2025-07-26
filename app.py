import streamlit as st
import pandas as pd
import seaborn as sns
import time


# --- Create a container for logs ---
log_container = st.expander("View Processing Logs", expanded=False)

# --- Decorator ---
def log_decorator(func):
    def wrapper(x):
        start = time.time()
        result = func(x)
        elapsed = time.time() - start
        with log_container:
            st.write(f"[LOG] {func.__name__}({x}) → {result} in {elapsed:.4f}s")
        return result
    return wrapper

# --- Closure to track how many times it's been called ---
def make_transform_callback(transform_fn):
    count = 0

    @log_decorator
    def callback(x):
        nonlocal count
        count += 1
        with log_container:
            st.write(f"[STATE] Processed row #{count}")
        return transform_fn(x)

    return callback

# --- Load real data ---
@st.cache_data
def load_data():
    df = sns.load_dataset('titanic')  # Using seaborn's Titanic dataset
    return df[['age', 'fare']].dropna()

df = load_data()
st.title("🚢 Titanic Mini Data Pipeline")

# --- Define transformation ---
def scale_value(x):
    return x / 100  # simple normalization

# --- Create callback with closure and decorator ---
transform = make_transform_callback(scale_value)

# --- Apply transformation to both columns ---
df['age_scaled'] = df['age'].apply(transform)
df['fare_scaled'] = df['fare'].apply(transform)

# --- Show result ---
st.subheader("🔍 Sample Processed Data")
st.dataframe(df.head())

st.subheader("📈 Age vs Fare (Scaled)")
st.line_chart(df[['age_scaled', 'fare_scaled']])
