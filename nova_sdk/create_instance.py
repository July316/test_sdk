from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client
import os
import time
    
auth = v3.Password(auth_url=os.environ['OS_AUTH_URL'],
                    username=os.environ['OS_USERNAME'],
                    password=os.environ['OS_PASSWORD'],
                   project_name=os.environ['OS_PROJECT_NAME'],
                   user_domain_name=os.environ['OS_USER_DOMAIN_NAME'],
                    project_domain_name=os.environ['OS_PROJECT_DOMAIN_NAME'])
sess = session.Session(auth=auth)
nova_client = client.Client("2.1", session=sess)
def print_server(server):
    print("-"*35)
    print("server id: %s" % server.id)
    print("server name: %s" % server.name)
    print("server image: %s" % server.image)
    print("server flavor: %s" % server.flavor)
    print("server key name: %s" % server.key_name)
    print("user_id: %s" % server.user_id)
    print("-"*35)
def list_detail():
    nova_host = nova_client.hosts.list()
    print("list all host:%s" % nova_host)
     
    print("================list servers=======================")
    nova_servers = nova_client.servers.list()
    print("list all instance:%s " % nova_servers)
    for server in nova_servers:
        print("instance name:%s || instance id:%s|| instance network:%s" % (server.name,server.id,server.networks))
         
    print("================list flavors=======================")
    nova_flavors = nova_client.flavors.list()
    print("list all flavor:%s" % nova_flavors)
#     print dir(nova_flavors[0])
    for flavor in nova_flavors:
        print("flavors name:%s || vcpus:%s || ram:%s || disk:%s" % (flavor.name,flavor.vcpus,flavor.ram,flavor.disk))
     
    print("================list networks=======================")
    nova_networks = nova_client.networks.list()
    print("list all network:%s" % nova_networks)
    for network in nova_networks:
        print("network name:%s || network id:%s" % (network.label,network.id))
     
    print("================list images=======================")
    nova_images = nova_client.images.list()
    print("list all image:%s" % nova_images)
#     print dir(nova_images[0])
    for image in nova_images:
        print("image name:%s || image id:%s" % (image.name,image.id))

#create server
def create_instance(image_name,flavors_name,networks_label,ins_name):
    try:
        image = nova_client.images.find(name=image_name)
        flavor = nova_client.flavors.find(name=flavors_name)
#         network = nova_client.networks.list()
        net = nova_client.networks.find(label=networks_label)
        nics = [{'net-id': net.id}]
        instance = nova_client.servers.create(name=ins_name,image=image,flavor=flavor,nics=nics)
        print("Sleeping for 5s after create command")
        time.sleep(5)
        print("List of VMs")
        print(nova_client.servers.list())
    finally:
        print("Execution Completed")

#update server
def update_instance(ins_name):
    server_detail = nova_client.servers.find(name=ins_name)
    server_id = server_detail.id    
#     server = nova_client.servers.get(server_id)
#     n = server.name
    print_server(server_detail)   
    server_detail.update(name=ins_name +'1')
    server_updated = nova_client.servers.get(server_id)
    print_server(server_updated)


#start server
def start_server(ins_name):
    print("=======================start server====================")
    server_detail = nova_client.servers.find(name=ins_name)
    print ("the instace start before status:%s" % server_detail.status)
    if  server_detail.status != "ACTIVE":
        server_detail.start()
    print ("the starting %s instance" % server_detail.name)
    print ("...........................")
    time.sleep(15)
    if server_detail.status == "ACTIVE":
        print ("the instace start status:%s" % server_detail.status)  
        
#reboot server


#stop server
def stop_server(ins_name):
    server_detail = nova_client.servers.find(name=ins_name)
    server_id = server_detail.id
    server_detail.stop()
    print server_detail.status 

#delete server
def del_server(server_del):
    servers_list = nova_client.servers.list()
    server_exists = False
      
    for s in servers_list:
        if s.name == server_del:
            print("This server %s exists" % server_del)
            server_exists = True
            break
    if not server_exists:
        print("server %s does not exist" % server_del)
    else:
        print("deleting server..........")
        nova_client.servers.delete(s)
        print("server %s deleted" % server_del)
if __name__ == "__main__":
#     pass
#     list_detail()
#     create_instance(image_name="cirros",flavors_name="m1.tiny",networks_label="selfservice",ins_name="test12911111")
#     update_instance("test1291")
#     start_server("test12911111")
    stop_server("test12911111")
#     start_server(ins_name)
#     del_server("test211")

