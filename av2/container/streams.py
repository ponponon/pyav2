from typing import Tuple, List
from av2.video.stream import VideoStream


class StreamContainer(object):

    """

    A tuple-like container of :class:`Stream`.

    ::

        # There are a few ways to pulling out streams.
        first = container.streams[0]
        video = container.streams.video[0]
        audio = container.streams.get(audio=(0, 1))


    """
    _streams: List
    video: Tuple[VideoStream]
    audio: Tuple
    subtitles: Tuple
    data: Tuple
    other: Tuple
