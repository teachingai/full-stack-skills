---
name: ocrmypdf-image
description: OCRmyPDF image processing skill — deskew crooked pages, auto-rotate, remove backgrounds, and clean scanned images before OCR. Use when the user needs to fix page rotation, straighten crooked scans, or clean up noisy scanned PDFs.
---

# OCRmyPDF — Image Processing Guide

## Overview

OCRmyPDF can perform image processing on each page of a PDF before OCR. These operations fix common scanning issues: crooked pages, wrong orientation, noisy backgrounds, and dirty scans. Processing is applied per-page.

For core OCR operations (install, languages, modes), see the **ocrmypdf** skill. For optimization, see **ocrmypdf-optimize**.

**Important**: Image processing will rasterize PDF pages as images, potentially losing vector content quality. Always review output files.

## Image Processing Options

### Rotate Pages (`--rotate-pages`)

Automatically detects and corrects page orientation (0/90/180/270 degrees).

```bash
# Auto-rotate misoriented pages
ocrmypdf --rotate-pages input.pdf output.pdf

# Adjust rotation aggressiveness (default: 14.0, lower = more aggressive)
ocrmypdf --rotate-pages --rotate-pages-threshold 2.0 input.pdf output.pdf
```

**Tip**: Use `-v1` to see confidence levels per page and tune the threshold.

### Deskew (`--deskew`)

Straightens pages that were scanned at a slight angle (crooked scans).

```bash
# Straighten crooked pages
ocrmypdf --deskew input.pdf output.pdf
```

**Note**: `--deskew` fixes "slightly off horizontal" pages. For pages at the wrong cardinal angle (90/180/270), use `--rotate-pages`.

### Remove Background (`--remove-background`)

Attempts to detect and remove noisy backgrounds from grayscale/color images. Monochrome images are ignored.

```bash
# Remove noisy background
ocrmypdf --remove-background input.pdf output.pdf
```

**Warning**: Do not use on documents with color photos — it may remove them.

### Clean (`--clean`)

Uses [unpaper](https://www.flameeyes.eu/projects/unpaper) to clean pages before OCR, but does **not** alter the final output PDF. Improves OCR accuracy without changing appearance.

```bash
# Clean for better OCR (output unchanged)
ocrmypdf --clean input.pdf output.pdf
```

**Requires**: unpaper installed on the system.

### Clean Final (`--clean-final`)

Like `--clean`, but inserts the cleaned page into the final output. Review each page — unpaper may remove important content.

```bash
# Clean and use cleaned version in output
ocrmypdf --clean-final input.pdf output.pdf
```

**Warning**: May leave visual artifacts. Always review output.

### Oversample (`--oversample DPI`)

Resample images to higher resolution before OCR, which can improve accuracy for low-DPI scans.

```bash
# Oversample to 400 DPI
ocrmypdf --oversample 400 input.pdf output.pdf
```

## Combining Options

Image processing options can be combined freely. The order of command-line flags does not matter — OCRmyPDF always applies them in this fixed order:

1. Rotate
2. Remove background
3. Deskew
4. Clean

```bash
# Full processing pipeline
ocrmypdf --rotate-pages --deskew --clean input.pdf output.pdf

# Deskew + clean final (aggressive cleanup)
ocrmypdf --deskew --clean-final input.pdf output.pdf

# Everything: rotate, remove background, deskew, clean
ocrmypdf --rotate-pages --remove-background --deskew --clean input.pdf output.pdf
```

## Processing Without OCR

Apply image processing without performing OCR:

```bash
# Deskew and convert to PDF/A, no OCR
ocrmypdf --ocr-engine none --deskew --output-type pdfa input.pdf output.pdf
```

## Rasterizer Selection (v17+)

Choose the PDF rasterization engine:

```bash
# Auto (default) — prefers pypdfium2 when available
ocrmypdf --rasterizer auto input.pdf output.pdf

# Explicitly use pypdfium2 (faster)
ocrmypdf --rasterizer pypdfium input.pdf output.pdf

# Explicitly use Ghostscript
ocrmypdf --rasterizer ghostscript input.pdf output.pdf
```

## Quick Reference

| Option | What it does | Notes |
|--------|-------------|-------|
| `--rotate-pages` | Fix page orientation (90/180/270) | Use threshold to tune |
| `--deskew` | Straighten slightly crooked pages | For small angles |
| `--remove-background` | Remove noisy backgrounds | Not for photos |
| `--clean` | Clean pages for OCR only | Output unchanged |
| `--clean-final` | Clean pages, use in output | Review output! |
| `--oversample DPI` | Upscale images before OCR | Improves low-DPI scans |
| `--rasterizer auto/pypdfium/ghostscript` | Choose rasterizer | v17+ |

## Common Recipes

### Fix a crooked batch scan

```bash
ocrmypdf --deskew --rotate-pages input.pdf output.pdf
```

### Clean a noisy old document

```bash
ocrmypdf --deskew --clean --remove-background input.pdf output.pdf
```

### Maximum preprocessing

```bash
ocrmypdf --rotate-pages --deskew --clean-final --oversample 400 input.pdf output.pdf
```

## Troubleshooting

- **`--clean` fails**: Install unpaper (`apt install unpaper` or equivalent).
- **`--remove-background` removes photos**: Only use on text-only documents; skip for documents with images.
- **`--clean-final` artifacts**: Review output; try `--clean` instead (does not alter output).
- **Low OCR quality after processing**: Try `--oversample 300` or `--oversample 400`.

## References

- [OCRmyPDF Cookbook: Image Processing](https://ocrmypdf.readthedocs.io/en/latest/cookbook.html#image-processing)
- [unpaper](https://www.flameeyes.eu/projects/unpaper)
