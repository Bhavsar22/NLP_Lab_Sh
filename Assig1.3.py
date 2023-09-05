import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
   "The man who does not read books has no advantage over the one who cannot read them."
    "Teachers can open the door,but you must enter it yourself."
    "The breautiful thing about learning is that no one can take it away from you."
    "Education is the most powerful weapon you can use to change the world."

)
about_doc = nlp(about_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )
 #--------output---------# 
"""TOKEN: The
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: man
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: who
=====
TAG: WP         POS: PRON
EXPLANATION: wh-pronoun, personal

TOKEN: does
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: not
=====
TAG: RB         POS: PART
EXPLANATION: adverb

TOKEN: read
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: books
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: has
=====
TAG: VBZ        POS: VERB
EXPLANATION: verb, 3rd person singular present

TOKEN: no
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: advantage
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: over
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: one
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: who
=====
TAG: WP         POS: PRON
EXPLANATION: wh-pronoun, personal

TOKEN: can
=====
TAG: MD         POS: AUX
EXPLANATION: verb, modal auxiliary

TOKEN: not
=====
TAG: RB         POS: PART
EXPLANATION: adverb

TOKEN: read
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: them
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: Teachers
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: can
=====
TAG: MD         POS: AUX
EXPLANATION: verb, modal auxiliary

TOKEN: open
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: door
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: ,
=====
TAG: ,          POS: PUNCT
EXPLANATION: punctuation mark, comma

TOKEN: but
=====
TAG: CC         POS: CCONJ
EXPLANATION: conjunction, coordinating

TOKEN: you
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: must
=====
TAG: MD         POS: AUX
EXPLANATION: verb, modal auxiliary

TOKEN: enter
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: it
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: yourself
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: The
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: breautiful
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: thing
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: about
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: learning
=====
TAG: VBG        POS: VERB
EXPLANATION: verb, gerund or present participle

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: that
=====
TAG: IN         POS: SCONJ
EXPLANATION: conjunction, subordinating or preposition

TOKEN: no
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: one
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: can
=====
TAG: MD         POS: AUX
EXPLANATION: verb, modal auxiliary

TOKEN: take
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: it
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: away
=====
TAG: RB         POS: ADV
EXPLANATION: adverb

TOKEN: from
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: you
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: Education
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: most
=====
TAG: RBS        POS: ADV
EXPLANATION: adverb, superlative

TOKEN: powerful
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: weapon
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: you
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: can
=====
TAG: MD         POS: AUX
EXPLANATION: verb, modal auxiliary

TOKEN: use
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: to
=====
TAG: TO         POS: PART
EXPLANATION: infinitival "to"

TOKEN: change
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: world
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: The
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: man
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: who
=====
TAG: WP         POS: PRON
EXPLANATION: wh-pronoun, personal

TOKEN: does
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: not
=====
TAG: RB         POS: PART
EXPLANATION: adverb

TOKEN: read
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: books
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: has
=====
TAG: VBZ        POS: VERB
EXPLANATION: verb, 3rd person singular present

TOKEN: no
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: advantage
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: over
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: one
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: who
=====
TAG: WP         POS: PRON
EXPLANATION: wh-pronoun, personal

TOKEN: can
=====
TAG: MD         POS: AUX
EXPLANATION: verb, modal auxiliary

TOKEN: not
=====
TAG: RB         POS: PART
EXPLANATION: adverb

TOKEN: read
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: them
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: Teachers
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: can
=====
TAG: MD         POS: AUX
EXPLANATION: verb, modal auxiliary

TOKEN: open
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: door
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: ,
=====
TAG: ,          POS: PUNCT
EXPLANATION: punctuation mark, comma

TOKEN: but
=====
TAG: CC         POS: CCONJ
EXPLANATION: conjunction, coordinating

TOKEN: you
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: must
=====
TAG: MD         POS: AUX
EXPLANATION: verb, modal auxiliary

TOKEN: enter
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: it
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: yourself
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: The
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: breautiful
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: thing
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: about
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: learning
=====
TAG: VBG        POS: VERB
EXPLANATION: verb, gerund or present participle

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: that
=====
TAG: IN         POS: SCONJ
EXPLANATION: conjunction, subordinating or preposition

TOKEN: no
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: one
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: can
=====
TAG: MD         POS: AUX
EXPLANATION: verb, modal auxiliary

TOKEN: take
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: it
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: away
=====
TAG: RB         POS: ADV
EXPLANATION: adverb

TOKEN: from
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: you
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: .
=====
TAG: .          POS: PUNCT
EXPLANATION: punctuation mark, sentence closer

TOKEN: Education
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: most
=====
TAG: RBS        POS: ADV
EXPLANATION: adverb, superlative

TOKEN: powerful
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: weapon
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: you
=====
TAG: PRP        POS: PRON
EXPLANATION: pronoun, personal

TOKEN: can
=====
TAG: MD         POS: AUX
EXPLANATION: verb, modal auxiliary

TOKEN: use
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: to
=====
TAG: TO         POS: PART
EXPLANATION: infinitival "to"

TOKEN: change
=====
TAG: VB         POS: VERB
EXPLANATION: verb, base form

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: world
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass"""
