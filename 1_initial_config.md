#### Configuration
```
backend "file" {
  path = "/var/opt/hashicorp/vault/"
}

listener "tcp" {
  address = "0.0.0.0:8200"
  tls_disable = 1
}
```
#### Docker RUN
See [notes.md](motes.md) for more information
```bash
> $ sudo docker run -it --cap-add IPC_LOCK vault                                                                                    ```

#### Results from RUN

```
==> Vault server configuration:

                 Backend: file
              Listener 1: tcp (addr: "0.0.0.0:8200", tls: "disabled")
               Log Level: info
                   Mlock: supported: true, enabled: true
                 Version: Vault v0.6.0

==> Vault server started! Log data will stream in below:
```

```bash
> $ export VAULT_ADDR='http://172.17.0.3:8200'
```
### vault init
```bash
./vault init
```
#### Results from vault init
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

### vault unseal
```
./vault unseal
```
#### Results from unseal
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
