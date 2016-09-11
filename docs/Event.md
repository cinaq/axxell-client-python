# Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time** | **str** | Read-only | [optional] 
**event_type** | **str** | Type of event, consumer cannot set recommend | [optional] 
**event_id** | **str** | Read-only | [optional] 
**event_time** | **str** | Read-only | [optional] 
**entity_type** | **str** | Read-only | [optional] 
**entity_id** | **str** | The user that triggered this event. You are free to choose whatever you like but it has to be consistent. Good examples are email address, internal user id or sha256 hash of these values. | [optional] 
**target_entity_type** | **str** | Read-only | [optional] 
**target_entity_id** | **str** | Way to identify your product. Use the product id from your shop | [optional] 
**body** | **str** | Meta information that doesn&#39;t fit into above fields. Read-only | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


