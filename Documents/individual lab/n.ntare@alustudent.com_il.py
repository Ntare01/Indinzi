class Assignment:
    """Represents a single assignment with details about its type, score, and weight."""
    
    def __init__(self, name, assignment_type, score, weight):
        self.name = name
        self.assignment_type = assignment_type
        self.score = score
        self.weight = weight
        
        # Validate the score and weight
        self.validate_score_and_weight()
        
    def validate_score_and_weight(self):
        if not (0 <= self.score <= 100):
            raise ValueError("Score must be between 0 and 100.")
        if not (0 <= self.weight <= 100):
            raise ValueError("Weight must be between 0 and 100.")


class Student:
    """Represents a student with assignments and calculates progression based on scores."""
    
    def __init__(self):
        self.assignments = []
        self.formative_weight_total = 0
        self.summative_weight_total = 0
    
    def add_assignment(self, assignment):
        if assignment.assignment_type == "Formative":
            if self.formative_weight_total + assignment.weight > 60:
                raise ValueError("Total formative weight cannot exceed 60%.")
            self.formative_weight_total += assignment.weight
        elif assignment.assignment_type == "Summative":
            if self.summative_weight_total + assignment.weight > 40:
                raise ValueError("Total summative weight cannot exceed 40%.")
            self.summative_weight_total += assignment.weight
        self.assignments.append(assignment)

    def calculate_weighted_scores(self):
        formative_total, summative_total = 0, 0
        for assignment in self.assignments:
            weighted_score = (assignment.score * assignment.weight) / 100
            if assignment.assignment_type == "Formative":
                formative_total += weighted_score
            elif assignment.assignment_type == "Summative":
                summative_total += weighted_score
        return formative_total, summative_total

    def determine_progression(self):
        formative_total, summative_total = self.calculate_weighted_scores()
        if formative_total >= 30 and summative_total >= 20:
            return "Pass"
        else:
            return "Fail - Retake Course"

    def resubmission_eligibility(self):
        resubmissions = [a for a in self.assignments if a.assignment_type == "Formative" and a.score < 50]
        return resubmissions

    def generate_transcript(self, order="ascending"):
        transcript = sorted(self.assignments, key=lambda x: x.score, reverse=(order == "descending"))
        print("Transcript Breakdown:")
        print(f"{'Assignment':<15} {'Type':<15} {'Score(%)':<10} {'Weight(%)':<10}")
        print("-" * 50)
        for a in transcript:
            print(f"{a.name:<15} {a.assignment_type:<15} {a.score:<10} {a.weight:<10}")


# Main code to test functionality
if __name__ == "__main__":
    student = Student()
    # Example assignments
    student.add_assignment(Assignment("Assignment 1", "Formative", 45, 15))
    student.add_assignment(Assignment("Assignment 2", "Formative", 90, 10))
    student.add_assignment(Assignment("Midterm", "Summative", 34, 20))
    student.add_assignment(Assignment("Final Exam", "Summative", 95, 20))

    # Display Transcript
    student.generate_transcript(order="ascending")

    # Check Progression
    print("Course Progression:", student.determine_progression())

    # Check Resubmission Eligibility
    resubmissions = student.resubmission_eligibility()
    if resubmissions:
        print("Assignments eligible for resubmission:")
        for a in resubmissions:
            print(a.name)
    else:
        print("No assignments eligible for resubmission.")

