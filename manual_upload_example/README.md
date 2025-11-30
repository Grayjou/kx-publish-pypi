# Manual Upload Example

This folder contains scripts and examples for manually building and uploading Python packages to PyPI.

## 🎯 Overview

There are two approaches available:

### 1. **Unified Pure Python Publisher (Recommended)** - `unified_publish.py`

A modern, cross-platform, pure Python solution for package publishing.

**Features:**
- ✅ Pure Python (no PowerShell or shell script dependencies)
- ✅ Cross-platform (works on Windows, macOS, Linux)
- ✅ Single-file TOML configuration support
- ✅ Secure token handling (environment variables, keyring, or config file)
- ✅ Transparent build and upload process with detailed logging
- ✅ Support for both TestPyPI and PyPI
- ✅ Clean build artifacts before building
- ✅ Version detection and validation
- ✅ Dry-run mode for testing

**Quick Start:**
```bash
# Basic usage - interactive mode
python unified_publish.py

# Publish to TestPyPI
python unified_publish.py --test

# Publish to PyPI
python unified_publish.py --prod

# Dry run (no actual upload)
python unified_publish.py --dry-run --prod

# Use a configuration file
python unified_publish.py --config publish_config.toml

# Skip confirmation prompts
python unified_publish.py --no-confirm --test
```

### 2. **Legacy PowerShell Scripts** - `publish.ps1` / `publish_test.ps1`

Windows-only PowerShell scripts for package publishing.

**Note:** These are provided for reference and backward compatibility. The unified Python publisher is recommended for new projects.

## 📁 Files

| File | Description |
|------|-------------|
| `unified_publish.py` | Pure Python cross-platform publisher |
| `publish_config.example.toml` | Example configuration file |
| `publish.py` | Legacy Python wrapper for PowerShell |
| `publish.ps1` | Legacy PowerShell script (production) |
| `publish_test.ps1` | Legacy PowerShell script (test) |
| `mock_config.txt` | Legacy configuration concept |

## 🔧 Configuration

### Option 1: TOML Configuration File

Copy `publish_config.example.toml` to `publish_config.toml` and customize:

```toml
[publish]
target = "test"  # or "prod"
confirm = true
clean = true

[package]
path = "."

[tokens]
# Use environment variables or keyring instead
# test = "pypi-..."  # NOT RECOMMENDED
# prod = "pypi-..."  # NOT RECOMMENDED
```

### Option 2: Environment Variables

```bash
# For TestPyPI
export TESTPYPI_TOKEN="pypi-xxxxx..."

# For PyPI
export PYPI_TOKEN="pypi-xxxxx..."
```

### Option 3: System Keyring (via kx-publish-pypi)

```bash
# Use the main kx-publish-pypi tool to set up tokens
kx-publish-pypi setup-tokens
```

## 🔒 Security

**Token Security Priority:**

1. **Most Secure:** System keyring via `kx-publish-pypi setup-tokens`
2. **Secure:** Environment variables
3. **Not Recommended:** Config file (never commit to version control)

**Important:**
- Never commit API tokens to version control
- Add `publish_config.toml` to `.gitignore`
- Use environment variables for CI/CD

## 📖 Usage Examples

### Basic Workflow

```bash
# 1. Navigate to your package directory
cd /path/to/your/package

# 2. Set up your token (choose one method)
export TESTPYPI_TOKEN="pypi-xxxxx..."
# OR
kx-publish-pypi setup-tokens

# 3. Run the publisher
python /path/to/unified_publish.py --test
```

### Dry Run (Test Without Uploading)

```bash
python unified_publish.py --dry-run --prod
```

### Automated Publishing (CI/CD)

```bash
# In your CI/CD pipeline, set the token as a secret
# Then run:
python unified_publish.py --no-confirm --prod
```

### Skip Build (Use Existing Artifacts)

```bash
# If you already built the package
python unified_publish.py --skip-build --test
```

## 🆚 Comparison: Unified Publisher vs kx-publish-pypi

| Feature | Unified Publisher | kx-publish-pypi |
|---------|-------------------|-----------------|
| Purpose | Standalone single-file solution | Full CLI tool |
| Dependencies | Minimal (tomli optional) | Rich, Click, etc. |
| Installation | Copy file to project | pip install |
| Features | Build & upload | Full workflow + checks |
| Best For | Simple projects, CI/CD | Interactive development |

**Recommendation:**
- Use **kx-publish-pypi** for development workflows
- Use **unified_publish.py** for simple automated publishing or as a reference implementation

## 📄 License

MIT License - Same as the main kx-publish-pypi project.

---

**Part of [kx-publish-pypi](https://github.com/Khader-X/kx-publish-pypi)** | Author: KhaderX.com
