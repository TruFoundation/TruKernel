# 🐄 TruKernel

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)

**The manifest-driven dispatch engine for modern command-line tools.**

TruKernel is a lightweight, language-agnostic core that decouples command routing from execution logic. It allows developers to build extensible CLI applications where commands are defined in simple `.md` manifests rather than hardcoded registries.

> **Note:** TruKernel is an **engine**, not a shell. It powers applications like [TruShell](https://github.com/TruFoundation/TruShell), but can be embedded in any Python application requiring dynamic command dispatch.

## Features

*   **Manifest-Driven Architecture:** Define commands, aliases, and plugins in human-readable Markdown files. No recompilation needed.
*   **Lazy Loading:** Commands are imported only when invoked, ensuring fast startup times even with hundreds of plugins.
*   **OS Passthrough:** Unregistered commands automatically fall back to the host operating system’s shell (e.g., `bash`, `zsh`).
*   **Extensible Plugin System:** Load external modules dynamically via simple configuration.
*   **Clean Exit Protocol:** Uses sentinel values instead of `SystemExit` crashes for stable embedding.

## Installation

```bash
pip install trukernel
```
Or install from source:
```bash
git clone https://github.com/TruFoundation/TruKernel.git
cd TruKernel
pip install -e .
```

##  Quick Start

### 1. Create a Manifest
Create a file named `commands.md`:

```markdown
# My App Commands

{cmd: hello}; "run_hello()"; [my_app.commands];
{cmd: version}; "run_version()"; [my_app.core];
```

### 2. Initialize the Kernel

```python
from trukernel.engine import TruKernel

# Initialize the engine
kernel = TruKernel(manifest_path="commands.md")

# Execute a command
result = kernel.execute_command("hello")
if result == kernel.EXIT_SENTINEL:
    print("Exiting...")
```

### 3. Define Your Commands
In `my_app/commands.py`:

```python
def run_hello(args: str) -> str:
    return "Hello, World!"

def run_version(args: str) -> str:
    return "v1.0.0"
```

## Architecture

TruKernel follows a strict separation of concerns:

| Component | Responsibility |
| :--- | :--- |
| **Engine** (`trukernel/engine.py`) | Dispatches commands, manages registry, handles OS fallback. |
| **Parser** (`trukernel/parser.py`) | Parses Markdown manifests into executable routes. |
| **State** (`trukernel/state.py`) | Manages persistent data (history, config paths). |
| **Logger** (`trukernel/logging.py`) | Centralized logging with minimal overhead. |

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) and sign the [Contributor License Agreement (CLA)](CLA.md) before submitting pull requests.

##  License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.
