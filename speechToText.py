from watson_developer_cloud import SpeechToTextV1, WatsonApiException
from watson_developer_cloud.speech_to_text_v1 import SpeechRecognitionAlternative

api_key = 'fLB0Gp_gaUM8UnNnneBEy2rWnalqpbRLvDZE2zgkSfw_'
url = 'https://gateway-lon.watsonplatform.net/speech-to-text/api'
        
def getTextFromFile(audio_file):
    speech_to_text = SpeechToTextV1(iam_apikey=api_key, url=url)
    speech_to_text.set_detailed_response(True)

    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/wav',
        timestamps=True
    ).get_result()['results']

    result = speech_recognition_results[0]
    alternatives = result['alternatives']
    alternative = (SpeechRecognitionAlternative)(alternatives[0])
    transcript = alternative.transcript['transcript']
    return transcript

def textFromSpeech(audio_file):
    try:
        return getTextFromFile(audio_file)
    except WatsonApiException as ex:
        print('Method failed with status code ' + str(ex.code) + ': ' + ex.message)
        raise Exception('Error with the request to the API')
    except Exception as ex:
        print('Exception while handling the results. Reason: ' + str(ex))
        raise Exception('Error with the request handling')