import csv

# Path to the CSV file and the output HTML file
csv_file = 'Vera Naines18895017.csv'
html_file = 'athlete.html'
template_file = 'athlete_template.html'

# Open the CSV file and extract the data
with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

# The athlete's name should come from the first row
athlete_name = data[0][0]  # Corrected to fetch the athlete's name from the first row

overall_places = []
grades = []
times = []
dates = []
meets = []

# Extract the data from the CSV (starting from row 2 to skip the athlete number)
for row in data[2:]:  # Start from row 2 to skip the first two rows
    if row and len(row) >= 6 and row[0] == athlete_name:  # Check for row validity
        overall_places.append(row[1] if row[1] else "N/A")  # Handle missing overall places
        grades.append(row[2] if row[2] else "N/A")  # Handle missing grades
        times.append(row[3] if row[3] else "N/A")  # Handle missing times
        dates.append(row[4] if row[4] else "N/A")  # Handle missing dates
        meets.append(row[5] if row[5] else "N/A")  # Handle missing meet names

# Generate the rows for the athlete's results
meet_rows_for_athlete = ''
for place, grade, time, date, meet in zip(overall_places, grades, times, dates, meets):
    meet_rows_for_athlete += f'''
        <tr>
            <td>{place}</td>
            <td>{grade}</td>
            <td>{time}</td>
            <td>{date}</td>
            <td>{meet}</td>
        </tr>
    '''

# Read the HTML template file
with open(template_file, 'r', encoding='utf-8') as f:
    html_template = f.read()

# Replace placeholders in the template with actual data
html_content = html_template.replace('{{ athlete_name }}', athlete_name).replace('{{ meet_rows }}', meet_rows_for_athlete)

# Write the populated HTML content to a file
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML file '{html_file}' has been created successfully.")


