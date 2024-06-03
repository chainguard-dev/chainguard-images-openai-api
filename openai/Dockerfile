# syntax=docker/dockerfile:1

FROM cgr.dev/chainguard/python:latest-dev as dev

WORKDIR //openai-run

RUN python -m venv venv
ENV PATH="//openai-run/venv/bin":$PATH
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM cgr.dev/chainguard/python:latest

WORKDIR //openai-run

COPY gpt.py gpt.py
COPY --from=dev //openai-run/venv //openai-run/venv
ENV PATH="//openai-run/venv/bin:$PATH"

ENTRYPOINT ["python", "gpt.py"]



