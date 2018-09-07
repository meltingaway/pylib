import argparse
import datetime
import pytz
import time

from dateutil import parser

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-s",
  help="The date time string. e.g. \"01/12/2011\"")
arg_parser.add_argument("-ts", type=int,
  help="The timestamp since epoch. e.g. 1515571200 ")


def main():
  args = arg_parser.parse_args()

  if args.s:
    print parser.parse(args.s).strftime("Seconds: %s, Microseconds: %f ")
  elif args.ts:  
    print "Local time: " + datetime.datetime.fromtimestamp(args.ts).strftime("%c %z")
  else:
    arg_parser.print_help()

# Reference:
# http://pytz.sourceforge.net/#localized-times-and-date-arithmetic
# https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior


if __name__ == "__main__":
    main()
