import logging

# create logger object
logger_mcloggyface = logging.getLogger()
logger_mcloggyface.setLevel(logging.DEBUG)

# create file handler
fh = logging.FileHandler("debug/warnings.log", mode='w+')
fh.setLevel(logging.WARNING)

# create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# format
fh_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
ch_formatter = logging.Formatter('[%(levelname)s] %(message)s')
fh.setFormatter(fh_formatter)
ch.setFormatter(ch_formatter)

# add/register them with the logger obj
logger_mcloggyface.addHandler(fh)
logger_mcloggyface.addHandler(ch)

logger_mcloggyface.info('I\'m back baby!')
