# This is a sample Python script.
import sys
from youtube_data import process_data

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    channels = input('Enter the name(s) or link(s) of the youtube channel (Comma-separated): ')
    channels = channels.split(",")
    channels = [x.strip() for x in channels]
    for i in channels:
        process_data(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
