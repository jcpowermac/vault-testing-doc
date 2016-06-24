```
./vault auth-enable userpass
Successfully enabled 'userpass' at 'userpass'!
```

```bash
> $ ./vault write auth/userpass/users/jcallen password= policies=ansible
Success! Data written to: auth/userpass/users/jcallen
```
