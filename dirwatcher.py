import logging
import datetime
import time
import argparse
# from pyfiglet import Figlet

__author__ = "Subash Karki, mob_coding"
# __rearch_site__ = [{
#     1: "https://docs.python.org/3.1/library/logging.html",
#     2: "www.devdungeon.com/content/create-ascii-art-text-banners-python"
# }]

logger = logging.getLogger(__file__)


def watch_dir(args):
    watching_file = {}
    """look at the dir and put in dict if its not already there
        log the message if added new
    """
    logger.info(
        'Watching dir: {}, File extension: {}, Interval: {}, magic text:{}'
        .format(
            args.path, args.ext, args.interval, args.magic
        ))
    while True:
        try:
            logger.info("Inside watch loop")
            time.sleep(args.interval)
        except KeyboardInterrupt:
            break


def find_magic(file_name, starting_line, magic_word):
    pass


def create_praser():
    parser = argparse.ArgumentParser(description='File Extension serach.')
    parser.add_argument('-e', '--ext', type=str, default='.txt',
                        help="File its watching for")
    parser.add_argument('-i', '--interval', type=float,
                        default=1.0, help="Number od second to watch the file")
    parser.add_argument('path', help="Dir to path to watch for")
    parser.add_argument('magic', help="Sting to find in the watch file")
    return parser


def main():
    logging.basicConfig(format='%(asctime)s  %(levelname)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logger.setLevel(logging.DEBUG)
    # custom_fig = Figlet(font='graffiti')
    # running_text = (custom_fig.renderText('Running...'))
    # print(running_text)
    app_start_time = datetime.datetime.now()
    logger.info(
        '\n'
        '-------------------------------------------------------------------\n'
        '    Running {0}\n'
        '    Started on {1}\n'
        '-------------------------------------------------------------------\n'
        .format(__file__, app_start_time.isoformat())
    )
    # watching_text = (custom_fig.renderText('Watching...'))
    # print(watching_text)

    parser = create_praser()
    args = parser.parse_args()
    watch_dir(args)

    uptime = datetime.datetime.now() - app_start_time
    logger.info(
        '\n'
        '-------------------------------------------------------------------\n'
        '    Stopped {0}\n'
        '    Uptime was on {1}\n'
        '-------------------------------------------------------------------\n'
        .format(__file__, str(uptime))
    )
    # stop_text = (custom_fig.renderText('Stopped...'))
    # print(stop_text)


if __name__ == "__main__":
    main()
