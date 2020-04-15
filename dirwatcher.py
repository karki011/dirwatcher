#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import argparse
import logging
import datetime
import time
import signal

from pyfiglet import Figlet

# __rearch_site__ = [{
#     1: "https://docs.python.org/3.1/library/logging.html",
#     2: "www.devdungeon.com/content/create-ascii-art-text-banners-python"
# }]

f = Figlet(font='slant')
logger = logging.getLogger(__file__)
exit_flag = False
existed_files = []
magic_spell_position = {}
ascii_banner_start = f.renderText('Start!!')
ascii_banner_watching = f.renderText('Watching!!')
ascii_banner_stopped = f.renderText('Stopped!!')

__author__ = "Subash Karki, mob_coding with stew, Piero(Instructor)"


def watching_directory(args):
    """look at the dir and put in dict if its not already there
        log the message if added new
    """
    logger.info(
        'Watching directory: {}, Ext: {}, Interval: {}, Magic_word:{}'
        .format(
            args.path, args.ext, args.interval, args.magic
        ))
    directory = os.path.abspath(args.path)
    files_in_directory = os.listdir(directory)
    for file in files_in_directory:
        if file.endswith(args.ext) and file not in existed_files:
            logger.info('Another file: {} found in {}'.format(file, args.path))
            existed_files.append(file)
            magic_spell_position[file] = 0
    for file in existed_files:
        if file not in files_in_directory:
            logger.info(' {} removed from {}'.format(file, args.path))
            existed_files.remove(file)
            del magic_spell_position[file]
    for file in existed_files:
        find_magic(file, directory, args.magic)


def signal_handler(sig_num, frame):
    """
      This is a handler for SIGTERM and SIGINT. Other
        signals can be mapped here as well (SIGHUP?)
      Basically it just sets a global flag, and main()
      will exit it's loop if the signal is trapped.
      :param sig_num: The integer signal number
      that was trapped from the OS.
      :param frame: Not used
      :return None
      """
    global exit_flag
    # log the associated signal name (the python3 way)
    signames = dict((k, v) for v, k in reversed(sorted(
        signal.__dict__.items()))
        if v.startswith('SIG') and not v.startswith('SIG_'))
    logger.warning('Received signal: ' + signames[sig_num])
    if sig_num == signal.SIGINT or signal.SIGTERM:
        exit_flag = True


def find_magic(filename, directory, magic_word):
    """ Search thru the file and look for magic number"""
    watchfile = os.path.join(directory, filename)
    with open(watchfile) as f:
        for i, line in enumerate(f.readlines(), 1):
            if magic_word in line and i > magic_spell_position[filename]:
                logger.info('Magic word found: {} on line: {}'
                            ' in file: {}'.format(magic_word, i, filename))
            if i > magic_spell_position[filename]:
                magic_spell_position[filename] += 1


def create_praser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--ext', type=str, default='.txt',
                        help="File its watching for")
    parser.add_argument('-i', '--interval', type=float,
                        default=2, help="Number od second to watch the file")
    parser.add_argument('path', help="Dir to path to watch for")
    parser.add_argument('magic', help="String to find in the watch file")
    return parser


def main():
    """Start long runing program to watch directory's file changes"""
    logging.basicConfig(
        format='%(asctime)s.%(msecs)03d %(name)-12s %(levelname)-8s'
        '[%(threadName)-12s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    logger.setLevel(logging.DEBUG)
    print(ascii_banner_start)
    app_start_time = datetime.datetime.now()
    logger.info(
        '\n'
        '-------------------------------------------------------------------\n'
        '    Running {0}\n'
        '    Started on {1}\n'
        '-------------------------------------------------------------------\n'
        .format(__file__, app_start_time.isoformat())
    )
    print(ascii_banner_watching)

    parser = create_praser()
    args = parser.parse_args()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    while not exit_flag:
        try:
            watching_directory(args)
        except OSError as e:
            logger.error(str(e))
            # logger.error('{} directory does not exist'.format(args.path))
            time.sleep(args.interval)
        except Exception as e:
            logger.error('Unhandled exception: {}'.format(e))
        time.sleep(args.interval)

    uptime = datetime.datetime.now() - app_start_time
    logger.info(
        '\n'
        '-------------------------------------------------------------------\n'
        '    Stopped {0}\n'
        '    Uptime was on {1}\n'
        '-------------------------------------------------------------------\n'
        .format(__file__, str(uptime))
    )
    print(ascii_banner_stopped)


if __name__ == "__main__":
    main()
