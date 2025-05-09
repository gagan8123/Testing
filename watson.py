from langchain_ibm import WatsonxLLM


parameters = {
    "decoding_method": "sample",
    "max_new_tokens": 100,
    "min_new_tokens": 1,
    "temperature": 0.5,
    "top_k": 50,
    "top_p": 1,
}

model = WatsonxLLM(apikey='9dhWazh67-KWTUjf80FnPsmEUx828u1vid3PNrFAmuSS',
project_id='52cf4e44-2a8c-474d-b247-11957cc6891d',url='https://us-south.ml.cloud.ibm.com',model_id='meta-llama/llama-3-1-70b-instruct',params=parameters)

while True:
    prompt = input('user: ')
    response = model.invoke(prompt)
    print('model:', response)
