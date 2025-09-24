from flask import Flask, request, jsonify
from file_upload import save_uploaded_file, extract_text_from_file
from skills_extractor import extract_skills_from_text
from job_match import match_skills_to_jobs
from course_recommender import enhance_job_recommendations_with_courses
from job_search import search_jobs_by_skills
import os
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def health_check():
    return jsonify({'message': 'API is running'}), 200

@app.route('/upload', methods=['POST'])
def upload_cv():
    try:
        print("Request received")
        if 'cv' not in request.files:
            print("No file in request")
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['cv']
        print(f"Received file: {file.filename}")
        if file.filename == '':
            print("Empty filename")
            return jsonify({'error': 'No selected file'}), 400
        
        # Save the uploaded file
        file_path = save_uploaded_file(file)
        print(f"File saved at: {file_path}")
        if not file_path:
            print("Invalid file format")
            return jsonify({'error': 'Invalid file format'}), 400
        
        # Extract text from the uploaded CV
        cv_text = extract_text_from_file(file_path)
        print("Text extracted")
        
        # Extract skills from the CV text
        extracted_skills = extract_skills_from_text(cv_text)
        print(f"Extracted skills: {extracted_skills}")
        
        # Match the extracted skills with relevant jobs
        job_recommendations = match_skills_to_jobs(extracted_skills)
        print(f"Matched jobs: {job_recommendations}")
        
        # Enhance job recommendations with course recommendations
        enhanced_job_recommendations = enhance_job_recommendations_with_courses(job_recommendations)
        print("Added course recommendations")
        
        # Get job listings from SerpAPI (optional, based on API key availability)
        job_listings = []
        try:
            if extracted_skills:
                # Try to get job listings if API key is available
                job_listings = search_jobs_by_skills(extracted_skills, limit=5).get('jobs', [])
                print(f"Found {len(job_listings)} job listings")
        except Exception as e:
            print(f"Error fetching job listings: {e}")
            # Continue without job listings if there's an error
            pass
        
        return jsonify({
            'extracted_skills': extracted_skills,
            'job_recommendations': enhanced_job_recommendations,
            'job_listings': job_listings
        })
    
    except Exception as e:
        print(f"Exception occurred: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/jobs', methods=['GET'])
def get_jobs():
    try:
        # Get parameters from query string
        skills = request.args.get('skills', '')
        location = request.args.get('location', '')
        limit = int(request.args.get('limit', 5))
        
        # Convert skills string to list if provided
        skills_list = skills.split(',') if skills else []
        
        # Search for jobs
        results = search_jobs_by_skills(skills_list, location=location, limit=limit)
        
        return jsonify(results)
    
    except Exception as e:
        print(f"Exception occurred: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    # Add a timestamp to the data
    data['timestamp'] = datetime.now().isoformat()
    # Append to a JSON file
    try:
        with open('contact_data.json', 'a') as f:
            json.dump(data, f)
            f.write('\n')  # Add newline for each entry
        return jsonify({"message": "Data saved successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)