
from app.services.service import sent_to_openai


def process_request_simple(data):

    response_data = sent_to_openai(data)
    
    ## figure out what data we need from user
    response = {
        'status': 'success',
        'data': response_data
    }
    
    return response_data

def process_request_mc(data):
    prompt = data['prompt']
    
    
    response_data = sent_to_openai(prompt)
    
    
    response = {
        'status': 'success',
        'data': response_data
    }
    
    return response


def process_request_tf(data):
    prompt = data['prompt']
    
    
    response_data = sent_to_openai(prompt)
    
    
    response = {
        'status': 'success',
        'data': response_data
    }
    
    return response


