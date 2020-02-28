from ansible.module_utils.basic import AnsibleModule
import wget

# url = 'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=661409485,3554849204&fm=15&gp=0.jpg'
# dst = '/tmp/girl.jpg'
# cd pip-20.0.2
# python setup.py install (python 2.7.5)
# pip2 install wget

def main():
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True, type='str'),
            dst=dict(required=True, type='str')
        )
    )
    wget.download(module.params['url'], module.params['dst'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()
