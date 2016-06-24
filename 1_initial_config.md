#### [Server Configuration](https://www.vaultproject.io/docs/config/index.html)
For more details see Hashicorp Vault documentation. Since we will only have a single node
file as a backend is sufficient.

[vault.hcl](example/vault.hcl) 
---
```
backend "file" {
  path = "/var/opt/hashicorp/vault/"
}

listener "tcp" {
  address = "0.0.0.0:8200"
  tls_disable = 1
}
```

#### Build Image
```bash
> $ sudo docker build -t vault .
```

#### Run Container
```bash
> $ sudo docker run -it --cap-add IPC_LOCK vault                                                                                    ```
```
See [notes.md](notes.md) for more information regarding `--cap-add`.

#### Immediate interactive results

```
==> Vault server configuration:

                 Backend: file
              Listener 1: tcp (addr: "0.0.0.0:8200", tls: "disabled")
               Log Level: info
                   Mlock: supported: true, enabled: true
                 Version: Vault v0.6.0

==> Vault server started! Log data will stream in below:
```

The vault server is running in the container and I am running the client on my local machine.
First we need to set an environmental variable.
```bash
> $ export VAULT_ADDR='http://172.17.0.3:8200'
```
#### vault init
Next initialize the vault.
```bash
./vault init
```
Typically the unseal keys would be kept private but this is just an example.  By default
five unseal keys are created.
```
Unseal Key 1: 19ba958fd12e7c15bc5e6f228e48a847d04447aba1773f233c4da031bb6589b601
Unseal Key 2: 19d0d0fffd4668fd51b5e6380c49c6c8624393e5be1e35b9b7742260a57641b302
Unseal Key 3: d8ee2daa090844e7b3076a2ce708e3462a68d4c4b2485e7a66b39154df10cfae03
Unseal Key 4: 3a8c7c9a22f2bbc52dc6f1b211ac1fd3c4c449e0a7257c6ff8da5afb7f3b941304
Unseal Key 5: fbb281cfd6bc97dfcf747da6faed3a5d8cef0ec1ab7317ac291de9cf055d1a0e05
Initial Root Token: e2ce682e-60b1-78c6-efc0-f444c0c3c6fc

Vault initialized with 5 keys and a key threshold of 3. Please
securely distribute the above keys. When the Vault is re-sealed,
restarted, or stopped, you must provide at least 3 of these keys
to unseal it again.

Vault does not store the master key. Without at least 3 keys,
your Vault will remain permanently sealed.

```

#### vault unseal
```
./vault unseal
```
Unseal needs to be ran for at least three times in this example based on the current `key threshold`.

```bash
> $ ./vault unseal
Key (will be hidden):
Sealed: true
Key Shares: 5
Key Threshold: 3
Unseal Progress: 1

> $ ./vault unseal
Key (will be hidden):
Sealed: true
Key Shares: 5
Key Threshold: 3
Unseal Progress: 2

> $ ./vault unseal
Key (will be hidden):
Sealed: false
Key Shares: 5
Key Threshold: 3
Unseal Progress: 0
```

[Next](2_create_policy.md)

