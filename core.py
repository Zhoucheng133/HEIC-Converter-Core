import os
from pillow_heif import register_heif_opener
from PIL import Image

register_heif_opener()

def convert(input_file, output_dir, quality, use_exif) -> bool:
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
        
        return True
    except Exception as _:
        return False
    

if __name__=="__main__":
    convert("test/test.HEIC", "test", 80, True)