from spacy import displacy

LABEL = {
    'LOC'     : '地点',
    'ORDINAL' : '序数',
    'QUANTITY': '基数',
}
 
class NamedEntityClient():
    def __init__(self, model, visualize=True):
        self.model = model
        self.visualize = visualize

    def get_ents(self, sentence):
        doc = self.model(sentence)
        html = (
            displacy.render(doc, style="ent") 
            if self.visualize else ''
        )
        ents = [
            {'ent': ent.text, 'label': LABEL[ent.label_]}
            for ent in doc.ents
        ]
        return {'entities': ents, 'html': html}