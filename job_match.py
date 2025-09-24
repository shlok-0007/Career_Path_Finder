import json

# Load job dataset (replace this with a database or more advanced dataset in production)
with open('jobs.json') as f:
    job_dataset = json.load(f)

def match_skills_to_jobs(extracted_skills):
    job_recommendations = []
    
    # Convert extracted_skills to a set for intersection
    extracted_skills = set(extracted_skills)
    
    for job in job_dataset:
        job_skills = set(job['skills'])
        
        # Calculate the match score based on intersection of extracted and job skills
        common_skills = extracted_skills.intersection(job_skills)
        match_score = len(common_skills) / len(job_skills) * 100  # Match percentage
        
        if match_score > 0:
            job_recommendations.append({
                'title': job['title'],
                'match': round(match_score, 2),
                # 'description': job['description'],
                'skillsToAcquire': list(job_skills - common_skills)
            })
    
    # Sort recommendations by match score in descending order
    job_recommendations = sorted(job_recommendations, key=lambda x: x['match'], reverse=True)
    return job_recommendations
