import csv
import datetime as dt
from collections import defaultdict

from pep_parse.constants import (BASE_DIR, DATETIME_FORMAT,
                                 PEP_SUMMARY_FILENAME, RESULTS_DIR_NAME)


class PepParsePipeline:
    def __init__(self) -> None:
        self.results_dir = BASE_DIR / RESULTS_DIR_NAME
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.results[item['status']] += 1

        return item

    def close_spider(self, spider):
        now = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = PEP_SUMMARY_FILENAME.format(datetime=now)
        file_path = self.results_dir / file_name

        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(
                (('Статус', 'Количество'),
                 *self.results.items(),
                 ('Total', sum(self.results.values()))
                 )
            )
