try:
    import hvac
    HAS_HVAC = True
except ImportError:
    HAS_HVAC = False

def create_argument_spec():

    argument_spec = dict()
    argument_spec.update(
        url=dict(required=True, type='str'),
        username=dict(required=True, aliases=['user', 'admin'], type='str'),
        password=dict(required=True, aliases=['pass', 'pwd'], type='str', no_log=True),
        path=dict(required=True, type='str')
    )
    return argument_spec


def main():
    argument_spec = create_argument_spec()
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)

    if not HAS_HVAC:
        module.fail_json(msg="Hashicorp Vault Python library hvac required, please install.") 

    try:
        client = hvac.Client(url=module.params['url'])
        client.auth_userpass(module.params['username'], module.params['password'])
        results = client.read(module.params['path'])['data']

        module.exit_json(**results)
    except Exception as e:
        module.fail_json(msg=str(e))


from ansible.module_utils.basic import *


if __name__ == '__main__':
    main()
