import streamlit as st
import json
import os
from datetime import datetime
import pandas as pd

# Set page config
st.set_page_config(
    page_title="AI Career Pivot for Engineers",
    page_icon="",
    layout="wide"
)

# Define engineer use cases with detailed information
ENGINEER_USE_CASES = {
    "Technical Translators": {
        "description": "Strong technical background, wants to bridge engineering and AI",
        "goal": "Become AI implementation specialists in their engineering domain",
        "timeline": "6-12 months for specialization",
        "focus": "Industry-specific AI applications, technical sales, consulting",
        "example": "Mechanical Engineer ? AI-powered predictive maintenance consultant"
    },
    "Data-Driven Analysts": {
        "description": "Some data analysis experience, wants to go deeper into AI/ML",
        "goal": "Transition to data scientist or AI analyst roles",
        "timeline": "6-18 months for comprehensive skills",
        "focus": "Statistics, machine learning, data visualization, Python proficiency",
        "example": "Process Engineer ? Manufacturing AI Data Scientist"
    },
    "Strategic Pivoteurs": {
        "description": "Senior engineers looking for management/strategy roles in AI",
        "goal": "AI project management, product management, strategic roles",
        "timeline": "3-6 months for business understanding",
        "focus": "AI business applications, project management, strategic thinking",
        "example": "Engineering Manager ? AI Product Strategy Director"
    },
    "Practical Implementers": {
        "description": "Hands-on engineers wanting to implement AI in current industry",
        "goal": "Stay in industry but become the AI expert",
        "timeline": "3-9 months for applied skills",
        "focus": "Industry-specific AI tools, automation, practical applications",
        "example": "Civil Engineer ? Smart Infrastructure AI Specialist"
    },
    "Entrepreneur Builders": {
        "description": "Want to start AI-related business or consulting practice",
        "goal": "Build AI-powered solutions or services",
        "timeline": "6-18 months for comprehensive understanding",
        "focus": "Business + technical skills, market understanding, networking",
        "example": "Aerospace Engineer ? AI-powered drone consulting startup"
    },
    "Career Survivors": {
        "description": "Need immediate employment, AI as job security strategy",
        "goal": "Quick AI literacy for job market competitiveness",
        "timeline": "1-3 months for basic competency",
        "focus": "Rapid skill acquisition, job search optimization, interview prep",
        "example": "Recently laid-off engineer ? AI-aware technical professional"
    }
}

# Timeline-based plans
TIMELINE_PLANS = {
    "3-Month Sprint": {
        "subtitle": "Survival Mode - Immediate Job Needs",
        "focus": "Rapid competency, job search optimization",
        "structure": [
            "Week 1-2: AI fundamentals crash course",
            "Week 3-4: Industry-specific AI applications", 
            "Week 5-8: Python basics + key AI tools",
            "Week 9-12: Portfolio projects, interview prep"
        ]
    },
    "6-Month Strategic": {
        "subtitle": "Balanced Approach - Career Enhancement",
        "focus": "Comprehensive skills with practical application",
        "structure": [
            "Month 1: AI landscape understanding",
            "Month 2-3: Python for AI (Py4AI focus)",
            "Month 4-5: Specialized AI applications",
            "Month 6: Portfolio, networking, job search"
        ]
    },
    "12-Month Mastery": {
        "subtitle": "Deep Transformation - Complete Career Pivot", 
        "focus": "Expert-level knowledge, thought leadership",
        "structure": [
            "Q1: Foundation (AI + Python + Math refresh)",
            "Q2: Specialization (domain-specific AI applications)",
            "Q3: Advanced projects + networking",
            "Q4: Expertise demonstration, job placement"
        ]
    },
    "18+ Month Evolution": {
        "subtitle": "Gradual Transition - Learning While Working",
        "focus": "Learning while working, minimal disruption", 
        "structure": [
            "Months 1-6: Evening/weekend learning, basics",
            "Months 7-12: Skill application in current role",
            "Months 13-18: Transition planning and execution"
        ]
    }
}

