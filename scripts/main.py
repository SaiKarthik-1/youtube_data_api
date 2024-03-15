from process_youtube_data import process_input_data

def main():
    """
    Youtube Data Aggregator process
    :return: Channel and video data
    """

    channels = input('Enter the name(s) or link(s) of the youtube channel or video (Comma-separated): ')
    if channels == '':
        exit('No input has been provided')

    channels = channels.split(",")
    channels = [x.strip() for x in channels]
    for i in channels:
        process_input_data(i)
        print('\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
