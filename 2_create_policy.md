#### Vault Policy
We want to create a policy where users only have access to a specific location.  
The policy below will force `ansible` users to only read/write in the `secret/ansible` location.

[ansible.hcl](example/vault/ansible.hcl) 

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

First we will auth using our root token
```
> $ ./vault auth e2ce682e-60b1-78c6-efc0-f444c0c3c6fc
Successfully authenticated! You are now logged in.
token: e2ce682e-60b1-78c6-efc0-f444c0c3c6fc
token_duration: 0
token_policies: [root]
```
Next create the policy
```bash
> $ ./vault policy-write ansible ansible.hcl
Policy 'ansible' written.
```


[Next](3_create_userpass.md)
