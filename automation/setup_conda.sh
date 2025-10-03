#!/bin/bash
# Setup a conda environment and install ML packages

# Create and activate conda environment
conda create -y -n research_env python=3.10
source $(conda info --base)/etc/profile.d/conda.sh
conda activate research_env

# Install core libraries
pip install torch torchvision torchaudio matplotlib numpy

# Verify environment and packages
python - <<'EOF'
import sys
import torch
import numpy as np
print(f"Python version: {sys.version}")
print(f"PyTorch version: {torch.__version__}")
print(f"Numpy version: {np.__version__}")
EOF

echo "Conda environment setup complete."
