'''translator module'''

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



authenticator = IAMAuthenticator('fpJISIzbDOJuE0lO1OF_RbU_lvq1lSL6TRnEWudIS9iw')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)


language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/48f70d11-2fd9-4e2e-87ad-d90fae7bc066')




def english_to_french(english_text):
    '''Takes english text and converts to french'''
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''takes french text and converts to english'''
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text