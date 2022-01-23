<h1 align="center">NLP Classifier</h1>
A simple text classifier that uses similarities between the text and the database to tell which entity is responsible.

The classifier documentation: [Documentation](https://github.com/Masso13/NLP-Classifier/wiki)

### Video:
<a href="https://youtu.be/UQf05o1ontE"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white"></a>

### Requirements:
* [Python 3.7.2](https://www.python.org/downloads/release/python-372/)
* [NLTK](https://pypi.org/project/nltk/)
```bash
pip install nltk==3.6.2
```

### How to use:
```python
# First, import the labries
import json, simpleclassifier
```


```python
# Second, open the database
with open("base.json", "r", encoding="utf8") as f:
    patterns = json.load(f)
```

```python
# Third, process your input
input_process = simpleclassifier.processText(str(input("Input > ")))
```

```python
# Fourth, create the classifier and predict output
classifier = simpleclassifier.Classifier()

output = classifier.predict(patterns, input_process)
```

### Create Database:
```python
# Create the Trainer
trainer = simpleclassifier.Trainer()

# Register the pattern and save
trainer.add_pattern("calculadora", "quanto é")
trainer.save_patterns(r"C:\Users\Masso\Desktop\base.json")

# Get patterns in Trainer
patterns = trainer.patterns
```
```json
{
    "wikipedia": [
        [
            "quem",
            "foi"
        ],
        [
            "quem",
            "é"
        ],
        [
            "quando",
            "foi"
        ],
        [
            "quando",
            "foi",
            "que"
        ],
        [
            "quando",
            "é"
        ],
        [
            "onde",
            "foi"
        ],
        [
            "onde",
            "é"
        ],
        [
            "o",
            "que",
            "é"
        ]
    ],
    "calculadora": [
        [
            "quanto",
            "é"
        ]
    ],
    "relogio": [
        [
            "quantas",
            "horas",
            "são"
        ],
        [
            "que",
            "horas",
            "são"
        ]
    ]
}
```
