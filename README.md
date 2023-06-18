<div align=center>
  <img src='https://github.com/oelin/coco/blob/main/images/snake.svg' width=60%>
</div>

# Coco

A library for creating self-extracting archives in Python.


## Overview

Coco is a data serialization library specialized for creating self-extracting archives (SEAs), i.e. a compressed stream which includes the decoder. SEAs are useful for distributing highly compressed files with uncommon, bespoke or proprietary codecs. The library currently utilized pickle as the outermost serialization format, however this is subject to change.


### Self-extracting Archives

A self-extracting archive is type of compressed file which also include the decompression program. A simple example would be an image compressed using LZW with an LZW decoder appended to the end of the file. The primary advantage of SEAs is that they allow for highly optimized domain specific compression while maintaining portability. 


### Security

One risk of SEAs is that they can essentially execute arbitrary code. The risk associated with decompressing an SEA is similar to the risk associated with running third party executables. For this reason, it's good practice to extract the data in a sandboxed environment.


## Usage

Create a decoder/extractor.

```py
import coco

@coco.decoder
def decode(data):
  # Decompression logic...
```

Create a self-extracting archive.

```py
archive = coco.encode(data, decoder)
```

Extract the original data.

```py
data = coco.decode(archive)
```

## Installation

```sh
pip install coco
```


## API

#### `coco.encode(data: Data, decoder: Decoder) -> Data`

Takes a compressed data stream and a decoder, returns a self-extracting archive.

#### `coco.decode(data: Data) -> Data`

Takes a self-extracting archive and returns an uncompressed data stream.
