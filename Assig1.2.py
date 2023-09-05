import spacy
nlp = spacy.load("en_core_web_sm")
conference_help_text = (
    "The man who does not read books has no advantage over the one who cannot read them."
    "Teachers can open the door,but you must enter it yourself."
)
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")
        
#----------output--------------#
"""The : the
                does : do
               books : book
                 has : have
                them : they
            Teachers : teacher
                 The : the
            learning : learn
                  is : be
           Education : education
                  is : be"""