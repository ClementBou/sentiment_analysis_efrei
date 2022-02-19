from detoxify import Detoxify
from googletrans import Translator


def checking_language(sentence):
    t = Translator()
    res = t.detect(sentence)
    if res.lang == 'en':
        return 1
    else:
        return 0

def predict(sentence):
    if checking_language(sentence) == 0:
        raise Exception("The text language used must be English")
    else:
        results = Detoxify('original').predict(sentence)
        print(results)

        if results['toxicity']:
            return "Toxic"
        elif results['severe_toxicity']:
            return "Severe Toxic"
        elif results['obscene']:
            return "Obscene"
        elif results['threat']: 
            return "Threat"
        elif results['insult']:
            return "Insult"
        elif results['identity_attack']:
            return "Indetity attack"


print(predict(str("yes")))