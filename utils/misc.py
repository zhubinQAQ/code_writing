import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def log_info(s):
    logger.info(s)


def log_data(task, num, test_data, results):
    """

    :param test_datas: list[]
    :param results: list[]
    :return:
    """
    logger.info(' [{} solution {}]'.format(task.split('.')[-1], num))
    logger.info('   |- test data -> '+ str(test_data))
    logger.info('   |-  result   -> '+str(results))
