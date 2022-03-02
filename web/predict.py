from googletrans import Translator
import torch
detoxify = torch.load('./web/model/detoxify.pt')



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
        return detoxify('original').predict(sentence)