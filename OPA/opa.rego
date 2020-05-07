package example.rules

#import input.container_id
#import input.installation_date
#import input.build_hosts
#import input.signature_key_IDs

#import data
#import input


default allow = "no data"

allow = data.container[i].container_passphrase {
        some i
        data.container[i].container_name == input.container_name
        data.container[i].container_hashvalue == input.container_hashvalue
}


