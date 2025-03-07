Creating a complete Python program for an automated environmental impact assessment tool like "green-inspect" involves several steps. I'll provide a basic structure for the program, focusing on input handling, a mock assessment process, and reporting. Keep in mind that a real-world implementation would require significant domain expertise, access to environmental data, and possibly machine learning models for accurate assessments. Below is a simplified version of how you might set this up:

```python
import json

class EnvironmentalImpactAssessment:
    def __init__(self, project_data):
        self.project_data = project_data
        self.assessment_result = {}

    def assess_resource_usage(self):
        try:
            resource_usage = self.project_data.get('resource_usage', {})
            self.assessment_result['resource_efficiency'] = "Good" if resource_usage.get('efficiency_score', 0) > 70 else "Poor"
        except Exception as e:
            print(f"Error in assessing resource usage: {e}")
            self.assessment_result['resource_efficiency'] = "Error"

    def assess_water_impact(self):
        try:
            water_usage = self.project_data.get('water_usage', {})
            self.assessment_result['water_impact'] = "Acceptable" if water_usage.get('impact_score', 0) < 50 else "High"
        except Exception as e:
            print(f"Error in assessing water impact: {e}")
            self.assessment_result['water_impact'] = "Error"

    def assess_pollution_levels(self):
        try:
            pollution = self.project_data.get('pollution', {})
            air_pollution = pollution.get('air', 0)
            water_pollution = pollution.get('water', 0)
            self.assessment_result['pollution_level'] = "Low" if (air_pollution + water_pollution) < 100 else "High"
        except Exception as e:
            print(f"Error in assessing pollution levels: {e}")
            self.assessment_result['pollution_level'] = "Error"

    def assess_biodiversity_impact(self):
        try:
            biodiversity = self.project_data.get('biodiversity', {})
            self.assessment_result['biodiversity_impact'] = "Significant" if biodiversity.get('species_affected', 0) > 5 else "Minimal"
        except Exception as e:
            print(f"Error in assessing biodiversity impact: {e}")
            self.assessment_result['biodiversity_impact'] = "Error"

    def perform_assessment(self):
        print("Starting environmental impact assessment...")
        self.assess_resource_usage()
        self.assess_water_impact()
        self.assess_pollution_levels()
        self.assess_biodiversity_impact()
        print("Assessment complete.")

    def generate_report(self):
        try:
            report = {
                "Summary": "Environmental Impact Assessment Report",
                "Project Name": self.project_data.get('project_name', 'Unnamed Project'),
                "Assessment Results": self.assessment_result
            }
            return report
        except Exception as e:
            print(f"Error in generating report: {e}")
            return {"error": "Failed to generate report"}

def load_project_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Project data file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON from file.")
        return {}

def main():
    file_path = "sample_project_data.json"  # Example path to the input data file
    project_data = load_project_data(file_path)
    
    if project_data:
        assessment = EnvironmentalImpactAssessment(project_data)
        assessment.perform_assessment()
        report = assessment.generate_report()
        print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
```

### Key Components of the Program:

1. **Data Loading:** Loads project-specific data from a JSON file. This could include details about resource usage, water impact, pollution levels, and biodiversity.

2. **Assessment Procedures:** The class `EnvironmentalImpactAssessment` includes methods for evaluating different environmental factors. These methods currently use simple conditional logic to derive assessment results.

3. **Error Handling:** Uses `try-except` blocks to manage potential issues during data access and processing.

4. **Report Generation:** Compiles the results into a structured report, which is printed in JSON format.

For a real-life application, it's critical to involve environmental experts to refine the logic behind assessments, obtain accurate data sources, potentially incorporate advanced analytics or machine learning, and maintain compliance with regulatory standards.