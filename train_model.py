import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle

# ✅ Load your CSV file
df = pd.read_csv(r"C:\Users\Asus Laptop\OneDrive\Desktop\Tecnobijproject\Rainfall_Detection2017_2023\Rainfall_Data_2017_2023.csv")

# ✅ Clean column names
df.columns = df.columns.str.strip()
df["State/UT"] = df["State/UT"].str.strip().str.upper()
df["District"] = df["District"].str.strip().str.upper()

# ✅ Encode states and districts
states = sorted(df["State/UT"].unique())
districts = sorted(df["District"].unique())

state_encoder = {state: idx for idx, state in enumerate(states)}
district_encoder = {dist: idx for idx, dist in enumerate(districts)}

# ✅ Create encoded features
df["state_encoded"] = df["State/UT"].map(state_encoder)
df["district_encoded"] = df["District"].map(district_encoder)

# ✅ Example target variable (replace with your actual target column)
# Here, we just make up a dummy target for example
df["target"] = np.random.uniform(100, 500, size=len(df))

# ✅ Create dummy features
df["year"] = 2023
dummy_features = pd.DataFrame(np.zeros((len(df), 15)), columns=[f"f{i}" for i in range(15)])

# ✅ Final feature set
X = pd.concat([df[["state_encoded", "district_encoded", "year"]], dummy_features], axis=1)
y = df["target"]

# ✅ Train model
model = RandomForestRegressor()
model.fit(X, y)

# ✅ Save model
with open(r"C:\Users\Asus Laptop\OneDrive\Desktop\Tecnobijproject\Rainfall_Detection2017_2023\models\rainfall_monthly_model.pkl", "wb") as f:
    pickle.dump(model, f)

# ✅ Save encoders
with open(r"C:\Users\Asus Laptop\OneDrive\Desktop\Tecnobijproject\Rainfall_Detection2017_2023\models\state_encoder.pkl", "wb") as f:
    pickle.dump(np.array(states), f)

with open(r"C:\Users\Asus Laptop\OneDrive\Desktop\Tecnobijproject\Rainfall_Detection2017_2023\models\district_encoder.pkl", "wb") as f:
    pickle.dump(np.array(districts), f)

print("✅ Model and encoders saved successfully.")
