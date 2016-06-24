```bash
> $ ./vault write secret/foo value=bar
Success! Data written to: secret/foo
```
```bash
> $ ./vault auth -method=userpass username=jcallen
Password (will be hidden):
```
```bash
Successfully authenticated! You are now logged in.
The token below is already saved in the session. You do not
need to "vault auth" again with the token.
token: cb370eaa-a9ec-6a53-0fe4-b08d08945313
token_duration: 2591999
token_policies: [ansible, default]
```

```
> $ ./vault read secret/foo                                                                                                                                                                             [±master ●]
Error reading secret/foo: Error making API request.

URL: GET http://172.17.0.3:8200/v1/secret/foo
Code: 400. Errors:

* permission denied
```

```
> $ ./vault write secret/ansible/foo value=bar
Success! Data written to: secret/ansible/foo
```
```
> $ ./vault read secret/ansible/foo
```

```
Key                     Value
---                     -----
refresh_interval        2592000
value                   bar
```
