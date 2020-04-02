import logging
from pyfiglet import Figlet
import datetime


__author__ = "Subash Karki"
# __rearch_site__ = [{
#     1: "https://docs.python.org/3.1/library/logging.html",
#     2: "www.devdungeon.com/content/create-ascii-art-text-banners-python"
# }]

logger = logging.getLogger(__file__)


def main():
    logging.basicConfig(format='%(asctime)s  %(levelname)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logger.setLevel(logging.DEBUG)
    custom_fig = Figlet(font='graffiti')
    running_text = (custom_fig.renderText('Running...'))
    print(running_text)
    app_start_time = datetime.datetime.now()
    logger.info(
        '\n'
        '-------------------------------------------------------------------\n'
        '    Running {0}\n'
        '    Started on {1}\n'
        '-------------------------------------------------------------------\n'
        .format(__file__, app_start_time.isoformat())
    )
    watching_text = (custom_fig.renderText('Watching...'))
    print(watching_text)
    uptime = datetime.datetime.now() - app_start_time
    logger.info(
        '\n'
        '-------------------------------------------------------------------\n'
        '    Stopped {0}\n'
        '    Uptime was on {1}\n'
        '-------------------------------------------------------------------\n'
        .format(__file__, str(uptime))
    )
    stop_text = (custom_fig.renderText('Stopped...'))
    print(stop_text)


if __name__ == "__main__":
    main()
