# blood_report_analysis

This project uses the CrewAI framework to analyze blood test reports, search for relevant health articles, and provide personalized health recommendations.

## Workflow and Approach

1. **Understanding the Requirements**
   - Analyzed the assignment to identify key components: blood test analysis, web search, and health recommendations.
   - Decided to use CrewAI framework as specified, with Google's Gemini Pro model for AI capabilities.

2. **Setting Up the Environment**
   - Installed necessary libraries: CrewAI, PyPDF2, google-generativeai.
   - Set up API keys for Google (Gemini) and Serper.dev for web searching.

3. **Designing the Agent Crew**
   - Created three specialized agents to handle different aspects of the task:
     a. Blood Test Analyst: For interpreting the blood test report.
     b. Medical Research Specialist: For finding relevant health articles.
     c. Holistic Health Advisor: For providing health recommendations.

4. **Implementing PDF Text Extraction**
   - Used PyPDF2 to extract text from the blood test report PDF.
   - Ensured all pages of the report are processed for comprehensive analysis.

5. **Crafting Agent Tasks**
   - Defined specific tasks for each agent:
     a. Analyze Blood Test: Detailed analysis of the report with clear explanations.
     b. Find Articles: Search for relevant, high-quality medical articles based on test results.
     c. Provide Recommendations: Synthesize analysis and research into actionable advice.

6. **Integrating Web Search Tools**
   - Implemented SerperDevTool for general internet searches.
   - Added WebsiteSearchTool for more focused, semantic searches on specific websites.

7. **Structuring the Workflow**
   - Organized tasks in a logical sequence: analysis → research → recommendations.
 
8. **Testing and Refinement**
   - Tested the system with sample blood test reports to ensure accuracy and reliability.
   - Refined agent prompts and task descriptions to improve output quality.

This approach allowed for a modular, extensible system that can analyze blood test reports, find relevant health information, and provide personalized recommendations, meeting all the requirements of the assignment.

## Setup Guide

Follow these steps to set up and run the project:

1. **Clone the Repository**
    ```
    git clone https://github.com/Harsh-svg988/Blood-Report_Analyzer.git
    cd  blood_report_analysis
    ```
2. **Set Up Virtual Environment**
    open terminal and run 
    ```
    python -m venv venv
    ```
3. **Activate Virtual Environment**
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. **Install Dependencies**
    run
    ```
    pip install -r requirement.txt
    ```
5. **Create a .evn file and set up environment variables**
- Set the API key as an environment variable:
  ```
    GOOGLE_API_KEY='your-api-key'
    SERPER_API_KEY = 'your-api-key'
  ```
- for reference you can look at the .env.example file

7. **Run the Script**
    ```
    python main.py
    ```
And now it will give you the result file as results.md