# Multilingual Font Maker

A web application that enables users to create and generate fonts for all 150 writing systems used today. Built on top of DeepVecFont-v2 (CVPR 2023), this app supports both font format conversion and custom font generation from image samples.

## Features

- **150 Writing Systems Support**: Covers all major and minor writing systems used globally
- **Multiple Input Methods**:
  - Upload `.ttf` font files to convert/adapt for other languages
  - Upload image samples to create custom fonts
- **Few-shot Learning**: Generate fonts with minimal examples using DeepVecFont-v2
- **Quality Selection**: Automatically selects best results using IOU metrics
- **SVG Output**: High-quality vector fonts in SVG format
- **Batch Processing**: Generate multiple character sets efficiently

## Technology Stack

- **Backend**: Python/Flask
- **ML Framework**: PyTorch + Transformers (DeepVecFont-v2)
- **Frontend**: React/TypeScript
- **File Processing**: FontForge integration for TTF conversion
- **Rendering**: CairoSVG for SVG generation

## Writing Systems Supported

The app supports 150+ writing systems including:
- Latin (English, French, Spanish, etc.)
- Cyrillic (Russian, Ukrainian, etc.)
- Greek, Armenian, Georgian
- Arabic, Hebrew, Persian, Urdu
- Devanagari (Hindi, Sanskrit)
- Chinese (Simplified & Traditional)
- Japanese (Hiragana, Katakana, Kanji)
- Korean (Hangul)
- Thai, Lao, Khmer
- Myanmar, Tibetan, Mongolian
- And many more...

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/fengzhou2520-debug/fontMaker.git
cd fontMaker

# Create conda environment
conda create -n fontmaker python=3.9
conda activate fontmaker

# Install dependencies
pip install -r requirements.txt

# Install FontForge (system-level)
apt install python3-fontforge  # Linux
# or
brew install fontforge  # macOS
```

### Running the App

```bash
# Start backend server
python app.py

# In another terminal, start frontend
cd frontend
npm install
npm start
```

Access the app at `http://localhost:3000`

## API Endpoints

### POST /api/upload
Upload font file or image sample
- `file`: .ttf file or image file
- `language`: Target language code
- `description`: What the sample represents

### POST /api/generate
Generate fonts for specified writing system
- `language`: Target language
- `referenceCharIds`: Character indices to use as references
- `nSamples`: Number of candidates to generate

### GET /api/results/{taskId}
Retrieve generated font results

### GET /api/download/{taskId}
Download generated font as SVG or TTF

## Project Structure

```
fontMaker/
├── backend/
│   ├── app.py                 # Flask application
│   ├── api/
│   │   ├── upload.py         # File upload handling
│   │   ├── generate.py       # Font generation pipeline
│   │   └── download.py       # Result export
│   ├── models/
│   │   ├── deepvecfont.py   # DeepVecFont-v2 wrapper
│   │   └── font_processor.py # Font processing utilities
│   ├── writing_systems.py    # 150 writing systems definitions
│   ├── utils/
│   │   ├── image_processor.py
│   │   ├── font_converter.py
│   │   └── validators.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── UploadForm.tsx
│   │   │   ├── LanguageSelector.tsx
│   │   │   └── ResultsViewer.tsx
│   │   ├── pages/
│   │   │   └── App.tsx
│   │   └── services/
│   │       └── api.ts
│   └── package.json
├── docker-compose.yml
└── README.md
```

## Usage Example

### 1. Font Conversion (TTF to Other Languages)

```bash
curl -X POST http://localhost:5000/api/upload \
  -F "file=@my_font.ttf" \
  -F "language=ja" \
  -F "description=Convert English font to Japanese"
```

### 2. Custom Font Generation from Images

```bash
curl -X POST http://localhost:5000/api/upload \
  -F "file=@sample_image.png" \
  -F "language=hi" \
  -F "description=Create Devanagari font from sample"
```

### 3. Generate Results

```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "language": "ja",
    "referenceCharIds": [0, 5, 10, 15],
    "nSamples": 20
  }'
```

## Model Details

Based on **DeepVecFont-v2: Exploiting Transformers to Synthesize Vector Fonts with Higher Quality** (CVPR 2023)

- Uses Transformer architecture for high-quality font synthesis
- Few-shot learning capability - generates fonts from minimal examples
- Produces SVG vector fonts for perfect scalability
- IOU-based selection for optimal glyph generation

## Requirements

- Python 3.9+
- CUDA 11.7 (GPU recommended)
- 8GB+ RAM (16GB recommended)
- FontForge library

See `requirements.txt` for full dependency list.

## License

This project builds upon DeepVecFont-v2, which is licensed under the terms of its original publication.

**Note**: Font copyright applies to generated fonts. Please respect font licenses when using commercial fonts as input.

## Citation

```bibtex
@inproceedings{wang2023deepvecfont,
  title={DeepVecFont-v2: Exploiting Transformers to Synthesize Vector Fonts with Higher Quality},
  author={Wang, Yuqing and Wang, Yizhi and Yu, Longhui and Zhu, Yuesheng and Lian, Zhouhui},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={18320--18328},
  year={2023}
}
```

## Contributing

Contributions are welcome! Please submit pull requests or open issues for bugs and feature requests.
