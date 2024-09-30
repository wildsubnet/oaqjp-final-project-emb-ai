import requests  
import json

def emotion_detector(text_to_analyze):  
    # Define a function named emotion_detector that takes a string input (text_to_analyze)
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    fmt_response = json.loads(response.text)
    emotions=fmt_response['emotionPredictions'][0]['emotion']
    dom_emote = ''
    dom_score = 0
    print("{")
    for emote,score in emotions.items():
        print(f"'{emote}': {score},")
        if score > dom_score:
            dom_emote = emote
            dom_score = score
    emotions['dominant_emotion']=dom_emote
    print(f"'dominant_emotion': '{dom_emote}'")
    print("}")
