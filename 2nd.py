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

def scores(FatFile):
    with open(FatFile, 'r') as file:
        file_content = file.read()

        # Define a regular expression pattern to match the score
        score_pattern = r"(\d+)/10"

        # Find all matches in the file content
        score_matches = re.findall(score_pattern, file_content)
        score_matches= [int(score) for score in score_matches]
        array4=[score_matches[0:4],score_matches[4:8],score_matches[8:12],score_matches[12:16],score_matches[16:20],score_matches[20:]]
        # Convert the matched strings to integers and append to a list


        # Print the extracted scores
        sum1 = sum(row[0] for row in array4)
        sum2 = sum(row[1] for row in array4)
        sum3 = sum(row[2] for row in array4)
        sum4 = sum(row[3] for row in array4)
        sums=[sum1,sum2,sum3,sum4]
        for i in range(4):
        # Construct a unique filename for each string
            filename = f'average_{i + 1}.json'
            jstring = json.dumps([str(sum1)], indent=2)
            with open(filename, 'w') as json_file:

                json_file.write((jstring))
if __name__=="__main__":
    #overwrites file to make it blank
    
    Analyze('C:/Hacked_Jan6/Metamorphosis/transcribed_text2.txt',1)
    