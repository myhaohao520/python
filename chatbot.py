#!/usr/bin/env python3

###This program is a simple ChatGPT powered chatbot###

#Import openai package to access ChatGPT language model
import openai

#Use your openAI API key to use ChatGPT
openai.api_key = "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"

#Create function to call route the parameter prompt into the function that generates a response from
the given prompt
def get_openai_response(prompt):
response = openai.Completion.create(
engine=&quot;davinci&quot;, # the OpenAI engine to use for the response
prompt=prompt, # the user&#39;s input
max_tokens=1024, # the maximum number of tokens to generate in the response
n=1, # the number of responses to generate
stop=None, # when to stop generating the response
temperature=0.5, # the &quot;creativity&quot; of the response
)
return response.choices[0].text.strip() # return the generated response

#Create a while loop to ask the user for an input and route the input into the function call as long as the
user doesn’t input the two words: exit or quit
while True:
user_input = input(&quot;User: &quot;) #ask user for an input
if user_input.lower() in [&quot;exit&quot;, &quot;quit&quot;]: #stops running when the user enters exit or quit
break

RE
ST
RIC
TE
D

response = get_openai_response(user_input) #store the response from the function call
print(&quot;Bot:&quot;, response) #display the response
