#!/bin/env python

import boto3

ec2 = boto3.resource('ec2')


snapshot = ec2.Snapshot('snap-dc5ddb24')

print "data_encryption_key_id", snapshot.data_encryption_key_id
print "description", snapshot.description
print "encrypted", snapshot.encrypted
print "kms_key_id", snapshot.kms_key_id
print "owner_alias", snapshot.owner_alias
print "owner_id", snapshot.owner_id
print "progress", snapshot.progress
print "snapshot_id", snapshot.snapshot_id
print "start_time", snapshot.start_time
print "state", snapshot.state
print "state_message", snapshot.state_message
print "tags", snapshot.tags
print "volume_id", snapshot.volume_id
print "volume_size", snapshot.volume_size

