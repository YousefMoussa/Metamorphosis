import openai
import requests
from DetailsAndRole import Job_Title,Job_Description
from demogpt import QUESTIONS
import re
import json
openai.api_key = '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'
URL = "https://api.openai.com/v1/chat/completions"


parameters = """
1. Technical Skills and Knowledge:
   - Demonstrated ability to articulate acquired knowledge through concrete examples.

2. Critical Thinking:
   - Proficiency in problem-solving, including the capacity to analyze issues and articulate the steps taken to arrive at effective solutions.

3. Communication Skills:
   - Strong communication skills, with the ability to elucidate complex processes in an easily understandable manner. Maintaining a professional demeanor and utilizing appropriate vocabulary.

4. Teamwork and Adaptability:
   - Proven ability to collaborate within a team, showcasing adaptability and cooperation to address significant challenges.
"""
def Create(fileA,n):

    file_path = fileA

    try:
        with open(file_path, 'r') as file:
            # Read the entire content of the file
            content = file.read()
            
            # Alternatively, you can read line by line
            # lines = file.readlines()

            # Print or process the content
            
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return content,n



def Analyze(answerfile,num):
    payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": f"The job I have an interview coming up for a '{Job_Title}' role. The job description for this role is '{Job_Description}'. I will provide the answer to the interview question '{QUESTIONS[num]}'. When I give my answer, I want you to asses my answer on the followign parameters and give a score out of 10 for each parameter. the parameters are '{parameters}. When you give me a score, justify it and provide feedback. My answer is '{Create(answerfile,num)}'. Do not include overall scores"}],
    "temperature" : .2,
    "top_p":1.0,
    "n" : 1,
    "stream": False,
    "presence_penalty":0,
    "frequency_penalty":0,
    
    }
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}"
    }

    response = requests.post(URL, headers=headers, json=payload,stream=True)


    if response.status_code == 200:
        pass
    else:
        print(f"Error: HTTP {response.status_code} - {response.text}")

    r_json = response.json()

    # Access specific fields in the JSON content
    g_text = r_json['choices'][0]['message']['content']
    with open('FinalData.txt', 'a') as file:
        print('QUESTION: ',QUESTIONS[num], file=file )
        print(g_text,file=file)


def text_to_html_list(file_path, output_html):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    html_content = '<html><body><ul>\n'
    
    for line in lines:
        if line.strip():  # Check if line is not empty
            html_content += f'  <li>{line.strip()}</li>\n'
    
    html_content += '</ul></body></html>'

    with open(output_html, 'w') as html_file:
        html_file.write(html_content)

# Example usage
    #overwrites file to make it blank
    
    Analyze('C:/Hacked_Jan6/Metamorphosis/transcribed_text6.txt',5)
    input_file_path = 'path/to/your/textfile.txt'
    output_html_file = 'C:\Hacked_Jan6\Metamorphosis\my-express-app\public\output.html'
    text_to_html_list(input_file_path, output_html_file)
    #scores('C:/Hacked_Jan6/Metamorphosis/FinalData.txt')
    