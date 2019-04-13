"""The classic MapReduce job: count the frequency of words.
"""
from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")
ALPHABET_RE = re.compile(r"[a-zA-Z]")

class MRCC1TOP10(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   combiner=self.combiner_count_words,
                   reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_find_max_word)
        ]
    
    def mapper_get_words(self, _, line):
        the_line = WORD_RE.findall(line)
        for key, value in enumerate(the_line):
            if (value == "my" and (key + 1 < len(the_line))):
                yield (value + "," + the_line[key+1].lower(), 1)

    def combiner_count_words(self, value, counts):
        yield (value, sum(counts))

    def reducer_count_words(self, value, counts):
        #yield (value, sum(counts))
        yield None, (sum(counts), value)
    
    def reducer_find_max_word(self, _, word_count_pairs):
        # each item of word_count_pairs is (count, word),
        # so yielding one results in key=counts, value=word
        list_descending = sorted(word_count_pairs, reverse = True)
        yield ("top 10", list_descending[0:9])

if __name__ == '__main__':
    MRCC1TOP10.run()
