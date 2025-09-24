"""
Course Recommender Module for Career Path Finder

This module provides course recommendations for skills that users need to acquire.
It uses a predefined database of courses mapped to skills.
"""

# Sample course database - In a production environment, this would be in a real database
# Each skill can have multiple courses from different platforms
COURSE_DATABASE = {
    "python": [
        {
            "title": "Python for Everybody",
            "url": "https://www.coursera.org/specializations/python",
            "platform": "Coursera",
            "skill": "python"
        },
        {
            "title": "The Complete Python Bootcamp",
            "url": "https://www.udemy.com/course/complete-python-bootcamp/",
            "platform": "Udemy",
            "skill": "python"
        },
        {
            "title": "Python Crash Course",
            "url": "https://www.edx.org/learn/python",
            "platform": "edX",
            "skill": "python"
        }
    ],
    "javascript": [
        {
            "title": "JavaScript: Understanding the Weird Parts",
            "url": "https://www.udemy.com/course/understand-javascript/",
            "platform": "Udemy",
            "skill": "javascript"
        },
        {
            "title": "Modern JavaScript From The Beginning",
            "url": "https://www.udemy.com/course/modern-javascript-from-the-beginning/",
            "platform": "Udemy",
            "skill": "javascript"
        },
        {
            "title": "JavaScript Algorithms and Data Structures",
            "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/",
            "platform": "FreeCodeCamp",
            "skill": "javascript"
        }
    ],
    "react": [
        {
            "title": "React - The Complete Guide",
            "url": "https://www.udemy.com/course/react-the-complete-guide-incl-redux/",
            "platform": "Udemy",
            "skill": "react"
        },
        {
            "title": "Full Stack Web Development with React",
            "url": "https://www.coursera.org/specializations/full-stack-react",
            "platform": "Coursera",
            "skill": "react"
        },
        {
            "title": "React Native - The Practical Guide",
            "url": "https://www.udemy.com/course/react-native-the-practical-guide/",
            "platform": "Udemy",
            "skill": "react"
        }
    ],
    "data analysis": [
        {
            "title": "Data Analysis with Python",
            "url": "https://www.coursera.org/learn/data-analysis-with-python",
            "platform": "Coursera",
            "skill": "data analysis"
        },
        {
            "title": "Data Analysis and Visualization",
            "url": "https://www.linkedin.com/learning/data-analysis-and-visualization-foundations",
            "platform": "LinkedIn Learning",
            "skill": "data analysis"
        },
        {
            "title": "Data Analysis with Pandas",
            "url": "https://www.datacamp.com/courses/data-manipulation-with-pandas",
            "platform": "DataCamp",
            "skill": "data analysis"
        }
    ],
    "machine learning": [
        {
            "title": "Machine Learning",
            "url": "https://www.coursera.org/learn/machine-learning",
            "platform": "Coursera",
            "skill": "machine learning"
        },
        {
            "title": "Machine Learning A-Z",
            "url": "https://www.udemy.com/course/machinelearning/",
            "platform": "Udemy",
            "skill": "machine learning"
        },
        {
            "title": "Deep Learning Specialization",
            "url": "https://www.coursera.org/specializations/deep-learning",
            "platform": "Coursera",
            "skill": "machine learning"
        }
    ],
    "sql": [
        {
            "title": "SQL for Data Science",
            "url": "https://www.coursera.org/learn/sql-for-data-science",
            "platform": "Coursera",
            "skill": "sql"
        },
        {
            "title": "The Complete SQL Bootcamp",
            "url": "https://www.udemy.com/course/the-complete-sql-bootcamp/",
            "platform": "Udemy",
            "skill": "sql"
        },
        {
            "title": "SQL Essential Training",
            "url": "https://www.linkedin.com/learning/sql-essential-training",
            "platform": "LinkedIn Learning",
            "skill": "sql"
        }
    ],
    "aws": [
        {
            "title": "AWS Certified Solutions Architect",
            "url": "https://www.udemy.com/course/aws-certified-solutions-architect-associate/",
            "platform": "Udemy",
            "skill": "aws"
        },
        {
            "title": "AWS Fundamentals",
            "url": "https://www.coursera.org/specializations/aws-fundamentals",
            "platform": "Coursera",
            "skill": "aws"
        },
        {
            "title": "AWS Cloud Practitioner Essentials",
            "url": "https://aws.amazon.com/training/digital/aws-cloud-practitioner-essentials/",
            "platform": "AWS Training",
            "skill": "aws"
        }
    ],
    "docker": [
        {
            "title": "Docker and Kubernetes: The Complete Guide",
            "url": "https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/",
            "platform": "Udemy",
            "skill": "docker"
        },
        {
            "title": "Getting Started with Docker",
            "url": "https://www.pluralsight.com/courses/getting-started-docker",
            "platform": "Pluralsight",
            "skill": "docker"
        },
        {
            "title": "Docker for Developers",
            "url": "https://www.linkedin.com/learning/docker-for-developers",
            "platform": "LinkedIn Learning",
            "skill": "docker"
        }
    ],
    "nodejs": [
        {
            "title": "Node.js, Express & MongoDB",
            "url": "https://www.udemy.com/course/nodejs-express-mongodb-bootcamp/",
            "platform": "Udemy",
            "skill": "nodejs"
        },
        {
            "title": "Server-side Development with NodeJS",
            "url": "https://www.coursera.org/learn/server-side-nodejs",
            "platform": "Coursera",
            "skill": "nodejs"
        },
        {
            "title": "Node.js API Masterclass",
            "url": "https://www.udemy.com/course/nodejs-api-masterclass/",
            "platform": "Udemy",
            "skill": "nodejs"
        }
    ],
    "agile": [
        {
            "title": "Agile with Atlassian Jira",
            "url": "https://www.coursera.org/learn/agile-atlassian-jira",
            "platform": "Coursera",
            "skill": "agile"
        },
        {
            "title": "Agile Fundamentals",
            "url": "https://www.pluralsight.com/courses/agile-fundamentals",
            "platform": "Pluralsight",
            "skill": "agile"
        },
        {
            "title": "Scrum: The Basics",
            "url": "https://www.linkedin.com/learning/scrum-the-basics",
            "platform": "LinkedIn Learning",
            "skill": "agile"
        }
    ],
    "java": [
        {
            "title": "Java Programming Masterclass",
            "url": "https://www.udemy.com/course/java-the-complete-java-developer-course/",
            "platform": "Udemy",
            "skill": "java"
        },
        {
            "title": "Java Programming and Software Engineering Fundamentals",
            "url": "https://www.coursera.org/specializations/java-programming",
            "platform": "Coursera",
            "skill": "java"
        },
        {
            "title": "Spring & Hibernate for Beginners",
            "url": "https://www.udemy.com/course/spring-hibernate-tutorial/",
            "platform": "Udemy",
            "skill": "java"
        }
    ],
    "devops": [
        {
            "title": "DevOps on AWS",
            "url": "https://www.coursera.org/specializations/aws-devops",
            "platform": "Coursera",
            "skill": "devops"
        },
        {
            "title": "DevOps Essentials",
            "url": "https://www.pluralsight.com/paths/devops-essentials",
            "platform": "Pluralsight",
            "skill": "devops"
        },
        {
            "title": "DevOps Engineer Masters Program",
            "url": "https://www.simplilearn.com/devops-engineer-masters-program-certification-training",
            "platform": "Simplilearn",
            "skill": "devops"
        }
    ],
    "git": [
        {
            "title": "Git Complete: The Definitive Guide",
            "url": "https://www.udemy.com/course/git-complete/",
            "platform": "Udemy",
            "skill": "git"
        },
        {
            "title": "Version Control with Git",
            "url": "https://www.coursera.org/learn/version-control-with-git",
            "platform": "Coursera",
            "skill": "git"
        },
        {
            "title": "Git Essential Training",
            "url": "https://www.linkedin.com/learning/git-essential-training",
            "platform": "LinkedIn Learning",
            "skill": "git"
        }
    ],
    "html": [
        {
            "title": "HTML, CSS, and Javascript for Web Developers",
            "url": "https://www.coursera.org/learn/html-css-javascript-for-web-developers",
            "platform": "Coursera",
            "skill": "html"
        },
        {
            "title": "Responsive Web Design",
            "url": "https://www.freecodecamp.org/learn/responsive-web-design/",
            "platform": "FreeCodeCamp",
            "skill": "html"
        },
        {
            "title": "HTML5 and CSS3 Fundamentals",
            "url": "https://www.edx.org/learn/html5/w3c-html5-and-css-fundamentals",
            "platform": "edX",
            "skill": "html"
        }
    ],
    "css": [
        {
            "title": "CSS - The Complete Guide",
            "url": "https://www.udemy.com/course/css-the-complete-guide-incl-flexbox-grid-sass/",
            "platform": "Udemy",
            "skill": "css"
        },
        {
            "title": "Advanced CSS and Sass",
            "url": "https://www.udemy.com/course/advanced-css-and-sass/",
            "platform": "Udemy",
            "skill": "css"
        },
        {
            "title": "CSS Grid and Flexbox for Responsive Web Design",
            "url": "https://frontendmasters.com/courses/css-grid-flexbox-v2/",
            "platform": "Frontend Masters",
            "skill": "css"
        }
    ],
    "data visualization": [
        {
            "title": "Data Visualization with Tableau",
            "url": "https://www.coursera.org/specializations/data-visualization",
            "platform": "Coursera",
            "skill": "data visualization"
        },
        {
            "title": "D3.js Data Visualization Fundamentals",
            "url": "https://www.pluralsight.com/courses/d3js-data-visualization-fundamentals",
            "platform": "Pluralsight",
            "skill": "data visualization"
        },
        {
            "title": "Data Visualization with Power BI",
            "url": "https://www.udemy.com/course/microsoft-power-bi-up-running-with-power-bi-desktop/",
            "platform": "Udemy",
            "skill": "data visualization"
        }
    ],
    "typescript": [
        {
            "title": "Understanding TypeScript",
            "url": "https://www.udemy.com/course/understanding-typescript/",
            "platform": "Udemy",
            "skill": "typescript"
        },
        {
            "title": "TypeScript Essential Training",
            "url": "https://www.linkedin.com/learning/typescript-essential-training",
            "platform": "LinkedIn Learning",
            "skill": "typescript"
        },
        {
            "title": "TypeScript for Professionals",
            "url": "https://www.educative.io/courses/typescript-for-professionals",
            "platform": "Educative",
            "skill": "typescript"
        }
    ],
    "flutter": [
        {
            "title": "Flutter & Dart - The Complete Guide",
            "url": "https://www.udemy.com/course/flutter-bootcamp-with-dart/",
            "platform": "Udemy",
            "skill": "flutter"
        },
        {
            "title": "Build Apps with Flutter",
            "url": "https://www.codecademy.com/learn/paths/build-apps-with-flutter",
            "platform": "Codecademy",
            "skill": "flutter"
        },
        {
            "title": "Flutter App Development Masterclass",
            "url": "https://www.udemy.com/course/flutter-app-development-masterclass-with-dart/",
            "platform": "Udemy",
            "skill": "flutter"
        }
    ],
    "golang": [
        {
            "title": "Go: The Complete Developer's Guide",
            "url": "https://www.udemy.com/course/go-the-complete-developers-guide/",
            "platform": "Udemy",
            "skill": "golang"
        },
        {
            "title": "Programming with Google Go",
            "url": "https://www.coursera.org/specializations/google-golang",
            "platform": "Coursera",
            "skill": "golang"
        },
        {
            "title": "Learn Go",
            "url": "https://www.codecademy.com/learn/learn-go",
            "platform": "Codecademy",
            "skill": "golang"
        }
    ],
    "vue": [
        {
            "title": "Vue - The Complete Guide",
            "url": "https://www.udemy.com/course/vuejs-2-the-complete-guide/",
            "platform": "Udemy",
            "skill": "vue"
        },
        {
            "title": "Vue.js Essentials",
            "url": "https://www.pluralsight.com/courses/vuejs-fundamentals",
            "platform": "Pluralsight",
            "skill": "vue"
        },
        {
            "title": "Vue JS 3: From Zero to Hero",
            "url": "https://www.udemy.com/course/vue-js-3-from-zero-to-hero/",
            "platform": "Udemy",
            "skill": "vue"
        }
    ],
    "angular": [
        {
            "title": "Angular - The Complete Guide",
            "url": "https://www.udemy.com/course/the-complete-guide-to-angular-2/",
            "platform": "Udemy",
            "skill": "angular"
        },
        {
            "title": "Angular Fundamentals",
            "url": "https://www.pluralsight.com/courses/angular-fundamentals",
            "platform": "Pluralsight",
            "skill": "angular"
        },
        {
            "title": "Building Web Applications with Angular",
            "url": "https://www.coursera.org/learn/angular",
            "platform": "Coursera",
            "skill": "angular"
        }
    ],
    "ruby": [
        {
            "title": "The Complete Ruby on Rails Developer Course",
            "url": "https://www.udemy.com/course/the-complete-ruby-on-rails-developer-course/",
            "platform": "Udemy",
            "skill": "ruby"
        },
        {
            "title": "Ruby Programming",
            "url": "https://www.codecademy.com/learn/learn-ruby",
            "platform": "Codecademy",
            "skill": "ruby"
        },
        {
            "title": "Learn to Code with Ruby",
            "url": "https://www.udemy.com/course/learn-to-code-with-ruby-lang/",
            "platform": "Udemy",
            "skill": "ruby"
        }
    ],
    "c#": [
        {
            "title": "C# Basics for Beginners",
            "url": "https://www.udemy.com/course/csharp-tutorial-for-beginners/",
            "platform": "Udemy",
            "skill": "c#"
        },
        {
            "title": "C# Fundamentals",
            "url": "https://www.pluralsight.com/courses/csharp-fundamentals-dev",
            "platform": "Pluralsight",
            "skill": "c#"
        },
        {
            "title": "Programming in C#: A comprehensive approach",
            "url": "https://www.edx.org/learn/c-sharp/microsoft-programming-in-c-sharp-a-comprehensive-approach",
            "platform": "edX",
            "skill": "c#"
        }
    ],
    "php": [
        {
            "title": "PHP for Beginners",
            "url": "https://www.udemy.com/course/php-for-beginners-/",
            "platform": "Udemy",
            "skill": "php"
        },
        {
            "title": "Learn PHP",
            "url": "https://www.codecademy.com/learn/learn-php",
            "platform": "Codecademy",
            "skill": "php"
        },
        {
            "title": "PHP & MySQL - Certification Course for Beginners",
            "url": "https://www.udemy.com/course/php-mysql-certification-course-for-beginners/",
            "platform": "Udemy",
            "skill": "php"
        }
    ],
    "laravel": [
        {
            "title": "Laravel - The Complete Guide with Real World Projects",
            "url": "https://www.udemy.com/course/laravel-the-complete-guide-with-real-world-projects/",
            "platform": "Udemy",
            "skill": "laravel"
        },
        {
            "title": "Laravel 9: Build Complete CMS",
            "url": "https://www.udemy.com/course/laravel-build-complete-cms/",
            "platform": "Udemy",
            "skill": "laravel"
        },
        {
            "title": "Laravel from Scratch",
            "url": "https://laracasts.com/series/laravel-8-from-scratch",
            "platform": "Laracasts",
            "skill": "laravel"
        }
    ],
    "swift": [
        {
            "title": "iOS & Swift - The Complete iOS App Development Bootcamp",
            "url": "https://www.udemy.com/course/ios-13-app-development-bootcamp/",
            "platform": "Udemy",
            "skill": "swift"
        },
        {
            "title": "SwiftUI Masterclass",
            "url": "https://www.udemy.com/course/swiftui-masterclass-course-ios-development-with-swift/",
            "platform": "Udemy",
            "skill": "swift"
        },
        {
            "title": "Learn Swift",
            "url": "https://www.codecademy.com/learn/learn-swift",
            "platform": "Codecademy",
            "skill": "swift"
        }
    ],
    "kotlin": [
        {
            "title": "Android App Development with Kotlin",
            "url": "https://www.udemy.com/course/android-kotlin-developer/",
            "platform": "Udemy",
            "skill": "kotlin"
        },
        {
            "title": "Kotlin for Java Developers",
            "url": "https://www.coursera.org/learn/kotlin-for-java-developers",
            "platform": "Coursera",
            "skill": "kotlin"
        },
        {
            "title": "Kotlin Fundamentals",
            "url": "https://www.pluralsight.com/courses/kotlin-fundamentals",
            "platform": "Pluralsight",
            "skill": "kotlin"
        }
    ],
    "blockchain": [
        {
            "title": "Blockchain Specialization",
            "url": "https://www.coursera.org/specializations/blockchain",
            "platform": "Coursera",
            "skill": "blockchain"
        },
        {
            "title": "Ethereum and Solidity: The Complete Developer's Guide",
            "url": "https://www.udemy.com/course/ethereum-and-solidity-the-complete-developers-guide/",
            "platform": "Udemy",
            "skill": "blockchain"
        },
        {
            "title": "Blockchain Fundamentals",
            "url": "https://www.pluralsight.com/courses/blockchain-fundamentals",
            "platform": "Pluralsight",
            "skill": "blockchain"
        }
    ],
    "cybersecurity": [
        {
            "title": "The Complete Cyber Security Course",
            "url": "https://www.udemy.com/course/the-complete-internet-security-privacy-course-volume-1/",
            "platform": "Udemy",
            "skill": "cybersecurity"
        },
        {
            "title": "IBM Cybersecurity Analyst Professional Certificate",
            "url": "https://www.coursera.org/professional-certificates/ibm-cybersecurity-analyst",
            "platform": "Coursera",
            "skill": "cybersecurity"
        },
        {
            "title": "CompTIA Security+ Certification Prep",
            "url": "https://www.pluralsight.com/paths/comptia-security-plus",
            "platform": "Pluralsight",
            "skill": "cybersecurity"
        }
    ],
    "mongodb": [
        {
            "title": "MongoDB - The Complete Developer's Guide",
            "url": "https://www.udemy.com/course/mongodb-the-complete-developers-guide/",
            "platform": "Udemy",
            "skill": "mongodb"
        },
        {
            "title": "MongoDB Basics",
            "url": "https://university.mongodb.com/courses/M001/about",
            "platform": "MongoDB University",
            "skill": "mongodb"
        },
        {
            "title": "The Complete Developers Guide to MongoDB",
            "url": "https://www.udemy.com/course/the-complete-developers-guide-to-mongodb/",
            "platform": "Udemy",
            "skill": "mongodb"
        }
    ],
    "django": [
        {
            "title": "Django 4 - Complete Course",
            "url": "https://www.udemy.com/course/django-4-complete-course/",
            "platform": "Udemy",
            "skill": "django"
        },
        {
            "title": "Django for Everybody",
            "url": "https://www.coursera.org/specializations/django",
            "platform": "Coursera",
            "skill": "django"
        },
        {
            "title": "Django Web Framework",
            "url": "https://www.pluralsight.com/courses/django-fundamentals-update",
            "platform": "Pluralsight",
            "skill": "django"
        }
    ],
    "flask": [
        {
            "title": "Python and Flask Bootcamp",
            "url": "https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask/",
            "platform": "Udemy",
            "skill": "flask"
        },
        {
            "title": "REST APIs with Flask and Python",
            "url": "https://www.udemy.com/course/rest-api-flask-and-python/",
            "platform": "Udemy",
            "skill": "flask"
        },
        {
            "title": "Flask: Getting Started",
            "url": "https://www.pluralsight.com/courses/flask-getting-started",
            "platform": "Pluralsight",
            "skill": "flask"
        }
    ],
    "tensorflow": [
        {
            "title": "TensorFlow Developer Professional Certificate",
            "url": "https://www.coursera.org/professional-certificates/tensorflow-in-practice",
            "platform": "Coursera",
            "skill": "tensorflow"
        },
        {
            "title": "Complete Guide to TensorFlow for Deep Learning with Python",
            "url": "https://www.udemy.com/course/complete-guide-to-tensorflow-for-deep-learning-with-python/",
            "platform": "Udemy",
            "skill": "tensorflow"
        },
        {
            "title": "TensorFlow: Getting Started",
            "url": "https://www.pluralsight.com/courses/tensorflow-getting-started",
            "platform": "Pluralsight",
            "skill": "tensorflow"
        }
    ],
    "pytorch": [
        {
            "title": "PyTorch for Deep Learning",
            "url": "https://www.udemy.com/course/pytorch-for-deep-learning-with-python-bootcamp/",
            "platform": "Udemy",
            "skill": "pytorch"
        },
        {
            "title": "Deep Learning with PyTorch",
            "url": "https://www.coursera.org/learn/deep-learning-with-pytorch",
            "platform": "Coursera",
            "skill": "pytorch"
        },
        {
            "title": "PyTorch Fundamentals",
            "url": "https://www.pluralsight.com/courses/pytorch-fundamentals",
            "platform": "Pluralsight",
            "skill": "pytorch"
        }
    ],
    "fastapi": [
        {
            "title": "FastAPI: The Complete Course",
            "url": "https://www.udemy.com/course/fastapi-the-complete-course/",
            "platform": "Udemy",
            "skill": "fastapi"
        },
        {
            "title": "Building REST APIs with FastAPI",
            "url": "https://testdriven.io/courses/fastapi-crud/",
            "platform": "TestDriven.io",
            "skill": "fastapi"
        },
        {
            "title": "FastAPI for Python Web Development",
            "url": "https://www.packtpub.com/product/fastapi-for-python-web-development/9781803234595",
            "platform": "Packt",
            "skill": "fastapi"
        }
    ],
    "kubernetes": [
        {
            "title": "Kubernetes for the Absolute Beginners",
            "url": "https://www.udemy.com/course/learn-kubernetes/",
            "platform": "Udemy",
            "skill": "kubernetes"
        },
        {
            "title": "Getting Started with Kubernetes",
            "url": "https://www.pluralsight.com/courses/kubernetes-getting-started",
            "platform": "Pluralsight",
            "skill": "kubernetes"
        },
        {
            "title": "Certified Kubernetes Administrator (CKA)",
            "url": "https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/",
            "platform": "Udemy",
            "skill": "kubernetes"
        }
    ]
}

def get_courses_for_skill(skill):
    """
    Get course recommendations for a specific skill.
    
    Args:
        skill: The skill to find courses for.
        
    Returns:
        A list of course dictionaries or an empty list if no courses found.
    """
    # Normalize the skill name to lowercase for case-insensitive matching
    skill_lower = skill.lower()
    
    # Direct match in the database
    if skill_lower in COURSE_DATABASE:
        return COURSE_DATABASE[skill_lower]
    
    # Try to find partial matches
    for db_skill in COURSE_DATABASE:
        if skill_lower in db_skill or db_skill in skill_lower:
            return COURSE_DATABASE[db_skill]
    
    # No match found
    return []

def get_courses_for_skills(skills_list, max_courses_per_skill=2):
    """
    Get course recommendations for a list of skills.
    
    Args:
        skills_list: List of skills to find courses for.
        max_courses_per_skill: Maximum number of courses to return per skill.
        
    Returns:
        A dictionary mapping skills to lists of course recommendations.
    """
    courses_by_skill = {}
    
    for skill in skills_list:
        courses = get_courses_for_skill(skill)
        if courses:
            # Limit the number of courses per skill
            courses_by_skill[skill] = courses[:max_courses_per_skill]
    
    return courses_by_skill

def enhance_job_recommendations_with_courses(job_recommendations):
    """
    Enhance job recommendations with course recommendations for skills to acquire.
    
    Args:
        job_recommendations: List of job recommendation dictionaries.
        
    Returns:
        Enhanced job recommendations with course data.
    """
    enhanced_recommendations = []
    
    for job in job_recommendations:
        enhanced_job = job.copy()
        
        # If the job has skills to acquire, add course recommendations
        if 'skillsToAcquire' in job and job['skillsToAcquire']:
            # Get courses for each skill to acquire
            all_courses = []
            skills_courses = get_courses_for_skills(job['skillsToAcquire'])
            
            # Flatten the courses list
            for skill, courses in skills_courses.items():
                all_courses.extend(courses)
            
            # Add the courses to the job recommendation
            enhanced_job['courses'] = all_courses
        
        enhanced_recommendations.append(enhanced_job)
    
    return enhanced_recommendations