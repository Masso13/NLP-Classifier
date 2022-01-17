from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation

stopwords = set(stopwords.words("portuguese") + list(punctuation))

def processText(text:str):
    palavras = {palavra for palavra in word_tokenize(text.lower()) if not palavra in punctuation}
    return palavras

class Classifier:
    def __init__(self):
        '''
        Return the classifier class
        '''
        self.process_similaty = lambda input, pattern: (len(input.intersection(pattern)) * 100) // len(pattern)
        self.similaties = {}
    
    def predict(self, patterns:dict, input:set):
        """Process patterns and check input similarities

        Args:
            patterns (dict): Patterns generated by `trainer.py`
            input (set): Input processed by `simpleclassifier.processText`

        Returns:
            Boolean/Tuple: Returns a tuple with the probable answer and similarity
        """

        for action in patterns:
            for pattern in patterns[action]:
                similaty = self.process_similaty(input, pattern)
                if similaty >= 50:
                    self.similaties[action] = similaty
                if 100 >= similaty >= 60:
                    break
        
        probably = False
        if len(self.similaties) > 1:
            for action in self.similaties:
                if not probably:
                    probably = action
                elif self.similaties[action] > self.similaties[probably]:
                    probably = action
        elif len(self.similaties) == 1:
            for action in self.similaties:
                probably = action
        return False if not probably else (probably, self.similaties[probably])