# App title and introduction
st.title(" AI Career Pivot for Engineers")
st.markdown("### From Layoff to AI Opportunity")
st.write("*Transform your engineering expertise into AI-powered career advantage*")

st.markdown("""
---
**Welcome, fellow engineer!** 

This assessment is designed specifically for engineers navigating career transitions in the AI era. Whether you've been laid off, are looking to future-proof your career, or want to leverage AI in your engineering domain, this assessment will create a personalized roadmap for your transformation.

> *"Nothing is a mistake. There's no win and no fail. Only MAKE."* - John Cage  
> *Applied to engineering: Every setback is data for your next optimization.*
""")

# Main assessment form
# First, get the use case selection outside the form for real-time updates
st.subheader(" AI Career Pivot Assessment")

# Use Case Selection (outside form for real-time updates)
st.markdown("###  Which Career Path Resonates Most?")
selected_use_case = st.radio(
    "Choose the path that best describes your goals:",
    list(ENGINEER_USE_CASES.keys()),
    help="This will determine your personalized learning plan and focus areas",
    key="use_case_selection"
)

# Show use case details with real-time updates
if selected_use_case:
    st.info(f"**Selected Path:** {selected_use_case}")
    use_case_info = ENGINEER_USE_CASES[selected_use_case]
    
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Description:** {use_case_info['description']}")
        st.write(f"**Goal:** {use_case_info['goal']}")
        st.write(f"**Example:** {use_case_info['example']}")
    with col2:
        st.write(f"**Focus Areas:** {use_case_info['focus']}")
        st.write(f"**Timeline:** {use_case_info['timeline']}")

