<h1 align="center">
  <a href="ledger.com/vault"><img width="250" src="https://www.ledger.com/wp-content/themes/ledger-v2/public/images/ledger.svg"></a>
</h1>

<h3 align="center">vault_device_registry</h3>

Flask service using [ledgercommon](https://github.com/LedgerHQ/python-ledgercommon/tree/1.1.0).

<p align="center">
  <a href="https://codecov.io/gh/LedgerHQ/vault-device-registry">
    <img src="https://codecov.io/gh/LedgerHQ/vault-device-registry/branch/develop/graph/badge.svg?token=" />
  </a>
  <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Made%20with-Python3.8-1f425f.svg" />
  </a>
</p>

#### Build Status

<table>
  <tr>
    <th align="center">develop</th>
    <th align="center">master</th>
  </tr>
  <tr>
    <td align="center">
      <a href="https://circleci.com/gh/LedgerHQ/vault-device-registry/tree/develop">
        <img src="https://circleci.com/gh/LedgerHQ/vault-device-registry/tree/develop.svg?style=shield&circle-token=__MISSING_TOKEN__" />
      </a>
    </td>
    <td align="center">
      <a href="https://circleci.com/gh/LedgerHQ/vault-device-registry/tree/master">
        <img src="https://circleci.com/gh/LedgerHQ/vault-device-registry/tree/master.svg?style=shield&circle-token=__MISSING_TOKEN__" />
      </a>
    </td>
  </tr>
</table>

### Run the service locally

```sh
$ PYPI_KEY=<YOUR_PYPI_KEY> pipenv install
$ ./run_dev.sh &
$ curl localhost:5000/_health
```

### Build docker image

```sh
$ docker build --no-cache -t ledgerhq/vault-device-registry:local --build-arg PYPI_KEY=<YOUR_PYPI_KEY> .
$ docker-compose down && DOCKER_IMAGE_VERSION=local docker-compose up -d
$ curl localhost:5000/_health
```

### CircleCI setup

You will need a few env variables set in your [CircleCi settings](https://circleci.com/gh/LedgerHQ/vault-device-registry/edit#env-vars).

They can be imported from another CircleCI settings page by an administrator.

- For automatically building the docker image:
  - `DOCKER_ORGANIZATION`
  - `DOCKER_PASSWORD`
  - `DOCKER_USERNAME`
- For fetching the private Ledger python libraries:
  - `PYPI_KEY`

You'll also need an API token for the develop/master status badges above. You can generate one from the [settings page](https://circleci.com/gh/LedgerHQ/vault-device-registry/edit#api) of your repo.
