import luigi
import requests
import os

class GetData(luigi.Task):
    def output(self):
        return luigi.LocalTarget('data/raw_words.txt')

    def run(self):
        url = "https://raw.githubusercontent.com/hugovk/everyfinnishword/refs/heads/master/kaikkisanat.txt"
        response = requests.get(url)
        print(response)

        os.makedirs(os.path.dirname(self.output().path), exist_ok=True)

        with open(self.output().path, 'w', encoding='utf-8') as f:
            f.write(response.text)