import os

# List of file paths to create within the project structure
structure = [
    "README.md",                   # Project overview and instructions
    "requirements.txt",            # List of Python dependencies
    "config/config.yaml",          # Configuration settings (API keys, paths, etc.)
    "src/main.py",                 # Entry point for the application
    "src/core/__init__.py",
    "src/core/agent.py",           # Main logic for autonomous coding, debugging, and optimization
    "src/core/dependency_manager.py",  # Manage code dependencies and graph analysis
    "src/models/__init__.py",
    "src/models/gpt4_handler.py",       # Interface for GPT-4 integration
    "src/models/codex_handler.py",      # Interface for OpenAI Codex
    "src/models/codebert_handler.py",   # Interface for CodeBERT functionality
    "src/indexing/__init__.py",
    "src/indexing/llamaindex_handler.py",  # Integration for LlamaIndex and RAG setup
    "src/langchain_integration/__init__.py",
    "src/langchain_integration/pipeline.py",  # Chain and prompt management with LangChain
    "src/utils/__init__.py",
    "src/utils/logger.py",          # Logging utilities for debugging and tracking
    "src/utils/file_utils.py",      # Helper functions for file operations
    "tests/test_agent.py",          # Unit tests for the core agent
    "tests/test_models.py",         # Tests for GPT-4, Codex, and CodeBERT integrations
    "tests/test_indexing.py",       # Tests for the indexing and retrieval functionalities
    "docs/architecture.md",         # Detailed architecture and design decisions
    "docs/usage.md"                 # How to set up, run, and extend the project
]

for file_path in structure:
    # Create any necessary directories
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    # Create the file (if it doesn't already exist)
    with open(file_path, 'w') as f:
        f.write("")  # You can add default content here if desired

print("Project structure created successfully!")
