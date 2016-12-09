from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client
import os
    
auth = v3.Password(auth_url=os.environ['OS_AUTH_URL'],
                    username=os.environ['OS_USERNAME'],
                    password=os.environ['OS_PASSWORD'],
                   project_name=os.environ['OS_PROJECT_NAME'],
                   user_domain_name=os.environ['OS_USER_DOMAIN_NAME'],
                    project_domain_name=os.environ['OS_PROJECT_DOMAIN_NAME'])
sess = session.Session(auth=auth)
# print sess.__dict__
nova = client.Client("2.1", session=sess)

# list instance
# nova_host = nova.hosts.list()
# print nova_host
# nova_name = nova.servers.list()
# print dir(nova_name[0])
# print getattr(nova_name[0], 'OS-EXT-STS:task_state')
# print dir(nova_name[0])
# for i in nova_name:
# #     print getattr(i, 'OS-EXT-STS:task_state')
#     print getattr(i,'OS-EXT-STS:vm_state')
#     print getattr(i,'OS-DCF:diskConfig')
# #     print getattr(i,'OS-SRV-USG:launched_at')
# #     print getattr(i,'OS-EXT-AZ:availability_zone')
#     print i.name,i.status,i.networks,i.id,i.flavor
# nova_id = nova.servers.find(name="nova1")
# print nova_id.__dict__
# nova_ip = nova.servers.ips("0400c226-3345-4932-a99a-6d22690597f4")
# print nova_ip
# print client.servers.list()
# print nova.flavors.list()
# print nova_name
# print nova.networks.list()

#create instances
image = nova.images.find(name="cirros")
flavor = nova.flavors.find(name="m1.tiny")
network = nova.networks.list()
net = nova.networks.find(label="selfservice")
# print dir(network[0])
# for i in network: 
#     print i.label
# print network.__dict__
# net_id = [your_net_id]
# nics = [{"net-id": net_id, "v4-fixed-ip": ''}]
nics = [{'net-id': net.id}]

# nova_new_instance = nova.servers.create(name="test21",image=image,flavor=flavor,nics=nics)

#update instance
# nova_id = nova.servers.find(name="test21")
# print "nova id use name"
# print nova_id

#!/usr/bin/env python
# import os
# from keystoneclient.v3 import client as kclient
# from novaclient import client as nova_client
# 
# conn = kclient.Client(user_domain_name=os.environ['OS_USER_DOMAIN_NAME'],
#                     username=os.environ['OS_USERNAME'],
#                     password=os.environ['OS_PASSWORD'],
#                     project_domain_name=os.environ['OS_PROJECT_DOMAIN_NAME'],
#                     project_name=os.environ['OS_PROJECT_NAME'],
#                     auth_url=os.environ['OS_AUTH_URL']
#                          )
# sess=conn.session
# # print sess
# nova = nova_client.Client("2.1", session=sess)
# print nova.servers.list()
# print nova.flavors.list()




# from novaclient import client
# import os
# PROJECT_ID=os.environ['OS_PROJECT_NAME']
# AUTH_URL=os.environ['OS_AUTH_URL']
# print AUTH_URL
# nova = client.Client("2.1", "admin", "123456","admin", "http://192.168.146.146:35357/v3")
# print nova.servers.list()