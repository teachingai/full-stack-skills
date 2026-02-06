---
name: ocrmypdf-optimize
description: OCRmyPDF optimization skill — control PDF/A output, optimization levels, JBIG2 compression, image quality, and rasterizer selection. Use when the user needs to reduce PDF file size, produce archival PDF/A, or fine-tune OCR output quality.
---

# OCRmyPDF — Optimization & Output Guide

## Overview

OCRmyPDF optimizes PDF images by default after OCR. This guide covers optimization levels, PDF/A output options, JBIG2 encoding, and advanced output control.

For core OCR operations, see the **ocrmypdf** skill. For image processing, see **ocrmypdf-image**.

## Optimization Levels

The `--optimize N` (`-O N`) flag controls optimization intensity (0-3):

| Level | What it does |
|-------|-------------|
| `-O 0` | No optimization |
| `-O 1` | Lossless optimization (default) |
| `-O 2` | Lossless + lossy PNG quantization (pngquant) |
| `-O 3` | Aggressive: all of the above maximized |

```bash
# No optimization (fastest, largest output)
ocrmypdf --optimize 0 input.pdf output.pdf

# Default lossless optimization
ocrmypdf input.pdf output.pdf

# Moderate lossy optimization (smaller files)
ocrmypdf --optimize 2 input.pdf output.pdf

# Maximum compression
ocrmypdf --optimize 3 input.pdf output.pdf
```

**Note**: `-O 2` and `-O 3` require **pngquant** installed.

## PDF/A Output

PDF/A is a format for long-term archival. OCRmyPDF produces PDF/A by default.

```bash
# PDF/A output (default)
ocrmypdf --output-type pdfa input.pdf output.pdf

# Standard PDF (no PDF/A conversion)
ocrmypdf --output-type pdf input.pdf output.pdf

# Auto (v17+) — speculative PDF/A with verapdf validation
ocrmypdf --output-type auto input.pdf output.pdf
```

### PDF/A Image Compression

```bash
# JPEG compression for color/grayscale images in PDF/A
ocrmypdf --output-type pdfa --pdfa-image-compression jpeg input.pdf output.pdf

# Lossless compression (default)
ocrmypdf --output-type pdfa --pdfa-image-compression lossless input.pdf output.pdf
```

### PDF/A Without Ghostscript (v17+)

With verapdf installed, OCRmyPDF can produce PDF/A without Ghostscript (faster):

```bash
ocrmypdf --output-type auto input.pdf output.pdf
```

## JBIG2 Encoding

JBIG2 significantly reduces monochrome image size. Requires **jbig2enc** installed.

```bash
# OCRmyPDF automatically uses jbig2enc if available on PATH
ocrmypdf --optimize 1 input.pdf output.pdf
```

**Note**: Lossy JBIG2 (`--jbig2-lossy`) was removed in v17.0.0 due to character substitution risks. Only lossless JBIG2 is supported.

### Install jbig2enc

```bash
# Build from source (not available in most package managers)
git clone https://github.com/agl/jbig2enc
cd jbig2enc
./autogen.sh && ./configure && make && sudo make install
```

## Optimize Without OCR

```bash
# Optimize images without performing any OCR
ocrmypdf --ocr-engine none --optimize 3 --skip-text input.pdf output.pdf
```

## Digitally Signed PDFs

OCRmyPDF cannot preserve digital signatures. By default it refuses to modify signed PDFs.

```bash
# Override (invalidates signatures)
ocrmypdf --invalidate-digital-signatures input.pdf output.pdf
```

## Quick Reference

| Task | Command |
|------|---------|
| No optimization | `ocrmypdf -O 0 input.pdf output.pdf` |
| Default (lossless) | `ocrmypdf input.pdf output.pdf` |
| Moderate compression | `ocrmypdf -O 2 input.pdf output.pdf` |
| Maximum compression | `ocrmypdf -O 3 input.pdf output.pdf` |
| Standard PDF (no PDF/A) | `ocrmypdf --output-type pdf input.pdf output.pdf` |
| JPEG in PDF/A | `ocrmypdf --pdfa-image-compression jpeg input.pdf output.pdf` |
| Optimize only (no OCR) | `ocrmypdf --ocr-engine none -O 3 --skip-text in.pdf out.pdf` |
| Handle signed PDFs | `ocrmypdf --invalidate-digital-signatures in.pdf out.pdf` |

## Troubleshooting

- **Output larger than input**: This can happen; try `-O 2` or `-O 3`, or `--pdfa-image-compression jpeg`.
- **pngquant not found**: Install pngquant for `-O 2` / `-O 3`.
- **"Signed PDF" error**: Use `--invalidate-digital-signatures` (signatures will be lost).
- **Slow PDF/A**: Install pypdfium2 and verapdf for faster speculative PDF/A (v17+).

## References

- [OCRmyPDF: PDF Optimization](https://ocrmypdf.readthedocs.io/en/latest/optimizer.html)
- [OCRmyPDF Cookbook](https://ocrmypdf.readthedocs.io/en/latest/cookbook.html#pdf-optimization)
- [jbig2enc](https://github.com/agl/jbig2enc)
