# Mini — Termux AI Coding Assistant

Mini is a lightweight AI coding assistant for Termux.

## Features

- Gemma 4 26B A4B free as the primary OpenRouter model
- Automatic fallback to `openrouter/free` when the primary free provider is busy
- API key is requested at launch and is not stored in the package
- No Python third-party package is required by Mini itself
- Simple CLI UI

## Run from source

```bash
python3 mini.py
```

## Package

The repository contains a `termux-create-package` manifest and a GitHub Actions workflow that builds the .deb package and APT repository.

After the GitHub Pages repository is published, users can add the repository once and then install:

```bash
pkg update
pkg install mini
mini
```

> A custom APT repository must be added to Termux before `pkg install mini` can find this package.
