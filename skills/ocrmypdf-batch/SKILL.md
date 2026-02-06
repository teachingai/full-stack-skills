---
name: ocrmypdf-batch
description: OCRmyPDF batch processing skill — process multiple PDFs in bulk, use Docker containers, automate with shell scripts, and set up watch folders. Use when the user needs to OCR many PDFs at once, automate OCR in CI/CD, or run OCRmyPDF in Docker.
---

# OCRmyPDF — Batch Processing, Docker & Automation Guide

## Overview

This skill covers batch processing multiple PDFs, Docker deployment, shell scripting automation, and watch folder setups with OCRmyPDF.

For core OCR operations, see the **ocrmypdf** skill. For image processing, see **ocrmypdf-image**. For Python API, see **ocrmypdf-api**.

## Batch Processing with Shell

### Process all PDFs in a directory

```bash
#!/bin/bash
# OCR all PDFs in a directory
INPUT_DIR="./scans"
OUTPUT_DIR="./ocr-output"
mkdir -p "$OUTPUT_DIR"

for pdf in "$INPUT_DIR"/*.pdf; do
    filename=$(basename "$pdf")
    echo "Processing: $filename"
    ocrmypdf --skip-text -l eng "$pdf" "$OUTPUT_DIR/$filename"
done
echo "Done!"
```

### Parallel batch processing with GNU parallel

```bash
# Process all PDFs in parallel using GNU parallel
find ./scans -name "*.pdf" | parallel -j4 \
    ocrmypdf --skip-text -l eng {} ./output/{/}
```

### Recursive directory processing

```bash
#!/bin/bash
# Recursively OCR all PDFs, preserving directory structure
INPUT_DIR="./documents"
OUTPUT_DIR="./searchable"

find "$INPUT_DIR" -name "*.pdf" -type f | while read -r pdf; do
    rel_path="${pdf#$INPUT_DIR/}"
    out_path="$OUTPUT_DIR/$rel_path"
    mkdir -p "$(dirname "$out_path")"
    echo "OCR: $rel_path"
    ocrmypdf --skip-text -l eng "$pdf" "$out_path" 2>&1 || echo "FAILED: $rel_path"
done
```

### In-place OCR (overwrite originals on success)

```bash
#!/bin/bash
# OCR files in place — only overwrites on success
for pdf in ./documents/*.pdf; do
    echo "Processing: $pdf"
    ocrmypdf --skip-text "$pdf" "$pdf"
done
```

## Docker

### Official Docker images

Available for x64 and ARM:

```bash
# Pull the latest image
docker pull jbarlow83/ocrmypdf

# Basic usage
docker run --rm -v "$(pwd):/data" jbarlow83/ocrmypdf \
    /data/input.pdf /data/output.pdf

# With language and options
docker run --rm -v "$(pwd):/data" jbarlow83/ocrmypdf \
    -l eng+fra --deskew /data/input.pdf /data/output.pdf
```

### Batch processing with Docker

```bash
#!/bin/bash
# Batch OCR using Docker
INPUT_DIR="$(pwd)/scans"
OUTPUT_DIR="$(pwd)/output"
mkdir -p "$OUTPUT_DIR"

for pdf in "$INPUT_DIR"/*.pdf; do
    filename=$(basename "$pdf")
    echo "Processing: $filename"
    docker run --rm \
        -v "$INPUT_DIR:/input:ro" \
        -v "$OUTPUT_DIR:/output" \
        jbarlow83/ocrmypdf \
        --skip-text -l eng \
        "/input/$filename" "/output/$filename"
done
```

### Docker Compose (watch folder)

```yaml
# docker-compose.yml
version: '3'
services:
  ocrmypdf-watcher:
    image: jbarlow83/ocrmypdf
    volumes:
      - ./inbox:/inbox
      - ./outbox:/outbox
    entrypoint: >
      sh -c 'while true; do
        for f in /inbox/*.pdf; do
          [ -f "$$f" ] || continue;
          ocrmypdf --skip-text "$$f" "/outbox/$$(basename $$f)" &&
          rm "$$f";
        done;
        sleep 10;
      done'
```

## Watch Folder with Watcher Extension

OCRmyPDF provides an optional watcher service:

```bash
# Install watcher extension
pip install ocrmypdf[watcher]

# Run the watcher (monitors input folder, outputs to output folder)
# See OCRmyPDF docs for watcher configuration
```

## CI/CD Integration

### GitHub Actions example

```yaml
name: OCR PDFs
on: push
jobs:
  ocr:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install OCRmyPDF
        run: |
          sudo apt-get update
          sudo apt-get install -y ocrmypdf tesseract-ocr-eng
      - name: OCR all PDFs
        run: |
          mkdir -p output
          for pdf in docs/*.pdf; do
            ocrmypdf --skip-text "$pdf" "output/$(basename "$pdf")"
          done
      - uses: actions/upload-artifact@v4
        with:
          name: ocr-pdfs
          path: output/
```

## Convert Multiple Images to Searchable PDF

```bash
# Use img2pdf to combine images, then pipe to ocrmypdf
pip install img2pdf

# Combine and OCR
img2pdf scan_*.jpg | ocrmypdf - output.pdf

# Or one image at a time
ocrmypdf --image-dpi 300 scan.jpg output.pdf
```

## Quick Reference

| Task | Command |
|------|---------|
| Batch OCR directory | `for f in *.pdf; do ocrmypdf "$f" "out/$f"; done` |
| Parallel batch | `find . -name "*.pdf" \| parallel ocrmypdf {} out/{/}` |
| Docker single file | `docker run --rm -v "$(pwd):/data" jbarlow83/ocrmypdf /data/in.pdf /data/out.pdf` |
| In-place OCR | `ocrmypdf myfile.pdf myfile.pdf` |
| Images to PDF | `img2pdf *.jpg \| ocrmypdf - output.pdf` |

## Troubleshooting

- **Docker permission errors**: Ensure volume mounts are correct; use `--user $(id -u):$(id -g)` if needed.
- **Batch script fails on one file**: Add error handling (`|| echo "FAILED"`) to continue processing.
- **Memory issues on large batches**: Process files sequentially with `--jobs 1`, or limit parallel workers.

## References

- [OCRmyPDF Docker](https://ocrmypdf.readthedocs.io/en/latest/docker.html)
- [OCRmyPDF Cookbook: Batch Processing](https://ocrmypdf.readthedocs.io/en/latest/cookbook.html)
