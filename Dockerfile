FROM quay.io/jupyter/minimal-notebook

LABEL maintainer="astromahdi <astromahdi@astromahdi.com>"

# Fix: https://github.com/hadolint/hadolint/wiki/DL4006
# Fix: https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN pip install --no-cache-dir \
    jupyterlab-pytutor

RUN mkdir -p /tmp/prepackaged
COPY doctest_example.py /tmp/prepackaged/
USER root
RUN chown -R jovyan:users /tmp/prepackaged
USER ${NB_UID}
