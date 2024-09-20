import csv

csv_file_path = '/Users/xiayuxuan/Desktop/SI339/deliverable2/data_pupulation/37th_Early_Bird_Open_Mens_5000_Meters_HS_Open_5K_24.csv'
html_meet= 'meet1.html'
template_file = '/Users/xiayuxuan/Desktop/SI339/deliverable2/meet_template.html'
# Reading the CSV file to examine its structure and content
with open(csv_file_path, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    csv_data = list(reader)

# Displaying the first few rows of the CSV file to understand its structure
print(csv_data[:10])  # Showing first 10 rows

# Extracting data from CSV for populating the HTML template

# Meet information
meet_name = csv_data[0][0]  # Meet name (Row 1, first column)
meet_date = csv_data[1][0]  # Meet date (Row 2, first column)
team_results_link = csv_data[2][0]  # Team results link (Row 3, first column)

# Extract team results (rows after header "Place", "Team", "Score")
team_results = []
for row in csv_data[7:]:  # Start after the table header in row 7
    if len(row) == 3:  # Ensure each row has the correct number of columns
        place, team_name, score = row
        team_results.append({'place': place, 'team_name': team_name, 'score': score})
team_row = ''

for team in team_results:
    team_row += f'''
    <tr>
        <td>{team['place']}</td>
        <td>{team['team_name']}</td>
        <td>{team['score']}</td>
    </tr>
    '''

# athlete_details = [
#     {
#         'name': 'Matthew Guikema', 
#         'time': '17:35.10', 
#         'place': '1', 
#         'image': 'images/matthew_guikema.jpg',  # Placeholder for image path
#         'feedback': 'Led the team with a strong performance.'
#     },
#     {
#         'name': 'Nicholas Yuan', 
#         'time': '17:44.40', 
#         'place': '2', 
#         'image': 'images/nicholas_yuan.jpg', 
#         'feedback': 'Followed closely with an excellent time.'
#     },
#     {
#         'name': 'Oskar MacArthur', 
#         'time': '18:37.50', 
#         'place': '3', 
#         'image': 'images/oskar_macarthur.jpg', 
#         'feedback': 'Achieved a personal record.'
#     },
#     # Additional athletes could be extracted similarly from the paragraph description
# ]
athlete_results = []
for row in csv_data[7:]:  # Start after the table header in row 7
    if len(row) == 8:  # Ensure each row has the correct number of columns
        place, _, name, _, time, team, _, _ = row
        if team == "Ann Arbor Skyline":
            print("test")
            athlete_results.append({'place': place, 'name': name, 'time': time, 'team': team})
athlete_rows = ''
for athlete in athlete_results:
    athlete_rows += f'''
    <tr>
        <td>{athlete['name']}</td>
        <td>{athlete['time']}</td>
        <td>{athlete['place']}</td>
    </tr>
    '''
with open(template_file,'r', encoding='utf-8') as f:
    html_template = f.read()
html_content = html_template.replace('{{meet_name}}', meet_name).replace('{{meet_date}}', meet_date).replace('{{team_rows}}',  team_row).replace('{{athlete_rows}}', athlete_rows)

with open(html_meet, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML file '{html_meet}' has been created successfully.")





# team_rows = ''
# for team in team_results:
#     team_rows += f'''
#     <tr>
#         <td>{team['place']}</td>
#         <td>{team['team_name']}</td>
#         <td>{team['score']}</td>
#     </tr>
#     '''





