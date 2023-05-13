import exiftool


class DocumentMetadata:

    __slots__ = ["filepath"]

    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_metadata(self) -> dict:
        with exiftool.ExifTool() as et:
            metadata = et.get_metadata(self.filepath)
        return metadata

    def remove_metadata(self) -> bool:
        with exiftool.ExifTool() as et:
            et.delete_all_metadata(self.filepath)
        return True
