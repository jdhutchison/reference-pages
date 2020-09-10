---
title: Vault
weight: 1
---


Installation
------------

Ansible play to deploy and set up exists.


Initialisation
-------------
To get the initial settings:

```bash
export VAULT_ADDR=http://127.0.0.1:8200
vault operator init > /etc/vault/init.file
```

This will get the initial unseal keys and token.

### Unsealing vault
The vault is sealed initially and needs to be unsealed and prior to that the token must be set for the CLI client to be usable.

```bash
export VAULT_TOKEN="<token>"
vault operator unseal
```

The last command will prompt for a key from the initial key shards. It needs to be repeated three times to complete the unsealing.

### Eanbling plugins and authentication methods

To enable the approle (for policies) and user/passphrase authentication:

```bash
vault auth enable userpass
vault auth enable approle
```

Usage
-----

To login with the CLI client:

```bash
vault login <token>
```

### Policies

[Vault policy documentation](https://www.vaultproject.io/docs/concepts/policies)

Policies are defined in HCL which has one or more namespaces for secrets each of which have an array of permissions.

Namespaces can have glob style __*__ at the end to match anything or __+__ in the middle of a path as a wildcard (eg. *secrets/foo/v+/bar* to match *secrets/foo/v1.0/bar* and *secrets/foo/v2/bar*).

The possible permissions are: create, update, read, list, delete, deny and sudo (which allows access to paths otherwise reserved for root). Deny takes precedence over everything.

#### Example policy

```json
# This allows the user to create "secret/foo" with a parameter named
# "bar". The parameter "bar" can only contain the values "zip" or "zap",
# but any other parameters may be created with any value.
path "secret/foo" {
capabilities = ["create"]
allowed_parameters = {
"bar" = ["zip", "zap"]
"*"   = []
}
}
```

#### Create policy via CLI

```bash
vault policy [write/delete/read] <policy name> <path to hcl for writes>
```

#### Create policy via API
The policy HCL needs to be contained in JSON, eg. `{"policy": "<POLICY HCL>"}`

```
curl -X PUT/POST/GET/DELETE --header "X-Vault-Token: <TOKEN>" --data '<POLICY JSON>' https://hutch.id.au/vault/v1/sys/policy/<policy-name>
```


### Set up a new token

Via command line:

```bash
vault token create -policy=<policy a> -policy=<policy b>
```

Via API:

[Vault token API documentation](https://www.vaultproject.io/api/auth/token)

```bash
curl -X POST --header "X-Vault-Token: <TOKEN>" --data '<TOKEN HCL>' https://hutch.id.au/vault/v1/auth/token/create
```

Sample body:
```json
{
"role_name": "moonbear-backups",
"policies": ["moonbear-backups"],
"meta": {
"user": "associated user"
},
"no_parent": true,
"ttl": "168h"
"type": "service",
}
```

### Set up a user with credentials
