import os
import argparse
from pillow_heif import register_heif_opener
from PIL import Image

register_heif_opener()

def convert(input_file, output_dir, quality=80, use_exif=True) -> bool:
    heic_path = os.path.join(input_file)
    jpeg_path = os.path.join(
        output_dir, os.path.splitext(os.path.basename(input_file))[0] + ".jpg"
    )

    try:
        img = Image.open(heic_path)
        exif_bytes = img.info.get("exif")

        if exif_bytes and use_exif:
            img.save(jpeg_path, "JPEG", quality=quality, exif=exif_bytes)
        else:
            img.save(jpeg_path, "JPEG", quality=quality)
        
        print(f"Converted: {heic_path} -> {jpeg_path}")
        return True
    except Exception as e:
        print(f"Failed to convert {heic_path}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Convert HEIC images to JPEG")
    parser.add_argument("input_file", help="Path to the input HEIC file")
    parser.add_argument("output_dir", help="Directory to save JPEG file")
    parser.add_argument("--quality", type=int, default=80, help="JPEG quality (default: 80)")
    parser.add_argument("--no-exif", action="store_true", help="Do not preserve EXIF data")

    args = parser.parse_args()
    convert(args.input_file, args.output_dir, quality=args.quality, use_exif=not args.no_exif)

if __name__ == "__main__":
    main()