# Now the main form with all other fields
with st.form("engineer_ai_assessment"):
    
    # Personal & Professional Context
    st.markdown("###  Personal & Professional Background")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name*", placeholder="Enter your full name")
        email = st.text_input("Email*", placeholder="engineer@example.com")
        linkedin = st.text_input("LinkedIn Profile", placeholder="linkedin.com/in/yourprofile")
        location = st.text_input("Current Location", placeholder="City, State/Country")
    
    with col2:
        engineering_discipline = st.selectbox(
            "Engineering Discipline*",
            ["", "Mechanical", "Electrical", "Civil", "Aerospace", "Chemical", "Industrial", "Software", "Other"]
        )
        years_experience = st.selectbox(
            "Years of Engineering Experience*",
            ["", "<2 years", "2-5 years", "5-10 years", "10-15 years", "15+ years"]
        )
        previous_title = st.text_input("Previous Job Title*", placeholder="e.g., Senior Mechanical Engineer")
        company_industry = st.text_input("Company/Industry", placeholder="e.g., Boeing/Aerospace")
    
    col3, col4 = st.columns(2)
    with col3:
        layoff_date = st.selectbox(
            "Layoff Timeline",
            ["Currently employed", "Within last month", "1-3 months ago", "3-6 months ago", "6+ months ago"]
        )
    with col4:
        financial_runway = st.selectbox(
            "Financial Runway",
            ["<3 months", "3-6 months", "6-12 months", "12+ months", "Prefer not to say"]
        )
    
    # Current Situation
    st.markdown("###  Current Situation & Goals")
    col1, col2 = st.columns(2)
    with col1:
        employment_status = st.selectbox(
            "Current Status",
            ["Actively job hunting", "Taking a break", "Exploring options", "Starting job search", "Still employed"]
        )
        job_timeline = st.selectbox(
            "Job Search Timeline",
            ["Need job ASAP", "Within 3 months", "Within 6 months", "Taking time to retrain", "Exploring entrepreneurship"]
        )
        urgency_level = st.selectbox(
            "AI Career Urgency",
            ["Just exploring", "Serious consideration", "Committed to pivot", "Desperate for any opportunity"]
        )
    
    with col2:
        geographic_flexibility = st.selectbox(
            "Geographic Flexibility",
            ["Must stay local", "Willing to relocate", "Open to remote", "Considering different regions"]
        )
        industry_pivot = st.selectbox(
            "Industry Change Willingness",
            ["Stay in same industry", "Adjacent industry", "Completely new industry", "Undecided"]
        )
    
    # Technical Background
    st.markdown("###  Technical Background")
    col1, col2 = st.columns(2)
    with col1:
        programming_exp = st.selectbox(
            "Programming Experience",
            ["None", "Basic scripting", "Some programming", "Moderate coding", "Advanced programmer"]
        )
        
        programming_languages = st.multiselect(
            "Programming Languages Known",
            ["Python", "MATLAB", "C/C++", "Java", "JavaScript", "R", "SQL", "VBA", "None"]
        )
        
        python_level = st.select_slider(
            "Python Experience Level",
            options=["Never used", "Basic scripts", "Comfortable", "Intermediate", "Advanced"],
            value="Never used"
        )
    
    with col2:
        data_analysis_exp = st.selectbox(
            "Data Analysis Experience",
            ["None", "Excel only", "Some statistical tools", "Moderate experience", "Advanced analytics"]
        )
        
        math_comfort = st.select_slider(
            "Math/Statistics Comfort",
            options=["Rusty/Weak", "Basic engineering math", "Comfortable", "Strong", "Advanced"],
            value="Comfortable"
        )
        
        learning_preference = st.selectbox(
            "Technical Learning Preference",
            ["Hands-on projects", "Structured courses", "Documentation reading", "Video tutorials", "Peer learning"]
        )
    
    # AI Knowledge
    st.markdown("###  AI Knowledge & Experience")
    col1, col2 = st.columns(2)
    with col1:
        ai_understanding = st.select_slider(
            "Current AI Understanding",
            options=["Complete beginner", "Heard buzzwords", "Basic concepts", "Some understanding", "Good foundation"],
            value="Complete beginner"
        )
        
        ai_tools_used = st.multiselect(
            "AI Tools Used",
            ["None", "ChatGPT", "GitHub Copilot", "Google Bard/Gemini", "Claude", "Industry-specific AI tools"]
        )
    
    with col2:
        ai_interests = st.multiselect(
            "AI Application Areas of Interest",
            ["Predictive maintenance", "Automation/robotics", "Computer vision", "NLP", "Data analytics", 
             "Process optimization", "Quality control", "Design optimization"]
        )
        
        biggest_concern = st.selectbox(
            "Biggest AI Concern",
            ["Job displacement fears", "Too complex to learn", "Not sure where to start", "Imposter syndrome", "Keeping up with pace"]
        )
    
    # Learning Preferences
    st.markdown("###  Learning Preferences & Capacity")
    col1, col2 = st.columns(2)
    with col1:
        study_time = st.selectbox(
            "Available Study Time per Week",
            ["<5 hours", "5-10 hours", "10-20 hours", "20-30 hours", "Full-time learning"]
        )
        
        learning_formats = st.multiselect(
            "Preferred Learning Formats",
            ["Audio (podcasts/audiobooks)", "Video tutorials", "Text/articles", "Interactive coding", "Live workshops", "Self-paced online"]
        )
        
        timeline_preference = st.selectbox(
            "Preferred Timeline",
            ["3-Month Sprint", "6-Month Strategic", "12-Month Mastery", "18+ Month Evolution"]
        )
    
    with col2:
        audio_context = st.multiselect(
            "Audio Learning Context",
            ["Commuting/car", "Walking/exercise", "Doing chores", "Focused listening", "Background learning"]
        )
        
        video_preference = st.selectbox(
            "Video Learning Preference", 
            ["Short clips (<10min)", "Medium sessions (10-30min)", "Long-form (30min+)", "Live streams", "Recorded lectures"]
        )
        
        hands_on_style = st.selectbox(
            "Hands-on Learning Style",
            ["Theory first", "Immediate practice", "Project-based", "Experiment-driven", "Guided tutorials"]
        )
    
    # Show selected timeline plan
    if timeline_preference:
        st.markdown(f"###  Your Selected Timeline: {timeline_preference}")
        plan_info = TIMELINE_PLANS[timeline_preference]
        
        st.info(f"**{plan_info['subtitle']}**")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Focus:** {plan_info['focus']}")
        with col2:
            st.write("**Structure:**")
            for item in plan_info['structure']:
                st.write(f"• {item}")
    
    # Career Goals
    st.markdown("###  Career Pivot Goals")
    col1, col2 = st.columns(2)
    with col1:
        pivot_motivation = st.selectbox(
            "Primary Motivation",
            ["Financial necessity", "Career growth", "Intellectual curiosity", "Future-proofing", "Industry disruption"]
        )
        
        target_roles = st.multiselect(
            "Target AI Role Types",
            ["AI consultant", "Data analyst/scientist", "AI project manager", "Technical sales (AI products)", 
             "AI trainer/educator", "AI product manager", "AI implementation specialist", "Entrepreneur"]
        )
        
        income_expectations = st.selectbox(
            "Income vs Previous Role",
            ["Significant decrease acceptable", "Moderate decrease ok", "Maintain similar level", "Increase expected"]
        )
    
    with col2:
        industry_target = st.selectbox(
            "Industry Target",
            ["Stay in current industry", "Tech companies", "Consulting firms", "Startups", 
             "Government/defense", "Healthcare", "Finance", "Manufacturing", "Undecided"]
        )
        
        role_preference = st.selectbox(
            "Role Preference",
            ["Individual contributor", "Team lead", "Manager", "Consultant", "Entrepreneur"]
        )
    
    # Investment & Resources
    st.markdown("###  Investment & Resources")
    col1, col2 = st.columns(2)
    with col1:
        learning_budget = st.selectbox(
            "Learning Investment Budget",
            ["$0 - free only", "$100-500", "$500-2000", "$2000-5000", "$5000+", "Company/unemployment funding"]
        )
        
        equipment_status = st.selectbox(
            "Technical Setup",
            ["Need new computer", "Basic setup ok", "Good technical setup", "Advanced setup"]
        )
    
    with col2:
        home_environment = st.selectbox(
            "Home Learning Environment",
            ["Poor/distracting", "Adequate", "Good dedicated space", "Excellent setup"]
        )
        
        family_support = st.selectbox(
            "Family Support Level",
            ["Unsupportive", "Neutral", "Supportive", "Very supportive"]
        )
    
    # Py4AI Interest
    st.markdown("###  Python for AI (Py4AI) Interest")
    col1, col2 = st.columns(2)
    with col1:
        python_ai_interest = st.select_slider(
            "Interest in 'Python for AI' Learning",
            options=["Not interested", "Curious", "Definitely want to learn", "Priority skill"],
            value="Curious"
        )
        
        py4ai_course_interest = st.selectbox(
            "Dr. C's Py4AI Course Interest",
            ["Not sure what this is", "Sounds interesting", "Would definitely take", "Perfect for my needs"]
        )
    
    with col2:
        st.markdown("####  Py4AI Philosophy")
        st.info("**'Just Enough Python to be Dangerous'** - Focus on practical AI applications rather than computer science theory. Perfect for engineers who want to leverage their problem-solving skills with AI tools.")
    
    # Open-ended questions
    st.markdown("###  Your Thoughts")
    biggest_challenge = st.text_area(
        "What's your biggest challenge in making this career pivot?",
        placeholder="What's holding you back or worrying you most about transitioning to AI?",
        height=100
    )
    
    most_exciting = st.text_area(
        "What's the most exciting AI opportunity you see in your field?",
        placeholder="Where do you think AI could make the biggest impact in your engineering domain?",
        height=100
    )
    
    ideal_outcome = st.text_area(
        "Describe your ideal career situation 12 months from now:",
        placeholder="What would success look like for you?",
        height=100
    )
    
    # Submit button
    submitted = st.form_submit_button(" Create My AI Career Plan", type="primary")

