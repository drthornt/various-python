#!/bin/env python

import boto3

print "Creating boto resour"
resource = boto3.resource('ec2')

print "resource is of type %s" % type(resource)
# resource is of type <class 'boto3.resources.factory.ec2.ServiceResource'>

print "creating client"
client = boto3.client('ec2')
account = boto3.client('sts').get_caller_identity().get('Account')

print "client is of type %s " % type (client)
# client is of type <class 'botocore.client.EC2'>

print "creating reseverations"

reservations = client.describe_instances(
    Filters=[
        {'Name': 'tag-key', 'Values': ['snapshot_schedule']},
    ]
    ).get(
        'Reservations', []
    )

print "created reservations"
print "reservations is of type %s" % type(reservations)
# reservations is of type list

instances = sum(
    [
        [i for i in r['Instances']]
        for r in reservations
    ], [])

print "instances is of type %s " % type ( instances)
# instances is of type <type 'list'>

print "Found %d instances that need backing up" % len(instances)

for instance in instances:
    print "instance is of type %s" % type(instance)
    # instance is of type <type 'dict'>
    print "Tags is of type %s " % type(instance['Tags'])
    # Tags is of type <type 'list'>
    for tag in instance['Tags']:
        print "tag is of type %s" % type(tag)
        # tag is of type <type 'dict'>
        print "Key: %s , Value: %s" % ( tag['Key'] , tag['Value'] )
    for dev in instance['BlockDeviceMappings']:
        if dev.get('Ebs', None) is None:
            # skip non-EBS volumes
            print "Skipped non ebs volume"
            continue
        vol_id = dev['Ebs']['VolumeId']
        print "Found EBS volume %s on instance %s" % ( vol_id, instance['InstanceId'])

        filter = [{'Name':'volume-id', 'Values':[vol_id]}]
        snaps = client.describe_snapshots(OwnerIds=[account,],MaxResults=10,Filters=filter)
        # snaps = client.describe_snapshots(OwnerIds=[account,],MaxResults=10)
        print "Snaps is of type %s" % type(snaps)
        for snapshot in snaps['Snapshots']:
            print snapshot['SnapshotId']
            print snapshot

