import os, datetime
from PIL import Image

def get_image_exif(image_path):
    with Image.open(image_path) as image:
        exif = image.getexif()
    return exif

while True:
    folder_path = input('輸入資料夾路徑: ')

    if not os.path.exists(folder_path):
        print('請輸入有效路徑。')
    else:
        break

index = 1
total = len(os.listdir(folder_path))

for image in os.listdir(folder_path):
    try:
        print(f'({index} / {total}) ', end='')

        image_path = os.path.join(folder_path, image)
        if not os.path.isfile(image_path): raise TypeError

        basename, ext = os.path.splitext(image)

        exif_time = get_image_exif(image_path).get(306, None)

        if exif_time is not None:
            new_basename = datetime.datetime.strptime(str(exif_time), "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%d %H-%M-%S")

            if os.path.exists(os.path.join(folder_path, f'{new_basename}{ext}')):
                suffix = 1

                while os.path.exists(os.path.join(folder_path, f'{new_basename}_{suffix:02}{ext}')):
                    suffix += 1

                new_basename = datetime.datetime.strptime(str(exif_time), "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%d %H-%M-%S") + f'_{suffix:02}'

            new = os.path.join(folder_path, f'{new_basename}{ext}')

            os.rename(image_path, new)

            print(f'{image_path} -> {new}。')
    except TypeError:
        print(f'{image_path} 並非一個檔案。')
    except Exception as e:
        print(f'未知錯誤 - ({e})')

    index += 1