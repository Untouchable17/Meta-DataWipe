import os
import exifread
import exiftool
from PIL.ExifTags import TAGS
from PIL import Image
from typing import Dict, Any, Optional, Tuple, Union


class ImageMetadata:

    __slots__ = ["filename", "metadata"]

    def __init__(self, filename: str) -> None:
        self.filename: str = filename
        self.metadata: dict = {}

    def _get_exif_tags(self) -> Dict[str, exifread.classes.IfdTag]:
        with open(self.filename, 'rb') as f:
            return exifread.process_file(f)

    @staticmethod
    def _get_gps_info(exif_data: dict) -> Optional[Tuple[float, float]]:
        gps_info = {}
        for key in exif_data.keys():
            if 'GPS' in key:
                gps_info[key] = exif_data[key]

        lat = gps_info.get('GPSLatitude', None)
        lat_ref = gps_info.get('GPSLatitudeRef', None)
        lon = gps_info.get('GPSLongitude', None)
        lon_ref = gps_info.get('GPSLongitudeRef', None)

        if lat and lat_ref and lon and lon_ref:
            lat_value = lat.values[0].num / float(lat.values[0].den)
            lon_value = lon.values[0].num / float(lon.values[0].den)
            if lat_ref.values[0] == 'S':
                lat_value = -lat_value
            if lon_ref.values[0] == 'W':
                lon_value = -lon_value
            return (lat_value, lon_value)
        else:
            return None

    def _get_basic_metadata(self, image: Image) -> dict:
        metadata = {
            'filename': os.path.basename(self.filename),
            'format': image.format,
            'size': image.size,
            'mode': image.mode,
            'animated': hasattr(image, 'is_animated') and image.is_animated
        }
        return metadata

    def _get_exif_metadata(self, image: Any) -> dict:
        metadata = {}
        exif_data = image.getexif()
        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                if isinstance(value, bytes):
                    value = value.decode('utf-8', errors='replace')
                metadata[tag] = value

            gps_info = self._get_gps_info(self._get_exif_tags())
            if gps_info:
                metadata['GPSLatitude'] = gps_info[0]
                metadata['GPSLongitude'] = gps_info[1]
        return metadata

    def _get_iptc_metadata(self) -> dict:
        metadata = {}
        try:
            with exiftool.ExifTool() as et:
                metadata.update(et.get_metadata(self.filename))
        except:
            pass
        return metadata

    def get_metadata(self) -> dict:

        with Image.open(self.filename) as image:
            metadata = self._get_basic_metadata(image)
            metadata.update(self._get_exif_metadata(image))
            metadata.update(self._get_iptc_metadata())
            return metadata

    def remove_metadata(self) -> Union[str, bool]:
        try:
            with exiftool.ExifTool() as et:
                et.delete_all_tags(self.filename)
            image = Image.open(self.filename)
            data = list(image.getdata())
            image_without_metadata = Image.new(image.mode, image.size)
            image_without_metadata.putdata(data)
            image_without_metadata.save(self.filename)
            return f"File metadata {self.filename} deleted successfully"
        except Exception as e:
            print(f"Error removing metadata: {str(e)}")
            return False
