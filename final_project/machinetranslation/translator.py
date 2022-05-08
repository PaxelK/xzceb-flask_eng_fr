import os
from ibm_watson import LanguageTranslatorV3
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2022-05-06',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    #write the code here
    if english_text is None:
        return "Input value is None"
    try:
    # Invoke a method
        #languages = language_translator.list_languages().get_result()
        #print(json.dumps(languages, indent=2))

        # Translates input and grabs the string out of dict -> list -> dict
        french_text = language_translator.translate(english_text,
        model_id='en-fr').get_result()["translations"][0]['translation']
        #print(french_text)
    except ApiException as ex:
        french_text = "Method failed with status code " + str(ex.code) + ": " + ex.message
    return french_text

def french_to_english(french_text):
    #write the code here
    if french_text is None:
        return "Input value is None"
    try:
    # Invoke a method
        #languages = language_translator.list_languages().get_result()
        #print(json.dumps(languages, indent=2))

        # Translates input and grabs the string out of dict -> list -> dict
        english_text = language_translator.translate(french_text,
        model_id='fr-en').get_result()["translations"][0]['translation']
        #print(english_text)
    except ApiException as ex:
        english_text = "Method failed with status code " + str(ex.code) + ": " + ex.message
    return english_text

if __name__ == '__main__':
    print(english_to_french("Hi, how are you?"))
    print(french_to_english("Salut, comment tu es?"))

    print(english_to_french(None))
