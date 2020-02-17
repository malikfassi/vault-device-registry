# We use a multi-step build to make sure the SSH private key
# used for git clone is not found in the final image we push.
FROM python:3.8-slim AS intermediate

ADD . /app
WORKDIR /app

ARG PYPI_DEPLOY_TOKEN
ENV PYPI_DEPLOY_TOKEN $PYPI_DEPLOY_TOKEN
RUN /app/install_pip_deps.sh

FROM python:3.8-slim

ADD . /app
WORKDIR /app

COPY --from=intermediate /app/.venv /app/.venv

RUN /app/install_run_deps.sh
# default port for dev env
EXPOSE 5002

CMD [ "/app/run.sh" ]
