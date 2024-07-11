

# # Rule-Based Example (Python)

# import pandas as pd

# # Example data
# job_seekers = pd.DataFrame({
#     'id': [1, 2, 3],
#     'skills': [['python', 'data analysis'], ['java', 'spring'], ['javascript', 'react']],
#     'location': ['New York', 'San Francisco', 'Los Angeles']
# })

# jobs = pd.DataFrame({
#     'id': [101, 102, 103],
#     'required_skills': [['python', 'machine learning'], ['java', 'spring'], ['javascript', 'angular']],
#     'location': ['New York', 'San Francisco', 'Los Angeles']
# })

# # Simple rule-based matching
# def match(job_seeker, job):
#     skills_match = all(skill in job_seeker['skills'] for skill in job['required_skills'])
#     location_match = job_seeker['location'] == job['location']
#     return skills_match and location_match

# matches = []
# for _, job_seeker in job_seekers.iterrows():
#     for _, job in jobs.iterrows():
#         if match(job_seeker, job):
#             matches.append((job_seeker['id'], job['id']))

# print(matches)



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Example data
data = pd.DataFrame({
    'seeker_id': [1, 2, 3, 4],
    'job_id': [101, 102, 103, 104],
    'skill_match': [1, 0, 1, 0],  # 1 if skills match, 0 otherwise
    'location_match': [1, 1, 0, 0],  # 1 if location matches, 0 otherwise
    'matched': [1, 0, 1, 0]  # Target variable: 1 if match, 0 otherwise
})

# Features and target variable
X = data[['skill_match', 'location_match']]
y = data['matched']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
