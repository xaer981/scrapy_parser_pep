from .constants import RESULTS_DIR_NAME

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'


ROBOTSTXT_OBEY = True


FEEDS = {
    f'{RESULTS_DIR_NAME}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    },
}


ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}