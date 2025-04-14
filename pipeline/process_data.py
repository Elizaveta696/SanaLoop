import luigi
import os

class ProcessData(luigi.Task):
    def requires(self):
        from pipeline.get_data import GetData
        return GetData()

    def output(self):
        return luigi.LocalTarget('data/processed_words.txt')

    def run(self):
        os.makedirs('data', exist_ok=True)

        with self.input().open('r') as infile:
            raw_words = infile.readlines()

        cleaned = set()
        for word in raw_words:
            word = word.strip().lower()
            if word.isalpha() and 2 <= len(word) <= 20:
                cleaned.add(word)

        with self.output().open('w') as outfile:
            for word in cleaned:
                outfile.write(word + '\n')
