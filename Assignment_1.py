##Assignment No.01##
#Name:Shweta Narendra Bhavsar
##Roll No:05
#Batch:B1
#Title:"Text Pre-Processing using NLP operations:perform Tokenization
# Stop word removal,Lemmatization ,Part-of-Speech Tagging use any sample text"

#import Libraries
import spacy
#language model loaded
nlp = spacy.load("en_core_web_sm")
about_text = (
   "Little Mary Phillips fell off her bike while attempting to avoid a trailof ants crossing the bike path. "
   "Once her tears had subsided and the cut on her knee ceased bleeding, she bravely got back on her bike."
)
##1-------Tokenization---------##

about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)


##2-------Stop Words-----------###

about_doc = nlp(about_text)
print([token for token in about_doc if not token.is_stop])


##3-------Lemmatization-----------##

about_doc=nlp(about_text)
for token in about_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")
        

 ##4-------Part of Speech----------##   
               
about_doc = nlp(about_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    ) 
 
 
'''Little 0
Mary 7
Phillips 12
fell 21
off 26
her 30
bike 34
while 39
attempting 45
to 56
avoid 59
a 65
trailof 67
ants 75
crossing 80
the 89
bike 93
path 98
. 102
Once 104
her 109
tears 113
had 119
subsided 123
and 132
the 136
cut 140
on 144
her 147
knee 151
ceased 156
bleeding 163
, 171
she 173
bravely 177
got 185
back 189
on 194
her 197
bike 201
. 205
[Little, Mary, Phillips, fell, bike, attempting, avoid, trailof, ants, crossing, bike, path, ., tears, subsided, cut, knee, ceased, bleeding, ,, bravely, got, bike, .]
              Little : little
                fell : fall
          attempting : attempt
                ants : ant
            crossing : cross
                Once : once
               tears : tear
                 had : have
            subsided : subside
              ceased : cease
                 got : get

TOKEN: Little
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: Mary
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: Phillips
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: fell
=====
TAG: VBD        POS: VERB
EXPLANATION: verb, past tense

TOKEN: off
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: her
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: bike
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: while
=====
TAG: IN         POS: SCONJ
EXPLANATION: conjunction, subordinating or preposition

TOKEN: attempting
=====
TAG: VBG        POS: VERB
EXPLANATION: verb, gerund or present participle

TOKEN: to
=====
TAG: TO         POS: PART
EXPLANATION: infinitival "to"

TOKEN: avoid
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: a
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: trailof
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: ants
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: crossing
=====
TAG: VBG        POS: VERB
EXPLANATION: verb, gerund or present participle

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: bike
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: path
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: Once
=====
TAG: IN         POS: SCONJ
EXPLANATION: conjunction, subordinating or preposition

TOKEN: her
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: tears
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: had
=====
TAG: VBD        POS: AUX
EXPLANATION: verb, past tense

TOKEN: subsided
=====
TAG: VBN        POS: VERB
EXPLANATION: verb, past participle

TOKEN: and
=====
TAG: CC         POS: CCONJ
EXPLANATION: conjunction, coordinating

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: cut
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: on
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: her
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: knee
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: ceased
=====
TAG: VBD        POS: VERB
EXPLANATION: verb, past tense

TOKEN: bleeding
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: ,
=====
TAG: ,          POS: PUNCT
EXPLANATION: punctuation mark, comma

TOKEN: she
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: bravely
=====
TAG: RB         POS: ADV
EXPLANATION: adverb

TOKEN: got
=====
TAG: VBD        POS: VERB
EXPLANATION: verb, past tense

TOKEN: back
=====
TAG: RB         POS: ADV
EXPLANATION: adverb

TOKEN: on
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: her
=====
TAG: PRP$       POS: PRON
EXPLANATION: pronoun, possessive

TOKEN: bike
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer'''
 