#### Current questions, issues and concerns 

- Where do we store the unseal keys?
- Need SSL certificate, how to generate?
- Determine a process (where?) of init, unseal, enable `userpass` and importing the policy
- Should this really be in a container?  
    - If yes: Need an entrypoint script to take care of the start/stop process.
    - If no: Need to write a systemd unit file to start and stop the service.
- Should another method of authentication should be used than userpass


