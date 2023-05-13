import pymediainfo
import ffmpeg


VIDEO_TRACK_TYPE = "Video"
AUDIO_TRACK_TYPE = "Audio"
SUBTITLE_TRACK_TYPE = "Text"
BIT_RATE_CONSTANT = 1000
FPS_CONSTANT = " fps"


class VideoMetadata:

    def __init__(self, filename):
        self.filename = filename
        self.media_info = None
        self.video_metadata = None
        self.audio_metadata = None
        self.subtitle_metadata = None

    def get_metadata(self):
        self.media_info = pymediainfo.MediaInfo.parse(self.filename)
        self.video_metadata = self._get_video_track_metadata()
        self.audio_metadata = self._get_audio_track_metadata()
        self.subtitle_metadata = self._get_subtitle_track_metadata()
        return {
            "video": self.video_metadata,
            "audio": self.audio_metadata,
            "subtitle": self.subtitle_metadata
        }

    def _get_video_track_metadata(self):
        video_track = next((
            track for track in self.media_info.tracks if track.track_type == VIDEO_TRACK_TYPE
        ), None)
        if not video_track:
            return {}
        data = {
            "codec": video_track.codec,
            "resolution": f"{video_track.width}x{video_track.height}",
            "frame_rate": f"{video_track.frame_rate}{FPS_CONSTANT}",
            "bit_rate": f"{video_track.bit_rate / BIT_RATE_CONSTANT:.0f} kbps",
        }
        return data

    def _get_audio_track_metadata(self):
        audio_track = next((
            track for track in self.media_info.tracks if track.track_type == AUDIO_TRACK_TYPE
        ), None)
        if not audio_track:
            return {}
        data = {
            "channels": audio_track.channel_s,
            "bit_rate": f"{audio_track.bit_rate / BIT_RATE_CONSTANT:.0f} kbps",
        }
        return data

    def _get_subtitle_track_metadata(self):
        subtitle_track = next((
            track for track in self.media_info.tracks if track.track_type == SUBTITLE_TRACK_TYPE
        ), None)
        if not subtitle_track:
            return {}
        data = {"codec": subtitle_track.codec}
        return data


class VideoMetadataRemover:

    def __init__(self, filename):
        self.filename = filename

    def remove_metadata(self):
        input_file = ffmpeg.input(self.filename)
        output_file = input_file.output(self.filename.replace(".", "_new."), map_metadata=-1)
        output_file.run()
        status = f"Metadata has been removed. A new file has been created: {self.filename.replace('.','_new.')}"
        return status
