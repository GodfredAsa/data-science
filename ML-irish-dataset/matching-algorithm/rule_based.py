import pandas as pd

# Example data
job_seekers = pd.DataFrame({
    'id': [1, 2, 3],
    'skills': [['python', 'data analysis'], ['java', 'spring'], ['javascript', 'react']],
    'location': ['New York', 'San Francisco', 'Los Angeles']
})

jobs = pd.DataFrame({
    'id': [101, 102, 103],
    'required_skills': [['python', 'machine learning'], ['java', 'spring'], ['javascript', 'angular']],
    'location': ['New York', 'San Francisco', 'Los Angeles']
})

# Simple rule-based matching
def match(job_seeker, job):
    skills_match = all(skill in job_seeker['skills'] for skill in job['required_skills'])
    location_match = job_seeker['location'] == job['location']
    return skills_match and location_match

matches = []
for _, job_seeker in job_seekers.iterrows():
    for _, job in jobs.iterrows():
        if match(job_seeker, job):
            matches.append((job_seeker['id'], job['id']))

print(matches)
