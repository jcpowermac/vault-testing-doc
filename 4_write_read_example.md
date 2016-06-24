#### Write and Read data

Using the root token lets create some dummy data
```bash
> $ ./vault write secret/foo value=bar
Success! Data written to: secret/foo
```
And now that I have created a user for myself lets login with my jcallen account
```bash
> $ ./vault auth -method=userpass username=jcallen
Password (will be hidden):
Successfully authenticated! You are now logged in.
The token below is already saved in the session. You do not
need to "vault auth" again with the token.
token: cb370eaa-a9ec-6a53-0fe4-b08d08945313
token_duration: 2591999
token_policies: [ansible, default]
```

Let's try to read the data that root just wrote.
```
> $ ./vault read secret/foo                                                                                                                                                                             [±master ●]
Error reading secret/foo: Error making API request.

URL: GET http://172.17.0.3:8200/v1/secret/foo
Code: 400. Errors:

* permission denied
```
No luck! Of course this was as intended.

I should be able to write to `secret/ansible` lets try that
```
> $ ./vault write secret/ansible/foo value=bar
Success! Data written to: secret/ansible/foo
```
And make sure we can read it too.
```
> $ ./vault read secret/ansible/foo
Key                     Value
---                     -----
refresh_interval        2592000
value                   bar
```
