import random

def generate_realistic_grades(num_grades=500):
    """
    Generate realistic grade distribution similar to a high school class.
    Uses a normal distribution centered around 75-80 with appropriate spread.
    """
    grades = []
    
    for _ in range(num_grades):
        # Normal distribution: mean=77, std_dev=12
        # This creates a realistic bell curve with most grades in B-C range
        grade = random.gauss(77, 12)
        
        # Clamp between 0 and 100
        grade = max(0, min(100, grade))
        
        # Round to nearest integer
        grade = round(grade)
        
        grades.append(grade)
    
    return grades

# Generate grades
'''   
grades = generate_realistic_grades(500)

# Write to file
with open('score.txt', 'w') as f:
    for grade in grades:
        f.write(f"{grade}\n")

print(f"Generated {len(grades)} grades in score.txt")
'''

# Read grades from score1.txt and count letter grades
grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

with open('score1.txt', 'r') as f:
    for line in f:
        score = int(line.strip())
        
        if score >= 90:
            grade_counts['A'] += 1
        elif score >= 80:
            grade_counts['B'] += 1
        elif score >= 70:
            grade_counts['C'] += 1
        elif score >= 60:
            grade_counts['D'] += 1
        else:
            grade_counts['F'] += 1

# Display results
print("Letter Grade Distribution:")
for letter, count in grade_counts.items():
    print(f"{letter}: {count} students")