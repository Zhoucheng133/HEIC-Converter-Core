# HEIC Convert Core

## 打包

```bash
nuitka --standalone --onefile core.py
```

## 使用

```bash
./core.bin <输入文件> <输出位置>
```

可选参数

```bash
# 质量 (默认80)
--quality <quality> 
# 不写入EXIF参数 (默认写入)
--no-exif
# 覆盖 (默认不覆盖)
--override
```