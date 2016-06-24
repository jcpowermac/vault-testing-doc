# Notes

```
jcallen@silicon ~/Development/vault-testing-doc              [13:05:05]
> $ sudo docker run -it vault                               [±master ●]
Error initializing core: Failed to lock memory: cannot allocate memory

This usually means that the mlock syscall is not available.
Vault uses mlock to prevent memory from being swapped to
disk. This requires root privileges as well as a machine
that supports mlock. Please enable mlock on your system or
disable Vault from using it. To disable Vault from using it,
set the `disable_mlock` configuration option in your configuration
file.
```
[Fix for above](https://github.com/cgswong/docker-vault/issues/4)
