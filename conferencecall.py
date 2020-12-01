import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer


summarizer=LexRankSummarizer()
summary=summarizer(parser.document,1)
for sentence in summary:
    print(sentence)


luhn_summarizer= LuhnSummarizer()
summary=luhn_summarizer(parser.document,3)
for sentence in summary:
    print(sentence)


