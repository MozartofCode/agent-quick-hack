import openai
import sqlite3  # Assuming SQLite for database operations
import dotenv
import os

dotenv()


# Set your OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Function to read prompts from text files
def read_prompt(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Function to generate SQL query using OpenAI
def generate_sql_query(user_input):
    prompt_1 = read_prompt('prompt_1.txt')
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use the appropriate model
        messages=[
            {"role": "system", "content": prompt_1},
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']

# Function to check for SQL vulnerabilities
def check_sql_vulnerability(sql_query):
    safety_prompt = read_prompt('safety_prompt.txt')
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use the appropriate model
        messages=[
            {"role": "system", "content": safety_prompt},
            {"role": "user", "content": sql_query}
        ]
    )
    return response['choices'][0]['message']['content']

# Function to execute SQL query (using SQLite as an example)
def execute_sql_query(sql_query):
    conn = sqlite3.connect('../housing_data.sqlite')  # Connect to your database
    cursor = conn.cursor()
    cursor.execute(sql_query)
    results = cursor.fetchall()
    conn.close()
    return results

# Function to convert SQL results to HTML using OpenAI
def convert_results_to_html(results):
    prompt_2 = read_prompt('prompt_2.txt')
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use the appropriate model
        messages=[
            {"role": "system", "content": prompt_2},
            {"role": "user", "content": str(results)}
        ]
    )
    return response['choices'][0]['message']['content']

# Main function to handle the workflow
def main(user_input):
    # Step 1: Generate SQL query
    sql_query = generate_sql_query(user_input)
    print("Generated SQL Query:", sql_query)

    # Step 2: Check for SQL vulnerabilities
    safety_check = check_sql_vulnerability(sql_query)
    if "unsafe" in safety_check.lower():
        print("SQL Query is unsafe. Aborting execution.")
        return

    # Step 3: Execute SQL query
    results = execute_sql_query(sql_query)
    print("SQL Execution Results:", results)

    # Step 4: Convert results to HTML
    html_output = convert_results_to_html(results)
    print("HTML Output:", html_output)

    # Step 5: Display HTML (or save to file)
    with open('output.html', 'w') as file:
        file.write(html_output)
    print("HTML saved to output.html")

# Example usage
if __name__ == "__main__":
    user_input = "Show all users who have signed up in the last 7 days."
    main(user_input)