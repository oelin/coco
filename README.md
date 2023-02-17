# Coco

A library for creating self-extracting archives in Python.


## Usage

Create a decoder/extractor.

```py
def decoder():
  def decode(data):
    # Decompression logic...
    
  return decode
```

Create a self-extracting archive.

```py
import coco

archive = coco.encode(data, decoder)
```

Extract the original data.

```py
data = coco.decode(archive)
```
