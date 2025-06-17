# semantic-evaluation-ai
Open-source script for evaluating semantic fidelity of biomedical translations using COMET.
# Semantic Evaluation of Biomedical Translations

This repository provides an open-source Python script for evaluating the **semantic fidelity** of machine-translated biomedical texts using the COMET model.

## Features

- Input: source and translated text files (sentence-aligned)
- Output: sentence-level semantic fidelity scores
- Based on: COMET Quality Estimation (QE)

## Usage

```bash
python evaluate_semantics_comet.py --source input_cz.txt --mt input_en.txt --output results.csv
