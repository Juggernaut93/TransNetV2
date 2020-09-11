import ffmpeg
import numpy as np


def get_frames(fn, width=48, height=27, nodup=True):
    # passthrough tells ffmpeg not to duplicate any frame (it does that to obtain constant frame rate)
    # using nodup is useful for example if you want the output to have the same frames as OpenCV, which seems to use passthrough vsync
    vsync_method = "passthrough" if nodup else "auto"
    video_stream, err = (
        ffmpeg
        .input(fn)
        .output('pipe:', format='rawvideo', pix_fmt='rgb24', s='{}x{}'.format(width, height), vsync=vsync_method)
        .run(capture_stdout=True, capture_stderr=True)
    )
    video = np.frombuffer(video_stream, np.uint8).reshape([-1, height, width, 3])
    return video
