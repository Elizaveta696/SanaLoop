import luigi
from pipeline.translate_data import GetTranslation

if __name__ == '__main__':
    luigi.build([GetTranslation()], local_scheduler = True)