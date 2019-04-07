from watson_developer_cloud import TextToSpeechV1, WatsonApiException

api_key = 'oUtVqrztJlA_QIym3KyYsYG43yA1FOx1YjKmJcuITvVT'
url = 'https://gateway-lon.watsonplatform.net/text-to-speech/api'

def getSpeechFromText(text):
    text_to_speech = TextToSpeechV1(iam_apikey=api_key, url=url)
    text_to_speech.set_detailed_response(True)

    text_synthezation_results = text_to_speech.synthesize(
        text=text, 
        accept='audio/wav', 
        voice='en-US_AllisonV2Voice'
    ).get_result().content

    return text_synthezation_results

def speechFromText(text):
    try:
        return getSpeechFromText(text)
    except WatsonApiException as ex:
        print('Method failed with status code ' + str(ex.code) + ': ' + ex.message)
        raise Exception('Error with the request to the API')
    except Exception as ex:
        print('Exception while handling the results. Reason: ' + str(ex))
        raise Exception('Error with the request handling')