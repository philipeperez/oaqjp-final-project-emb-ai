import requests
import json

def emotion_detector(text_to_analyze: str):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {
        'raw_document': {
            'text': text_to_analyze
        }
    }
    header = {
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'
    }
    response = requests.post(url, json=myobj, headers=header)
    formated_response = json.loads(response.text)

    emotion_predictions = formated_response['emotionPredictions'][0]['emotion']

    res = {**emotion_predictions, 'dominant_emotion': ''}
    greatest_emotion_value = 0

    for k in emotion_predictions:
        if emotion_predictions[k] > greatest_emotion_value:
            greatest_emotion_value = emotion_predictions[k]
            res['dominant_emotion'] = k

    return res
