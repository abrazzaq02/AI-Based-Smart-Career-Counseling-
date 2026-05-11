"""
Knowledge Base — All Career Rules for the Expert System
"""

KNOWLEDGE_BASE = {
    "AI Engineer": {
        "required_skills":    ["Programming", "Mathematics"],
        "required_interests": ["Artificial Intelligence"],
        "personality_bonus":  ["Analytical", "Introvert"],
        "min_cgpa":           3.0,
        "domains":            ["Software", "AI"],
        "icon":               "🤖",
        "color":              "#6C63FF",
        "roadmap": [
            "Python Programming (Basics to Advanced)",
            "Machine Learning with scikit-learn",
            "Deep Learning — TensorFlow / PyTorch",
            "Natural Language Processing (NLP)",
            "Model Deployment with Flask / FastAPI",
            "Build 3 AI Projects for Portfolio",
        ],
        "certifications": [
            "Google ML Crash Course (Free)",
            "DeepLearning.AI TensorFlow Developer Certificate",
            "AWS Certified Machine Learning – Specialty",
        ],
        "salary_pkr": "PKR 150,000 – 350,000 / month",
        "salary_usd": "$800 – $3,500 / month (remote)",
        "description": (
            "AI Engineers design, build, and deploy AI-powered systems. "
            "They train machine learning models and integrate AI into real-world products."
        ),
        "job_roles": ["ML Engineer", "AI Researcher", "NLP Engineer", "Computer Vision Engineer"],
    },

    "Data Scientist": {
        "required_skills":    ["Programming", "Statistics"],
        "required_interests": ["Data Science", "Artificial Intelligence"],
        "personality_bonus":  ["Analytical"],
        "min_cgpa":           2.8,
        "domains":            ["AI", "Software"],
        "icon":               "📊",
        "color":              "#00B4D8",
        "roadmap": [
            "Python & R Programming",
            "Statistics & Probability Theory",
            "Data Wrangling — Pandas, NumPy",
            "Data Visualization — Matplotlib, Seaborn, Plotly",
            "Machine Learning Algorithms",
            "SQL & Database Skills",
            "Kaggle Competitions (5+ medals target)",
        ],
        "certifications": [
            "IBM Data Science Professional Certificate",
            "Google Data Analytics Certificate",
            "DataCamp Data Scientist Track",
        ],
        "salary_pkr": "PKR 120,000 – 300,000 / month",
        "salary_usd": "$600 – $2,800 / month (remote)",
        "description": (
            "Data Scientists extract actionable insights from large datasets using "
            "statistical analysis, machine learning, and data visualization."
        ),
        "job_roles": ["Data Analyst", "BI Developer", "Research Scientist", "Quantitative Analyst"],
    },

    "Software Engineer": {
        "required_skills":    ["Programming", "Problem Solving"],
        "required_interests": ["Software Development", "Technology"],
        "personality_bonus":  ["Introvert", "Analytical"],
        "min_cgpa":           2.5,
        "domains":            ["Software"],
        "icon":               "💻",
        "color":              "#2EC4B6",
        "roadmap": [
            "Core Programming — Python / Java / C++",
            "Data Structures & Algorithms",
            "Object-Oriented Design Principles",
            "Version Control — Git & GitHub",
            "Backend Development — Node.js / Django / Spring",
            "Frontend Basics — HTML, CSS, JavaScript",
            "System Design Fundamentals",
        ],
        "certifications": [
            "Oracle Certified Java SE Programmer",
            "Microsoft Azure Developer Associate",
            "LeetCode 150+ Problems Solved",
        ],
        "salary_pkr": "PKR 100,000 – 280,000 / month",
        "salary_usd": "$500 – $2,500 / month (remote)",
        "description": (
            "Software Engineers design, develop, test, and maintain software systems "
            "and applications across web, mobile, and desktop platforms."
        ),
        "job_roles": ["Backend Developer", "Full Stack Developer", "Mobile Developer", "DevOps Engineer"],
    },

    "Cybersecurity Expert": {
        "required_skills":    ["Networking", "Programming"],
        "required_interests": ["Cybersecurity", "Networking"],
        "personality_bonus":  ["Analytical", "Introvert"],
        "min_cgpa":           2.7,
        "domains":            ["Networking", "Software"],
        "icon":               "🔐",
        "color":              "#E63946",
        "roadmap": [
            "Networking Fundamentals — TCP/IP, OSI Model",
            "Linux Operating System Mastery",
            "Ethical Hacking Fundamentals",
            "Penetration Testing — Metasploit, Burp Suite",
            "Network Security & Firewalls",
            "Cryptography & PKI",
            "CTF Competitions (Capture the Flag)",
        ],
        "certifications": [
            "CompTIA Security+ (Most Recognized)",
            "Certified Ethical Hacker (CEH)",
            "OSCP — Offensive Security Certified Professional",
        ],
        "salary_pkr": "PKR 130,000 – 320,000 / month",
        "salary_usd": "$700 – $3,200 / month (remote)",
        "description": (
            "Cybersecurity Experts protect organizations from cyber threats, "
            "conduct security audits, and respond to security incidents."
        ),
        "job_roles": ["Penetration Tester", "SOC Analyst", "Security Architect", "Incident Responder"],
    },

    "Graphic Designer": {
        "required_skills":    ["Creativity", "Design"],
        "required_interests": ["Graphic Design", "Art & Creative"],
        "personality_bonus":  ["Creative", "Introvert"],
        "min_cgpa":           2.0,
        "domains":            ["Design"],
        "icon":               "🎨",
        "color":              "#FF6B6B",
        "roadmap": [
            "Adobe Photoshop & Illustrator Mastery",
            "UI/UX Design Principles",
            "Typography & Color Theory",
            "Figma / Adobe XD (UI Design Tools)",
            "Motion Graphics — Adobe After Effects",
            "Build a Strong Behance Portfolio (20+ projects)",
        ],
        "certifications": [
            "Adobe Certified Professional",
            "Google UX Design Certificate (Coursera)",
            "Interaction Design Foundation Membership",
        ],
        "salary_pkr": "PKR 60,000 – 180,000 / month",
        "salary_usd": "$300 – $1,800 / month (remote/freelance)",
        "description": (
            "Graphic Designers create visual content—logos, branding, UI, and marketing "
            "materials—to communicate messages effectively."
        ),
        "job_roles": ["UI Designer", "Brand Designer", "Motion Designer", "Illustrator"],
    },

    "Business Analyst": {
        "required_skills":    ["Communication", "Problem Solving"],
        "required_interests": ["Business & Finance", "Management"],
        "personality_bonus":  ["Extrovert", "Analytical"],
        "min_cgpa":           2.5,
        "domains":            ["Business"],
        "icon":               "📈",
        "color":              "#F4A261",
        "roadmap": [
            "Business Communication Skills",
            "Data Analysis — Excel, Power BI, Tableau",
            "Requirements Gathering Techniques",
            "SQL for Business Intelligence",
            "Project Management Basics",
            "Stakeholder Management & Presentations",
        ],
        "certifications": [
            "CBAP — Certified Business Analysis Professional",
            "PMI-PBA — Professional in Business Analysis",
            "Microsoft Power BI Data Analyst Associate",
        ],
        "salary_pkr": "PKR 90,000 – 220,000 / month",
        "salary_usd": "$450 – $2,000 / month (remote)",
        "description": (
            "Business Analysts bridge IT and business teams, analyzing "
            "processes, gathering requirements, and recommending improvements."
        ),
        "job_roles": ["Product Analyst", "Systems Analyst", "BI Analyst", "Consultant"],
    },

    "Project Manager": {
        "required_skills":    ["Communication", "Leadership"],
        "required_interests": ["Management", "Business & Finance"],
        "personality_bonus":  ["Extrovert"],
        "min_cgpa":           2.5,
        "domains":            ["Business", "Software"],
        "icon":               "🗂️",
        "color":              "#457B9D",
        "roadmap": [
            "Project Management Fundamentals",
            "Agile & Scrum Methodology",
            "Risk Management & Mitigation",
            "MS Project / Jira / Trello",
            "Team Leadership & Communication",
            "Budget & Resource Planning",
        ],
        "certifications": [
            "PMP — Project Management Professional",
            "Certified Scrum Master (CSM)",
            "PRINCE2 Foundation & Practitioner",
        ],
        "salary_pkr": "PKR 120,000 – 300,000 / month",
        "salary_usd": "$600 – $2,800 / month (remote)",
        "description": (
            "Project Managers plan, execute, monitor, and close projects, "
            "ensuring delivery on time, within scope, and budget."
        ),
        "job_roles": ["Scrum Master", "Product Owner", "Program Manager", "Delivery Manager"],
    },

    "Network Engineer": {
        "required_skills":    ["Networking", "Problem Solving"],
        "required_interests": ["Networking", "Technology"],
        "personality_bonus":  ["Analytical"],
        "min_cgpa":           2.5,
        "domains":            ["Networking"],
        "icon":               "🌐",
        "color":              "#06D6A0",
        "roadmap": [
            "Networking Fundamentals — CCNA Level",
            "Cisco IOS Configuration",
            "Routing & Switching Protocols",
            "Network Monitoring — Wireshark, SolarWinds",
            "Cloud Networking — AWS / Azure",
            "IPv6 & Software Defined Networking (SDN)",
        ],
        "certifications": [
            "CCNA — Cisco Certified Network Associate",
            "CompTIA Network+",
            "AWS Certified Advanced Networking – Specialty",
        ],
        "salary_pkr": "PKR 100,000 – 260,000 / month",
        "salary_usd": "$500 – $2,400 / month (remote)",
        "description": (
            "Network Engineers design, implement, maintain, and troubleshoot "
            "computer networks for organizations."
        ),
        "job_roles": ["Network Administrator", "Cloud Network Engineer", "NOC Engineer", "VoIP Engineer"],
    },

    "Robotics Engineer": {
        "required_skills":    ["Programming", "Mathematics", "Problem Solving"],
        "required_interests": ["Robotics", "Artificial Intelligence", "Technology"],
        "personality_bonus":  ["Analytical", "Creative"],
        "min_cgpa":           3.0,
        "domains":            ["Robotics", "AI"],
        "icon":               "🦾",
        "color":              "#9B5DE5",
        "roadmap": [
            "C++ / Python Programming (Advanced)",
            "Electronics & Microcontrollers — Arduino, Raspberry Pi",
            "ROS — Robot Operating System",
            "Computer Vision with OpenCV",
            "Control Systems & Kinematics",
            "Build 2-3 Robotics Hardware Projects",
        ],
        "certifications": [
            "ROS Developer Certificate",
            "NVIDIA Jetson AI Specialist",
            "Coursera Robotics Specialization (UPenn)",
        ],
        "salary_pkr": "PKR 140,000 – 350,000 / month",
        "salary_usd": "$700 – $3,500 / month",
        "description": (
            "Robotics Engineers design, build, and program robots for "
            "manufacturing, healthcare, space, and automation applications."
        ),
        "job_roles": ["Automation Engineer", "ROS Developer", "Mechatronics Engineer", "Drone Engineer"],
    },

    "Game Developer": {
        "required_skills":    ["Programming", "Creativity"],
        "required_interests": ["Gaming", "Graphic Design"],
        "personality_bonus":  ["Creative", "Introvert"],
        "min_cgpa":           2.3,
        "domains":            ["Software", "Design"],
        "icon":               "🎮",
        "color":              "#FF9F1C",
        "roadmap": [
            "C# Programming Fundamentals",
            "Unity Game Engine — 2D & 3D",
            "Game Physics & Mechanics Design",
            "Game UI/UX Design",
            "Shader Programming (HLSL/GLSL)",
            "Publish Games on Steam / Play Store",
        ],
        "certifications": [
            "Unity Certified Professional Developer",
            "Unreal Engine Developer Certificate (Udemy)",
            "GameDev.tv Complete Unity Developer Course",
        ],
        "salary_pkr": "PKR 80,000 – 220,000 / month",
        "salary_usd": "$400 – $2,200 / month (remote/indie)",
        "description": (
            "Game Developers design and build video games for PC, "
            "mobile, console, and VR/AR platforms."
        ),
        "job_roles": ["Unity Developer", "Gameplay Programmer", "Game Designer", "VR/AR Developer"],
    },
}

ALL_SKILLS = [
    "Programming", "Mathematics", "Statistics", "Networking",
    "Creativity", "Design", "Communication", "Leadership",
    "Problem Solving", "Research",
]

ALL_INTERESTS = [
    "Artificial Intelligence", "Data Science", "Software Development",
    "Technology", "Cybersecurity", "Networking", "Graphic Design",
    "Art & Creative", "Business & Finance", "Management",
    "Robotics", "Gaming",
]

ALL_PERSONALITIES = ["Analytical", "Creative", "Introvert", "Extrovert"]

DOMAINS = ["All", "Software", "AI", "Networking", "Design", "Business", "Robotics"]
