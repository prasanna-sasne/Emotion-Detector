import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputJson = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, headers=headers, json=inputJson)
    
    # convert to json
    formatted_output = response.json()

    try:
        emotions = formatted_output['emotionPredictions'][0]['emotion']
        #dominant_emotion = max(emotions, key=emotions.get)

        return {
            **emotions,
            'dominant_emotion': max(emotions, key=emotions.get)
        }

    except(keyError, indexError):
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }