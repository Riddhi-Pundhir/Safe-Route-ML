
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import joblib   

df = pd.read_csv("crime_safety_dataset.csv")
print(df.shape)
print(df.head(3))

df = df.drop(columns=['id', 'victim_age', 'victim_gender', 'victim_race'])


print("Shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()
print("After removing duplicates:", df.shape)
print("\nCrime types in dataset:")
print(df['crime_type'].value_counts())

severity_map = {
    'Homicide': 1.0,
    'Assault': 0.9,
    'Domestic Violence': 0.85,
    'Robbery': 0.8,
    'Arson': 0.7,
    'Burglary': 0.6,
    'Drug Offense': 0.5,
    'Theft': 0.4,
    'Vandalism': 0.3,
    'Fraud': 0.2,
}
df['crime_severity'] = df['crime_type'].map(severity_map).fillna(0.5)
print(df[['crime_type', 'crime_severity']].drop_duplicates().sort_values('crime_severity', ascending=False))

df['hour'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.hour

city_coords = {
    'Philadelphia': (39.9526, -75.1652), 'Phoenix': (33.4484, -112.0740),
    'San Antonio': (29.4241, -98.4936),  'Houston': (29.7604, -95.3698),
    'Chicago': (41.8781, -87.6298),      'Los Angeles': (34.0522, -118.2437),
    'New York': (40.7128, -74.0060),     'Dallas': (32.7767, -96.7970),
}
np.random.seed(42)
df['latitude']  = df['city'].apply(lambda c: city_coords.get(c, (37.09, -95.71))[0] + np.random.uniform(-0.05, 0.05))
df['longitude'] = df['city'].apply(lambda c: city_coords.get(c, (37.09, -95.71))[1] + np.random.uniform(-0.05, 0.05))

df['lighting_level'] = df['hour'].apply(lambda h: round(np.random.uniform(0.6, 1.0), 2) if 6 <= h <= 19 else round(np.random.uniform(0.0, 0.4), 2))
df['crowd_density']  = df['hour'].apply(lambda h: round(np.random.uniform(0.4, 1.0), 2) if 8 <= h <= 20 else round(np.random.uniform(0.0, 0.35), 2))


def hour_risk(h):
    if h <= 5: return 1.0
    elif h <= 8: return 0.4
    elif h <= 17: return 0.2
    elif h <= 21: return 0.5
    else: return 0.8

df['hour_risk'] = df['hour'].apply(hour_risk)
df['risk_score'] = (
    0.50 * df['crime_severity'] +
    0.25 * (1 - df['lighting_level']) +
    0.15 * (1 - df['crowd_density']) +
    0.10 * df['hour_risk']
).round(4)
print(df['risk_score'].describe())

ml_df = df[['latitude', 'longitude', 'crime_severity', 'lighting_level', 'crowd_density', 'hour', 'risk_score']]
print(ml_df.shape)
print(ml_df.head())


from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import numpy as np

X = ml_df.drop(columns=['risk_score'])
y = ml_df['risk_score']

# Convert risk_score → 3 classes
def to_class(score):
    if score < 0.4:   return 0   # Safe
    elif score < 0.7: return 1   # Moderate
    else:             return 2   # High Risk

y_class = y.apply(to_class)
print("Class distribution:")
print(y_class.value_counts().rename({0:'Safe', 1:'Moderate', 2:'High Risk'}))

X_train, X_test, y_train, y_test = train_test_split(X, y_class, test_size=0.2, random_state=42)

models = {
    'Logistic Regression':   LogisticRegression(max_iter=1000, random_state=42),
    'Decision Tree':         DecisionTreeClassifier(random_state=42),
    'Random Forest':         RandomForestClassifier(n_estimators=100, random_state=42),
    'Gradient Boosting':     GradientBoostingClassifier(n_estimators=100, random_state=42),
}

results = []
for name, m in models.items():
    m.fit(X_train, y_train)
    preds = m.predict(X_test)
    results.append({
        'Model':      name,
        'Accuracy':   round(accuracy_score(y_test, preds), 4),
        'Precision':  round(precision_score(y_test, preds, average='weighted'), 4),
        'Recall':     round(recall_score(y_test, preds, average='weighted'), 4),
        'F1 Score':   round(f1_score(y_test, preds, average='weighted'), 4),
    })

results_df = pd.DataFrame(results).sort_values('F1 Score', ascending=False)
print("\n")
print(results_df.to_string(index=False))



from sklearn.ensemble import GradientBoostingClassifier

best_model = GradientBoostingClassifier(n_estimators=100, random_state=42)
best_model.fit(X_train, y_train)

final_preds = best_model.predict(X_test)
print("Final Model: Gradient Boosting")
print(f"Accuracy:  {accuracy_score(y_test, final_preds):.4f}")
print(f"Precision: {precision_score(y_test, final_preds, average='weighted'):.4f}")
print(f"Recall:    {recall_score(y_test, final_preds, average='weighted'):.4f}")
print(f"F1 Score:  {f1_score(y_test, final_preds, average='weighted'):.4f}")
print("\nDetailed Report:")
print(classification_report(y_test, final_preds, target_names=['Safe', 'Moderate', 'High Risk']))

joblib.dump(best_model, "ust_model.pkl")
print("Model saved as ust_model.pkl")
