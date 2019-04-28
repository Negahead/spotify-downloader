import os
import appdirs
import sys

from spotdl.handle import get_arguments
from spotdl.spotdl import match_args
from spotdl import internals
from spotdl import const


def test_appdirs():
    print(os.path.join(appdirs.user_config_dir(), "spotdl"))


def arg(song_url=None):
    options = get_arguments(raw_args=song_url)
    return options


def download():
    arguments = arg(song_url=['--song', 'https://open.spotify.com/track/2DGa7iaidT5s0qnINlwMjJ'])
    const.args = arguments

    internals.filter_path(const.args.folder)

    try:
        match_args()
        sys.exit(0)

    except KeyboardInterrupt as e:
        sys.exit(3)


if __name__ == '__main__':
    download()
