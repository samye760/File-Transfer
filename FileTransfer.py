"""This module is to copy a file of tables into another directory."""

import logging
import shutil
import sys
import os

logging.basicConfig(encoding='utf-8', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


def main():
    """Entrypoint of program run as module."""

    logging.info("Usage: First argument(optional) location of files to copy. \
                 Second argument names of files to copy.")

    if len(sys.argv) > 3:

        directory = sys.argv[1]
        file_names = sys.argv[2]
        output = sys.argv[3]

        logging.info("Directory copying files from: %s. Files to be copied: %s. Copying to %s",
                     directory, file_names, output)

    else:

        directory = '/opt/ebde/edo/Informatica/ArgFiles/'

        try:
            file_names = sys.argv[1]
            output = sys.argv[2]

            logging.info("Directory copying files from: %s. Files to be copied: %s. Copying to %s",
                         directory, file_names, output)
        except IndexError:
            logging.critical(
                "Please provide the name of your table files as the first argument.")
            exit()

    if not os.path.isdir(output):
        logging.info(
            "%s directory does not exist. Creating directory now.", output)
        os.mkdir(output)

    with open(file_names, 'r') as tables:
        start_count = len(tables.readlines())
        logging.info("%s has %s tables.", file_names, start_count)
        tables.seek(0)

        for count, table in enumerate(tables.readlines()):
            if table[-3:] == '.sh':
                table = directory + table
            else:
                table = directory + table.strip() + '.sh'

            if os.path.isfile(table):
                shutil.copy(table, output)
                logging.info("%s copied to %s. %s files copied so far.",
                             table, output, count + 1)
            else:
                logging.error("%s is not a file.", table)

    _, _, files = next(os.walk(output))
    logging.info("%s tables copied.", len(files))


if __name__ == "__main__":
    main()