# Handle form submission
if submitted:
    if name and email and engineering_discipline and years_experience and previous_title:
        # Create comprehensive assessment data
        assessment_data = {
            "timestamp": datetime.now().isoformat(),
            "personal_info": {
                "name": name,
                "email": email,
                "linkedin": linkedin,
                "location": location,
                "engineering_discipline": engineering_discipline,
                "years_experience": years_experience,
                "previous_title": previous_title,
                "company_industry": company_industry,
                "layoff_date": layoff_date,
                "financial_runway": financial_runway
            },
            "situation": {
                "employment_status": employment_status,
                "job_timeline": job_timeline,
                "urgency_level": urgency_level,
                "geographic_flexibility": geographic_flexibility,
                "industry_pivot": industry_pivot
            },
            "use_case": {
                "selected": selected_use_case,
                "details": ENGINEER_USE_CASES[selected_use_case] if selected_use_case else None
            },
            "technical_background": {
                "programming_exp": programming_exp,
                "programming_languages": programming_languages,
                "python_level": python_level,
                "data_analysis_exp": data_analysis_exp,
                "math_comfort": math_comfort,
                "learning_preference": learning_preference
            },
            "ai_knowledge": {
                "ai_understanding": ai_understanding,
                "ai_tools_used": ai_tools_used,
                "ai_interests": ai_interests,
                "biggest_concern": biggest_concern
            },
            "learning_preferences": {
                "study_time": study_time,
                "learning_formats": learning_formats,
                "timeline_preference": timeline_preference,
                "audio_context": audio_context,
                "video_preference": video_preference,
                "hands_on_style": hands_on_style
            },
            "career_goals": {
                "pivot_motivation": pivot_motivation,
                "target_roles": target_roles,
                "income_expectations": income_expectations,
                "industry_target": industry_target,
                "role_preference": role_preference
            },
            "resources": {
                "learning_budget": learning_budget,
                "equipment_status": equipment_status,
                "home_environment": home_environment,
                "family_support": family_support
            },
            "py4ai_interest": {
                "python_ai_interest": python_ai_interest,
                "py4ai_course_interest": py4ai_course_interest
            },
            "open_responses": {
                "biggest_challenge": biggest_challenge,
                "most_exciting": most_exciting,
                "ideal_outcome": ideal_outcome
            }
        }
        
        # Save assessment data
        json_file = "engineer_ai_assessments.json"
        try:
            if os.path.exists(json_file):
                with open(json_file, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
                    if not isinstance(existing_data, list):
                        existing_data = [existing_data]
            else:
                existing_data = []
            
            existing_data.append(assessment_data)
            
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(existing_data, f, indent=2, ensure_ascii=False)
                
            success_message = True
        except Exception as e:
            success_message = True  # Still show results even if file save fails
        
        # Success message and personalized plan
        st.success(f"Thank you, {name}! You will soon receive your personalized AI career plan via email.")
        st.balloons()
        
        # Generate personalized recommendations
        st.markdown("---")
        st.subheader(" Your Personalized AI Career Transformation Plan")
        
        # Use case summary
        if selected_use_case:
            use_case_info = ENGINEER_USE_CASES[selected_use_case]
            st.markdown(f"""
            ###  Your Path: **{selected_use_case}**
            
            **Profile Match:** {use_case_info['description']}
            
            **Your Goal:** {use_case_info['goal']}
            
            **Recommended Timeline:** {use_case_info['timeline']}
            """)
        
        # Timeline-specific plan
        if timeline_preference:
            plan_info = TIMELINE_PLANS[timeline_preference]
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"""
                #### ? {timeline_preference} Plan
                **{plan_info['subtitle']}**
                
                **Focus:** {plan_info['focus']}
                
                **Your Learning Structure:**
                """)
                for step in plan_info['structure']:
                    st.write(f"• {step}")
            
            with col2:
                st.markdown("####  Immediate Next Steps")
                
                # Customized next steps based on responses
                next_steps = []
                
                if urgency_level == "Desperate for any opportunity":
                    next_steps.extend([
                        " **Priority 1:** Start daily AI news consumption (10 min/day)",
                        " **Priority 2:** Begin free Python basics (Codecademy/freeCodeCamp)",
                        " **Priority 3:** Update LinkedIn profile with 'AI-curious engineer' messaging"
                    ])
                elif urgency_level == "Committed to pivot":
                    next_steps.extend([
                        " **Week 1:** Complete AI fundamentals crash course",
                        " **Week 2:** Start Py4AI or Python basics",
                        " **Week 3:** Join AI engineering communities (LinkedIn/Discord)"
                    ])
                else:
                    next_steps.extend([
                        " **This week:** Research AI applications in your engineering field",
                        " **Next week:** Choose your first AI learning resource",
                        " **This month:** Connect with 5 AI professionals on LinkedIn"
                    ])
                
                for step in next_steps:
                    st.write(step)
        
        # Personalized content recommendations
        st.markdown("###  Your Personalized Learning Content Mix")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("####  Audio Content")
            if "Audio (podcasts/audiobooks)" in learning_formats:
                st.write("**Perfect for your commute/exercise:**")
                audio_recs = []
                if ai_understanding in ["Complete beginner", "Heard buzzwords"]:
                    audio_recs.extend([
                        "• AI for Everyone (Andrew Ng course audio)",
                        "• Lex Fridman Podcast (AI episodes)",
                        "• The AI Podcast by NVIDIA"
                    ])
                if engineering_discipline in ["Mechanical", "Civil", "Aerospace"]:
                    audio_recs.append("• Engineering AI Podcast")
                
                for rec in audio_recs:
                    st.write(rec)
            else:
                st.write("*Audio not preferred - focus on video/text*")
        
        with col2:
            st.markdown("####  Video Content")
            if "Video tutorials" in learning_formats:
                st.write("**Matched to your learning style:**")
                video_recs = []
                if video_preference == "Short clips (<10min)":
                    video_recs.extend([
                        "• Two Minute Papers (AI research)",
                        "• AI Explained (quick concepts)",
                        "• Python in 60 seconds series"
                    ])
                elif video_preference in ["Medium sessions (10-30min)", "Long-form (30min+)"]:
                    video_recs.extend([
                        "• 3Blue1Brown (Neural Networks)",
                        "• Sentdex Python AI tutorials",
                        "• Andrew Ng's AI course videos"
                    ])
                
                for rec in video_recs:
                    st.write(rec)
            else:
                st.write("*Video not preferred - focus on text/audio*")
        
        with col3:
            st.markdown("####  Text Content")
            if "Text/articles" in learning_formats:
                st.write("**For deep understanding:**")
                text_recs = [
                    "• Towards Data Science (Medium)",
                    "• AI research newsletters",
                    "• Industry-specific AI blogs"
                ]
                
                if engineering_discipline == "Mechanical":
                    text_recs.append("• Machine Design AI articles")
                elif engineering_discipline == "Electrical":
                    text_recs.append("• IEEE AI publications")
                
                for rec in text_recs:
                    st.write(rec)
            else:
                st.write("*Text not preferred - focus on audio/video*")
        
        # Py4AI recommendation
        if python_ai_interest in ["Definitely want to learn", "Priority skill"]:
            st.markdown("###  Py4AI - Perfect Match for You!")
            st.success(f"""
            **Why Py4AI is ideal for your situation:**
            
            ? **Engineering Background:** Built for engineers who think in systems and problem-solving
            
            ? **"Just Dangerous Enough":** Focus on practical AI applications, not computer science theory
            
            ? **Time-Efficient:** Designed for {study_time} learning capacity
            
            ? **Industry Relevant:** Applied to {engineering_discipline} engineering contexts
            
            **Next Step:** Contact Dr. C about early access to Py4AI curriculum!
            """)
        
        # Networking recommendations
        st.markdown("###  Strategic Networking Plan")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**LinkedIn Strategy:**")
            st.write("• Update headline: 'Engineering professional transitioning to AI'")
            st.write(f"• Join {engineering_discipline} + AI groups")
            st.write("• Share weekly AI learning insights")
            st.write("• Comment on AI posts from industry leaders")
        
        with col2:
            st.write("**Community Engagement:**")
            st.write("• Join r/MachineLearning + r/EngineeringAI")
            st.write("• Attend local AI/ML meetups")
            st.write("• Follow AI researchers on Twitter/X")
            st.write("• Participate in AI Discord/Slack communities")
        
        # Risk mitigation based on concerns
        if biggest_concern:
            st.markdown("###  Addressing Your Main Concern")
            
            concern_advice = {
                "Job displacement fears": """
                **Reality Check:** AI amplifies human capability rather than replacing it entirely. Engineers who understand AI become invaluable.
                **Action:** Focus on becoming the AI-savvy engineer in your field rather than competing against AI.
                """,
                "Too complex to learn": """
                **Reality Check:** You already mastered complex engineering concepts. AI concepts follow similar logical patterns.
                **Action:** Start with applications in your field - you'll see familiar engineering principles in new contexts.
                """,
                "Not sure where to start": """
                **Reality Check:** You've just created a personalized starting plan above!
                **Action:** Follow your 3-month sprint plan, starting with the immediate next steps listed above.
                """,
                "Imposter syndrome": """
                **Reality Check:** Your engineering background gives you problem-solving skills that many AI enthusiasts lack.
                **Action:** Remember you're adding AI to your engineering expertise, not starting from zero.
                """,
                "Keeping up with pace": """
                **Reality Check:** Focus on fundamentals first. The core concepts evolve slowly; applications evolve quickly.
                **Action:** Master the basics thoroughly, then you can adapt to new applications easily.
                """
            }
            
            if biggest_concern in concern_advice:
                st.info(concern_advice[biggest_concern])
        
        # Show complete assessment data for review
        with st.expander(" View Your Complete Assessment Data"):
            st.json(assessment_data)
            
        # Contact information
        st.markdown("---")
        st.markdown("###  Ready to Start Your Transformation?")
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("""
            ** Dr. C's Guidance Available**
            
            Ready to dive deeper into your AI career transformation?
            
            • Personalized mentoring sessions
            • Py4AI early access
            • Engineering-specific AI curriculum
            • Career transition coaching
            """)
        
        with col2:
            st.success("""
            ** Next Steps:**
            
            1. Check your email for detailed plan
            2. Connect with Dr. C on LinkedIn
            3. Join the Engineers?AI community
            4. Schedule optional strategy call
            
            **Contact:** drC@berkeleyai.edu
            """)
            
    else:
        st.error("? Please fill in all required fields (marked with *).")

