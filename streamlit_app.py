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
st.title('Chart Generator - DEMO')
st.write('The following is a demo of the use of LLMs to generate parameters for use in a dynamic chart making webapp')

openai.api_key = st.secrets["OpenAIapikey"]

# Input Query
st.write('Please input your query to generate the appropriate chart:')
query_text = st.text_input('Enter Query')

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


    
    
if query_text is not None:   
        print("we have a query now")
        # FETCH RESPONSE

        messages=[
        {"role": "system", "content": "You are a data analyst who needs to take a request for a chart and convert that into specific parameters. The parameters are: Type: bar/pie/line, Dimension: time/channel/device, Metric: Sessions/ Users/ Revenue/ Transactions/ CVR, StartDate: [yyyy/mm/dd], End Date: [yyyy/mm/dd]. Todays date is 2023/09/07. Where a date range is not specified use a start date of 31 days ago and end date of yesterday The response should be a JSON object of these parameters. When a line chart is requested the dimension should be time and we should add a parameter for breakdown dimension called BreakdownDimension. "},
        {"role": "user", "content": query_text}
        ]
        
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            temperature = 0.1,
            stop = None,
            messages=messages)
        
        
        response_text = response.choices[0].message.content
        response_text = response_text.replace('\n', ' ').lower()

        LLMresponse = response_text
        st.write("so the thinking is done")
        st.write(LLMresponse
        
        #print(response_text)
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
        #placeurl = quote(places)
