import openai
import requests
from PDFExtract import *
from DetailsAndRole import *
import json
openai.api_key = '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'
URL = "https://api.openai.com/v1/chat/completions"



pdf='CurrResume.pdf'

#change filepath
ScrapedPdf= extract_text_from_pdf(pdf,'output.txt')
listofresume= clean_file(ScrapedPdf)



payload = {
"model": "gpt-3.5-turbo",
"messages": [{"role": "user", "content": f"My resume formatted as a python list is this '{listofresume}'. The job I have an interview coming up for a '{Job_Title}' role. The job description for this role is '{Job_Description}'.Ask me 6 questions total. The first question should be an easy getting to know the person question. The next two qustions should be based on my resume. The fourth and fifth question should be based on the company/role and how my resume fits in with the job description. The last question should be a bizzare one to test quick thinking and .Include nothing but the questions in your output.add a /n after each question."}],
"temperature" : .5,
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

response = requests.post(URL, headers=headers, json=payload, stream=True)


if response.status_code == 200:
    pass
else:
    print(f"Error: HTTP {response.status_code} - {response.text}")
''''
def convert_to_serializable(obj):
    if callable(obj):
        return str(obj)
    else:
        return obj
    
allstuff=response.json()
allstuff_json = json.dumps(allstuff, indent=2, default=convert_to_serializable)
with open('Questions.json', 'w') as file:
    print(allstuff_json,file=file)
'''
response_json = response.json()

    # Access specific fields in the JSON content
generated_text = response_json['choices'][0]['message']['content']




lines = generated_text.strip().split('\n')
# Create variables for each question
question_1 = lines[0][3:].strip()
question_2 = lines[1][3:].strip()
question_3 = lines[2][3:].strip()
question_4 = lines[3][3:].strip()
question_5 = lines[4][3:].strip()
question_6 = lines[5][3:].strip()
QUESTIONS=[question_1,question_2,question_3,question_4,question_5,question_6]

if __name__ == "__main__":


    for index, string_value in enumerate(QUESTIONS):
        # Construct a unique filename for each string
        filename = f'C:\Hacked_Jan6\Metamorphosis\my-express-app\public\output_{index + 1}.json'

        # Convert the string to a JSON-formatted string
        json_string = json.dumps([string_value], indent=2)

        # Writing to the file in 'w' mode (overwrite existing content)
        with open(filename, 'w') as json_file:

            json_file.write((json_string))

        print(f'Successfully wrote to {filename}')

