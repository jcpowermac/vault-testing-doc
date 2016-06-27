#### Current questions, issues and concerns 

- Need SSL certificate, how to generate?
- Determine a process (where?) of init, unseal, enable `userpass` and importing the policy
- Should this really be in a container?  If yes:
    - Need an entrypoint to take care of the process above and determine if it should be ran again when container is restarted.
    - If no: Need to write a systemd unit file to start and stop the service.  Examples might already exist
- Is userpass the proper auth method?


