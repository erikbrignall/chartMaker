import openai
import pandas as pd
import re #regex for extracting data from response
from urllib.parse import quote # for url encoding for place lookup
import requests
import time
import json
import streamlit as st

st.set_page_config(page_title='Chart Maker - DEMO')
st.image('logo-temp2.PNG', width=200)
st.title('API for chart generation - DEMO')
st.write('The following is a test UI for the LLM chart generator parameters API. For incendium eyes only :-)')

#openai.api_key = st.secrets["OpenAIapikey"]

# Input Query
with st.form(key='my_form_to_submit'):
    st.write('Please input your query to generate the appropriate chart:')
    query_text = st.text_input('Enter Query')
    submit_button = st.form_submit_button(label='Submit')


## The below function loops through the JSON structure and returns any value matching the key
def extract_values(obj, key):
        """Pull all values of specified key from nested JSON."""
        arr = []

        def extract(obj, arr, key):
            """Recursively search for values of key in JSON tree."""
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        extract(v, arr, key)
                    elif k == key:
                        arr.append(v)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr

        results = extract(obj, arr, key)
        return results


    
if submit_button:    
#if query_text is not None:   
        #print("we have a query now")
        # FETCH RESPONSE
        st.write("here is the json request:")

        url = "https://europe-west2-alt24-developments.cloudfunctions.net/chartmaker2"
        
        apikey = "xxxx"
        request_data = {"input": query_text, "apikey": apikey}
        st.write(request_data)
        start_time = time.time()
        response = requests.post(url, json=request_data)
        end_time = time.time()
        
        LLMresponse = response
        st.write("Here is the JSON response:")
        #st.json(LLMresponse)
        st.write(response.json())
        #print(response.status_code)
        #print(response.json())
        #print(response)
        
        response_time = end_time - start_time
        st.write(f"API Response Time: {response_time} seconds")
        
        ## extract individual elements from response
        
        ## TITLE
        #pattern = r'title: (.*?)summary:'
        #match = re.findall(pattern, response_text)
        #art_title = match[0]
        
        ## SUMMARY
        #pattern = r'summary: (.*?)places:'
        #match = re.findall(pattern, response_text)
        #art_summary = match[0]
        
        ## PLACES
        #pattern = r'places: (.*)'
        #match = re.findall(pattern, response_text)
        #places = match[0]
        #placeurl = quote(places)'''
