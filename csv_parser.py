import argparse


def csv_parser():

    """Получение названия csv-файла с предметами из командной строки"""

    parser = argparse.ArgumentParser(description='File name with subjects')
    parser.add_argument('file',
                        type=str,
                        nargs=1,
                        metavar='file name with subjects',
                        help='enter file name with subjects')
    args = parser.parse_args()
    return args.file[0]
