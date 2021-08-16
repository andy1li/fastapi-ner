from ner_client import NamedEntityClient
from collections import namedtuple

Doc = namedtuple('Doc', ['ents'])
Span = namedtuple('Span', ['text', 'label_'])

def ModelTestDouble(ents):
    return lambda sentence: Doc(
        ents = [Span(ent['text'], ent['label_']) for ent in ents]
    )

def NERClientTestDouble(ents):
    model = ModelTestDouble(ents)
    return NamedEntityClient(model, visualize=False)