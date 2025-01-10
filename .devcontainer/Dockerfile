FROM mcr.microsoft.com/vscode/devcontainers/dotnet:8.0

RUN curl -sSL -O https://packages.microsoft.com/config/debian/$(grep VERSION_ID /etc/os-release | cut -d '"' -f 2 | cut -d '.' -f 1)/packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && rm packages-microsoft-prod.deb \
    && apt-get update -y \
    && ACCEPT_EULA=Y apt-get install -y \
    python3 \
    python3-venv \
    python3-pip \
    git \
    msodbcsql18 \
    mssql-tools18 \
    unixodbc-dev \
    libgssapi-krb5-2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="$PATH:/opt/mssql-tools18/bin"

ARG VENV_PATH="/home/vscode/venv"
COPY requirements.txt /tmp/deps/
COPY .devcontainer/motd.txt /etc/motd
RUN su vscode -c "python3 -m venv ${VENV_PATH}"  \
    && . ${VENV_PATH}/bin/activate \
    && pip install --no-cache-dir --disable-pip-version-check -r /tmp/deps/requirements.txt \
    && rm -rf /tmp/deps

