import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import blood_test_analyst, article_researcher, health_advisor
from tasks import analyze_blood_test_task, find_articles_task, provide_recommendations_task


# Load environment variables
load_dotenv()



# Create a Crew and execute tasks
crew = Crew(
    agents=[blood_test_analyst, article_researcher, health_advisor],
    tasks=[analyze_blood_test_task, find_articles_task, provide_recommendations_task],
    verbose=True
)

results = crew.kickoff()

# Convert results to a string
results_str = str(results)

# Define the file name
output_file = "results1.md"

# Write the results to the file
with open(output_file, "w") as file:
    file.write("# Analysis Results\n\n")
    file.write(results_str)

print(f"Results have been written to {output_file}")
