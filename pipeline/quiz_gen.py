import luigi
from pipeline.store_data import get_all_translations
import random
from pipeline.translate_data import GetTranslation

class QuizUser(luigi.Task):
    batch_id = luigi.IntParameter()

    def requires(self):
        return GetTranslation(batch_id=self.batch_id)

    def output(self):
        return luigi.LocalTarget(f'data/quiz_results_{self.batch_id}')

    def run(self):
        all_pairs = get_all_translations()
        if len(all_pairs) < 10:
            print("Not enough translations in DB for Quiz. Srry!")
            return

        quiz_pairs = random.sample(all_pairs, 10)
        finnish_words = [pair[0] for pair in quiz_pairs]
        english_words = [pair[1] for pair in quiz_pairs]
        shuffled_en_words = english_words[:]
        random.shuffle(shuffled_en_words)

        print("\n Welcome to the SanaLoop Quiz!\n")

        matches = {}

        for i in range(1, 11):

            print(f"{'Finnish':<25}{'Elglish'}")
            print('-' * 50)
            for id, word in enumerate(finnish_words, 1):
                print(f"{id}. {word:<22}    {id}. {shuffled_en_words[id-1]}")

            print("Make a match! Write the answer like 1-4 (which stands for Finnish 1 - English 4)\n")

            while True:
                try:
                    pair = input(f"\nWrite your {i} match here:").strip()
                    fin, eng = map(int, pair.split("-"))
                    if fin in matches:
                        print("You already matched this Finnish word.")
                        continue
                    if fin < 1 or fin > 10:
                        print('Finnish index out of range.')
                        continue
                    if eng < 1 or eng > 10:
                        print('English index out of range.')
                        continue
                    matches[fin] = eng
                    break

                except:
                    print("Invalid format. try again like 2-7")

        score = 0
        for fin_index, eng_index in matches.items():
            correct_eng = english_words[fin_index - 1]
            user_eng = shuffled_en_words[eng_index -1]
            if correct_eng == user_eng:
                score += 1

        print(f"\nScore: {score}/10")
        if score == 10:
            print("Perfect match!")
        if score >= 7:
            print("Well done!")
        else:
            print("Keep Going!")

        with self.output().open('w') as outfile:
            outfile.write(f"Result: {score}/10\n")


    def complete(self):
        return False


