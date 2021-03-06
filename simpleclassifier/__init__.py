from nltk.tokenize import word_tokenize
from string import punctuation
import json

def processText(text:str):
    """Process the text by removing punctuation.

    Args:
        text (str): User input text.

    Returns:
        [set]: Returns a set with the processed text.
    """
    return {word for word in word_tokenize(text.lower()) if not word in punctuation}

class Classifier:
    def __init__(self, acceptable:int = 50):
        """Return the classifier class.

        Args:
            acceptable (int, optional): Acceptable percentage of similarity.
        """
        self.acceptable = acceptable
        self.process_similaty = lambda input, pattern: (len(input.intersection(pattern)) * 100) // len(pattern)
        self.similaties = {}
    
    def predict(self, patterns:dict, input:set):
        """Process patterns and check input similarities.

        Args:
            patterns (dict): Patterns generated by `trainer.py`.
            input (set): Input processed by `simpleclassifier.processText`.

        Returns:
            Boolean/Tuple: Returns a tuple with the probable answer and similarity.
        """

        for action in patterns:
            for pattern in patterns[action]:
                similaty = self.process_similaty(input, pattern)
                if similaty >= self.acceptable:
                    self.similaties[action] = similaty
                if 100 >= similaty >= self.acceptable + 10:
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

class Trainer:
    def __init__(self):
        """Return the trainer class.
        """
        self.patterns = {}
    
    def add_pattern(self, action:str, pattern:str):
        """Register the pattern in a key with the action name

        Args:
            action (str): The action is the entity responsible for the pattern.
            pattern (str): The pattern to be used as a base.
        """
        pattern = list(processText(pattern))
        if not action in self.patterns:
            self.patterns[action] = []
        self.patterns[action].append(pattern)
    
    def save_patterns(self, directory:str = "base.json"):
        """Save the patterns in a json file.

        Args:
            directory (str, "base.json"): Directory to save.
        """
        with open(directory, "w", encoding="utf8") as f:
            json.dump(self.patterns, f, ensure_ascii=False)