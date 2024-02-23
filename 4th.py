import openai
import requests
from DetailsAndRole import*
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
    "messages": [{"role": "user", "content": f"The job I have an interview coming up for a '{Job_Title}' role. The job description for this role is '{Job_Description}'. I will provide the answer to the interview question '{QUESTIONS[num]}'. When I give my answer, I want you to asses my answer on the followign parameters and give a score out of 10 for each parameter.The parameters are '{parameters}.My answer is '{Create(answerfile,num)}'. Give your analysis in a python dictionary, with the parameter as a key, and the value as a list containing the score and justification"}],
    "temperature" : 0,
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
    gp_text = r_json['choices'][0]['message']['content']
    if gp_text[-3] ==',':
        g_text = gp_text[:-3] + gp_text[-2:]
    else:
        g_text=gp_text
    with open('FinalData.txt', 'a') as file:
        print(g_text,file=file)
        print(',',file=file)

if __name__=="__main__":
    #overwrites file to make it blank
    #change filepath

    Analyze('C:/Hacked_Jan6/Metamorphosis/transcribed_text4.txt',3)
