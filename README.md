# 相片檔名編輯器
自動抓取相片的 EXIF 資訊並將檔名變更為 `%Y-%m-%d %H-%M-%S` 的格式。

## 運作原理
使用 `pillow` 抓取相片的 EXIF 資訊並使用 `os` 及 `datetime` 將檔案依 `%Y-%m-%d %H-%M-%S` 的格式重新命名。

## 前置作業
### 複製儲存庫
```bash
git clone https://github.com/bruh0422/Photo-Rename-EXIF.git
cd Photo-Rename-EXIF
```

## 開始使用
```bash
python run.py
```
接下來按照程式指定的步驟操作即可。
