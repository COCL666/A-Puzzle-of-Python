#!/usr/local/bin/python3
# yaml转为python的数据类型
[
    {
        'name': 'configure dbservers',
        'hosts': 'dbservers',
        'tasks':[
            {
                'name': 'install mariadb',
                'yum':{
                    'name': 'mariadb-server',
                    'state': 'present'
                }
            },
            {
                'name': 'start mariadb',
                'service':{
                        'name': 'mariadb',
                        'state': 'started',
                        'enabled': 'yes'
                }
            }
        ]
    },
    {
        'name': 'configure webservers',
        'hosts': 'webservers',
        'tasks':[
            {
                'name': 'install httpd',
                'yum':{
                    'name': 'httpd',
                    'state': 'present'
                }
            },
            {
                'name': 'start httpd',
                'service':{
                        'name': 'httpd',
                        'state': 'started',
                        'enabled': 'yes'
                }
            }
        ]
    }
]
