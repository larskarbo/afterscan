# Afterscan

![logo](afterscan-logo.JPG)

----

Usage

```
afterscan [OPTIONS] FILENAME
```

Example

```
afterscan myimage.jpg --threshold 75 -f
```

## Options

```
--threshold INTEGER         Threshold value between 0 and 255. Default=100
-o, --out TEXT              Output path. Default afterscan-[filename] in pwd
-i, --invert / --no-invert  Invert the image
-f, --force / --no-force    Overwrite existing file without asking
--help                      Show this message and exit.
```

## Demo

When drawing this amazing logo, I found myself having a scan with lines in the background.

By using this command I was able to produce the second image:


```
afterscan logo.jpg --threshold 75 -f
```

### Before

![image-before](afterscan-logo-before.JPG)

### After

![image-after](afterscan-logo.JPG)
