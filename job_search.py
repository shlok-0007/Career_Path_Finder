import requests
import json
import os
from urllib.parse import quote_plus

def search_jobs(query, location="", page=0, api_key=None):
    """
    Search for jobs using SerpAPI Google Jobs API
    
    Args:
        query (str): Job search query (e.g., "python developer")
        location (str, optional): Location for job search (e.g., "San Francisco")
        page (int, optional): Page number for pagination
        api_key (str, optional): SerpAPI API key
        
    Returns:
        dict: Job search results
    """
    # Get API key from environment variable if not provided
    if not api_key:
        api_key = os.environ.get('SERPAPI_KEY')
        if not api_key:
            raise ValueError("SerpAPI key is required. Set SERPAPI_KEY environment variable or pass it as a parameter.")
    
    # Base URL for SerpAPI Google Jobs endpoint
    base_url = "https://serpapi.com/search"
    
    # Build parameters
    params = {
        "engine": "google_jobs",
        "q": query,
        "api_key": api_key
    }
    
    # Add location if provided
    if location:
        params["location"] = location
    
    # Add pagination
    if page > 0:
        params["start"] = page * 10
    
    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Parse response
        data = response.json()
        
        # Process and format job listings
        if "jobs_results" in data:
            processed_jobs = []
            
            for job in data["jobs_results"]:
                processed_job = {
                    "title": job.get("title", ""),
                    "company_name": job.get("company_name", ""),
                    "location": job.get("location", ""),
                    "via": job.get("via", ""),
                    "description": job.get("description", ""),
                    "job_highlights": job.get("job_highlights", []),
                    "thumbnail": job.get("thumbnail", None),
                    "extensions": job.get("extensions", []),
                    "detected_extensions": job.get("detected_extensions", {}),
                    "job_id": job.get("job_id", ""),
                    "link": job.get("link", "")
                }
                
                processed_jobs.append(processed_job)
            
            return {
                "jobs": processed_jobs,
                "total_results": data.get("search_metadata", {}).get("total_results", 0)
            }
        else:
            return {"jobs": [], "total_results": 0}
    
    except requests.exceptions.RequestException as e:
        print(f"Error making request to SerpAPI: {e}")
        return {"error": str(e), "jobs": [], "total_results": 0}
    
    except (KeyError, ValueError, json.JSONDecodeError) as e:
        print(f"Error processing SerpAPI response: {e}")
        return {"error": str(e), "jobs": [], "total_results": 0}

def search_jobs_by_skills(skills, location="", limit=5, api_key=None):
    """
    Search for jobs based on a list of skills
    
    Args:
        skills (list): List of skills
        location (str, optional): Location for job search
        limit (int, optional): Maximum number of jobs to return
        api_key (str, optional): SerpAPI API key
    
    Returns:
        list: Job listings that match the skills
    """
    # Create a search query from skills
    query = " ".join(skills[:3])  # Use top 3 skills for search
    
    # Get job results
    results = search_jobs(query, location, api_key=api_key)
    
    # Limit the number of results
    if "jobs" in results:
        results["jobs"] = results["jobs"][:limit]
    
    return results