# Sidebar with use case information
with st.sidebar:
    st.subheader(" AI Career Paths for Engineers")
    st.write("Explore different transformation strategies:")
    
    for use_case, info in ENGINEER_USE_CASES.items():
        with st.expander(f" {use_case}"):
            st.write(f"**Focus:** {info['focus']}")
            st.write(f"**Timeline:** {info['timeline']}")
            st.write(f"**Example:** {info['example']}")
    
    st.write("---")
    st.subheader(" About Dr. C")
    st.write("""
    **Frank Coyle, PhD**
    - Former Prof. CS & AI (32 years)
    - UC Berkeley Lecturer 
    - Generative AI & LLMs Expert
    - Created Py4AI curriculum
    - Specialized in engineer transitions
    """)
    
    # Assessment statistics
    json_file = "engineer_ai_assessments.json"
    if os.path.exists(json_file):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    st.write("---")
                    st.write("###  Assessment Stats")
                    st.write(f"**Engineers assessed:** {len(data)}")
                    
                    # Show popular paths
                    if len(data) > 0:
                        use_cases = [entry.get('use_case', {}).get('selected', 'Unknown') for entry in data]
                        use_case_counts = {}
                        for uc in use_cases:
                            if uc != 'Unknown':
                                use_case_counts[uc] = use_case_counts.get(uc, 0) + 1
                        
                        if use_case_counts:
                            st.write("**Popular paths:**")
                            for uc, count in sorted(use_case_counts.items(), key=lambda x: x[1], reverse=True)[:3]:
                                st.write(f"• {uc}: {count}")
        except Exception as e:
            pass
    
    st.write("---")
    st.write("*Transform your engineering expertise into AI advantage!*")