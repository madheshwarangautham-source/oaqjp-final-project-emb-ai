#create an emotion detection application
import requests
import json
def emotion_detector(text_to_analyze):
    url="https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json={ "raw_document": { "text": text_to_analyze } }
    response=requests.post(url,headers=headers,json=input_json)
    return response.text
    
#format the output of application
    response_dict=json.loads(response.text)
    emotion_scores=response_dict[0]["emotion"]
    anger=emotion_scores["anger"]
    disgust=emotion_scores["disgust"]
    fear=emotion_scores["fear"]
    joy=emotion_scores["joy"]
    sadness=emotion_scores["sadness"]
    emotions={"anger":anger,"disgust":disgust,"fear":fear,"joy":joy,"sadness":sadness}
    dominant_emotion=max(emotions,key=emotions.get)
    result={"anger":anger,"disgust":disgust,"fear":fear,"joy":joy,"sadness":sadness,"dominant_emotion":dominant_emotion}
    return result
    

    

