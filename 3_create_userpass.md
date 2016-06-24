
#### Enable [userpass](https://www.vaultproject.io/docs/auth/userpass.html) auth backend
```
./vault auth-enable userpass
Successfully enabled 'userpass' at 'userpass'!
```
Once `userpass` is enabled we can create users
```bash
> $ ./vault write auth/userpass/users/jcallen password= policies=ansible
Success! Data written to: auth/userpass/users/jcallen
```


[Next](4_write_read_example.md)
