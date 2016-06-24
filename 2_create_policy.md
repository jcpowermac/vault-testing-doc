### Vault Policy
Vault Policy for Ansible secrets
#### ansible.hcl
```
path "secret/ansible/*" {
  policy = "write"
}

path "secret/ansible/*" {
  policy = "read"
}

path "auth/token/lookup-self" {
  policy = "read"
}
```

```
> $ ./vault auth e2ce682e-60b1-78c6-efc0-f444c0c3c6fc                                                                                                                                                   ```
```
Successfully authenticated! You are now logged in.
token: e2ce682e-60b1-78c6-efc0-f444c0c3c6fc
token_duration: 0
token_policies: [root]
```
```bash
> $ ./vault policy-write ansible ansible.hcl
Policy 'ansible' written.
```
