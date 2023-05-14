import argparse
import os

from exceptions import FileIsNotValid, InvalidFileTypeError, InvalidOptionError
from modules.document import DocumentMetadata
from modules.image import ImageMetadata
from modules.media import VideoMetadata, VideoMetadataRemover


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Get metadata for a file")
    parser.add_argument("-r", "--read", help="Option to read metadata")
    parser.add_argument("-d", "--delete", help="Option to remove metadata")
    parser.add_argument("-t", "--type", choices=['media', 'document', 'image'], help="Option to specify file type")
    args = parser.parse_args()

    if not args.read and not args.delete:
        raise InvalidOptionError("Specify an option to run. Write -h or --help for help")

    if not args.type:
        raise InvalidFileTypeError("Specify a file type")

    return args


def main():
    try:
        args = parse_args()
        if args.read and not os.path.isfile(args.read):
            raise FileIsNotValid(args.read, f"{args.read} is not a valid file")
        if args.read:
            if args.type == "media":
                metadata = VideoMetadata(args.read).get_metadata()
                print(metadata)
            elif args.type == "image":
                metadata = ImageMetadata(args.read).get_metadata()
                print(metadata)
            elif args.type == "document":
                metadata = DocumentMetadata(args.read).get_metadata()
                print(metadata)

        if args.delete and not os.path.isfile(args.delete):
            raise FileIsNotValid(args.delete, f"{args.delete} is not a valid file")
        if args.delete:
            if args.type == "media":
                VideoMetadataRemover(args.delete).remove_metadata()
                print(f"Metadata has been successfully removed from {args.delete}")
            elif args.type == "image":
                ImageMetadata(args.delete).remove_metadata()
                print(f"Metadata has been successfully removed from {args.delete}")
            elif args.type == "document":
                DocumentMetadata(args.delete).remove_metadata()
                print(f"Metadata has been successfully removed from {args.delete}")

    except InvalidOptionError as e:
        print(e)
    except InvalidFileTypeError as e:
        print(e)
    except FileIsNotValid as e:
        print(e)


if __name__ == '__main__':
    main()
