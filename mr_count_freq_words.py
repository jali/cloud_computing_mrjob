"""The classic MapReduce job: count the frequency of words.
"""
from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")


class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        the_line = WORD_RE.findall(line)
        for key, value in enumerate(the_line):
            if (value == "my" and (key + 1 < len(the_line))):
                yield (value + "," + the_line[key+1].lower(), 1)

    def combiner(self, value, counts):
        yield (value, sum(counts))

    def reducer(self, value, counts):
        yield (value, sum(counts))


if __name__ == '__main__':
     MRWordFreqCount.run()
