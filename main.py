import luigi
from pipeline.quiz_gen import QuizUser

def main():
    batch=1
    while True:
        luigi.build([QuizUser(batch_id=batch)])

        again = input("\n🎮 Play again with new words? (y/n): ").strip().lower()
        if again != 'y':
            break
        batch += 1

if __name__ == '__main__':
    main()