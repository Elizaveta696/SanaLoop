import luigi
import requests
import csv
import time
import os
from pipeline.store_data import init_db, save_translation, is_translated, get_all_translations

class GetTranslation(luigi.Task):
    def requires(self):
        init_db()
        from pipeline.process_data import ProcessData
        return ProcessData()

    def output(self):
        return luigi.LocalTarget('data/translated_words.csv')

    def run(self):
        os.makedirs('data', exist_ok=True)

        with open(self.input().path, 'r', encoding='utf-8', errors='replace') as infile:
            all_words = [line.strip() for line in infile if line.strip()]

        words = [word for word in all_words if not is_translated(word)]

        translations = []
        for word in words[:10]:
            try:
                params={
                    "client": "dict-chrome-ex",
                    "sl": "fi",
                    "tl": "en",
                    "q": word
                }
                response = requests.post("https://clients5.google.com/translate_a/t", params=params)

                response.raise_for_status()
                translated = response.json()[0]
                translations.append((word, translated))
                save_translation(word, translated)
                time.sleep(2)
            except Exception as e:
                print(e)
                translations.append((word, "ERROR"))


        valid_translations = [t for t in translations if t[1] != "ERROR"]

        with open(self.output().path, 'w', newline ='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(['Finnish', 'English'])
            writer.writerows(valid_translations)