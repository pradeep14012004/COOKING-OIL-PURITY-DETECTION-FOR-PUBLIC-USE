import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Cooking Oil Purity ML", page_icon="🫗")
st.title("🫗 Cooking Oil Purity — ML Demo")
st.caption("Train a lightweight classifier from your own labelled sensor CSV, then test a sample.")

st.info("Expected columns: ph, turbidity, color, label. Labels can be Pure, Used, or Waste.")

uploaded=st.file_uploader("Upload labelled sensor CSV", type="csv")
model=None
encoder=None
if uploaded:
    df=pd.read_csv(uploaded)
    required={"ph","turbidity","color","label"}
    missing=required-set(df.columns.str.lower())
    if missing:
        st.error("Missing columns: "+", ".join(sorted(missing)))
    else:
        df.columns=[c.lower() for c in df.columns]
        df=df.dropna(subset=list(required))
        encoder=LabelEncoder()
        y=encoder.fit_transform(df["label"].astype(str))
        model=RandomForestClassifier(n_estimators=150,random_state=42)
        model.fit(df[["ph","turbidity","color"]],y)
        st.success(f"Model trained on {len(df)} samples.")
        
st.subheader("Predict an oil sample")
c1,c2,c3=st.columns(3)
ph=c1.number_input("pH",0.0,14.0,7.0)
turb=c2.number_input("Turbidity",0.0,1000.0,10.0)
color=c3.number_input("Color value",0.0,1000.0,100.0)

if st.button("Predict"):
    if model is None:
        st.warning("Upload labelled sensor data first.")
    else:
        pred=model.predict([[ph,turb,color]])[0]
        probs=model.predict_proba([[ph,turb,color]])[0]
        label=encoder.inverse_transform([pred])[0]
        st.metric("Predicted quality",str(label))
        st.write("Class confidence:",round(float(probs.max())*100,2),"%")
