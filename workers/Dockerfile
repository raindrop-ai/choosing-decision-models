FROM python:3.12.16-slim-bookworm

ARG REQUIREMENTS_FILE=workers/requirements.txt
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc=4:12.2.0-3 gcc-12=12.2.0-14+deb12u1 libc6-dev=2.36-9+deb12u14 \
    && rm -rf /var/lib/apt/lists/*
COPY ${REQUIREMENTS_FILE} /requirements.txt
RUN python -m pip install --no-cache-dir --require-hashes --only-binary=:all: -r /requirements.txt
COPY evaluation/reference/ /app/
ENV PYTHONDONTWRITEBYTECODE=1 \
    TOKENIZERS_PARALLELISM=false \
    USE_TF=0 \
    PYTHONPATH=/app \
    HOME=/tmp \
    HF_HOME=/tmp/huggingface \
    TORCHINDUCTOR_CACHE_DIR=/tmp/torchinductor \
    TRITON_CACHE_DIR=/tmp/triton
WORKDIR /app
CMD ["python", "-c", "import torch; print(torch.__version__, torch.version.cuda)"]
