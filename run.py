import os, datetime
from PIL import Image

def get_photo_exif(photo_path):
    with Image.open(photo_path) as img:
        exif = img.getexif()
    return exif

while True:
    folder_path = input('輸入資料夾路徑: ')

    if not os.path.exists(folder_path):
        print('請輸入有效路徑。')
    else:
        break

index = 1
total = len(os.listdir(folder_path))

for photo in os.listdir(folder_path):
    try:
        print(f'({index} / {total}) ', end='')

        photo_path = os.path.join(folder_path, photo)
        if not os.path.isfile(photo_path): raise TypeError

        basename, ext = os.path.splitext(photo)

        exif_time = get_photo_exif(photo_path).get(306, None)

        if exif_time is not None:
            new_basename = datetime.datetime.strptime(str(exif_time), "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%d %H-%M-%S")

            if os.path.exists(os.path.join(folder_path, f'{new_basename}{ext}')):
                suffix = 1

                while os.path.exists(os.path.join(folder_path, f'{basename}_{suffix:02}{ext}')):
                    suffix += 1

                new_basename = datetime.datetime.strptime(str(exif_time), "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%d %H-%M-%S") + f'_{suffix:02}'

            new = os.path.join(folder_path, f'{new_basename}{ext}')

            os.rename(photo_path, new)

            print(f'{photo_path} -> {new}。')
    except TypeError:
        print(f'{photo_path} 並非一個檔案。')
    except Exception as e:
        print(f'未知錯誤 - ({e})')

    index += 1