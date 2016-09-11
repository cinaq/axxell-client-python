# AxxellClient.DefaultApi

All URIs are relative to *https://axxell.cinaq.com/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_count_events**](DefaultApi.md#aggregate_count_events) | **GET** /aggregates/countevents/{eventType} | 
[**aggregate_effective**](DefaultApi.md#aggregate_effective) | **GET** /aggregates/effective/{eventType} | 
[**aggregate_events**](DefaultApi.md#aggregate_events) | **GET** /aggregates/events/{eventType} | 
[**aggregate_recent**](DefaultApi.md#aggregate_recent) | **GET** /aggregates/recent/{eventType} | 
[**aggregate_top**](DefaultApi.md#aggregate_top) | **GET** /aggregates/top/{eventType} | 
[**auth_store**](DefaultApi.md#auth_store) | **POST** /auth | 
[**delete_all_events**](DefaultApi.md#delete_all_events) | **DELETE** /events | 
[**delete_all_items**](DefaultApi.md#delete_all_items) | **DELETE** /items | 
[**delete_item**](DefaultApi.md#delete_item) | **DELETE** /items/{itemid} | 
[**recommend_interesting**](DefaultApi.md#recommend_interesting) | **GET** /recommendations/interesting | 
[**recommend_similar**](DefaultApi.md#recommend_similar) | **GET** /recommendations/similar | 
[**register_event**](DefaultApi.md#register_event) | **POST** /events | 
[**register_item**](DefaultApi.md#register_item) | **POST** /items | 
[**register_store**](DefaultApi.md#register_store) | **POST** /store | 
[**retrieve_events**](DefaultApi.md#retrieve_events) | **GET** /events | 
[**retrieve_items**](DefaultApi.md#retrieve_items) | **GET** /items | 


# **aggregate_count_events**
> DataPoint aggregate_count_events(storeid, event_type, data_period)



Return list of counts per event

### Example 
```python
from __future__ import print_statement
import time
import AxxellClient
from AxxellClient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
AxxellClient.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# AxxellClient.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = AxxellClient.DefaultApi()
storeid = 'storeid_example' # str | Store identifier
event_type = 'event_type_example' # str | Valid values purchase, view or recommend
data_period = 'data_period_example' # str | Valid values are last7days, last30days, today, yesterday

try: 
    api_response = api_instance.aggregate_count_events(storeid, event_type, data_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->aggregate_count_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeid** | **str**| Store identifier | 
 **event_type** | **str**| Valid values purchase, view or recommend | 
 **data_period** | **str**| Valid values are last7days, last30days, today, yesterday | 

### Return type

[**DataPoint**](DataPoint.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregate_effective**
> list[DataPoint] aggregate_effective(storeid, event_type)



Return list of aggregated data points correlated with recommendationa and eventType

### Example 
```python
from __future__ import print_statement
import time
import AxxellClient
from AxxellClient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
AxxellClient.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# AxxellClient.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = AxxellClient.DefaultApi()
storeid = 'storeid_example' # str | Store identifier
event_type = 'event_type_example' # str | Valid values purchase, view or recommend

try: 
    api_response = api_instance.aggregate_effective(storeid, event_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->aggregate_effective: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeid** | **str**| Store identifier | 
 **event_type** | **str**| Valid values purchase, view or recommend | 

### Return type

[**list[DataPoint]**](DataPoint.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregate_events**
> list[DataPoint] aggregate_events(storeid, event_type)



Return list of aggregated data points

### Example 
```python
from __future__ import print_statement
import time
import AxxellClient
from AxxellClient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
AxxellClient.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# AxxellClient.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = AxxellClient.DefaultApi()
storeid = 'storeid_example' # str | Store identifier
event_type = 'event_type_example' # str | Valid values purchase, view or recommend

try: 
    api_response = api_instance.aggregate_events(storeid, event_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->aggregate_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeid** | **str**| Store identifier | 
 **event_type** | **str**| Valid values purchase, view or recommend | 

### Return type

[**list[DataPoint]**](DataPoint.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregate_recent**
> list[Item] aggregate_recent(storeid, event_type)



Returns recent products

### Example 
```python
from __future__ import print_statement
import time
import AxxellClient
from AxxellClient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
AxxellClient.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# AxxellClient.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = AxxellClient.DefaultApi()
storeid = 'storeid_example' # str | Store identifier
event_type = 'event_type_example' # str | Valid values purchase, view or recommend

try: 
    api_response = api_instance.aggregate_recent(storeid, event_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->aggregate_recent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeid** | **str**| Store identifier | 
 **event_type** | **str**| Valid values purchase, view or recommend | 

### Return type

[**list[Item]**](Item.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **aggregate_top**
> list[Item] aggregate_top(storeid, event_type)



Returns top products

### Example 
```python
from __future__ import print_statement
import time
import AxxellClient
from AxxellClient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
AxxellClient.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# AxxellClient.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = AxxellClient.DefaultApi()
storeid = 'storeid_example' # str | Store identifier
event_type = 'event_type_example' # str | Valid values purchase, view or recommend

try: 
    api_response = api_instance.aggregate_top(storeid, event_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->aggregate_top: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeid** | **str**| Store identifier | 
 **event_type** | **str**| Valid values purchase, view or recommend | 

### Return type

[**list[Item]**](Item.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_store**
> Store auth_store(store)



Retrieve authentication token using password

### Example 
```python
from __future__ import print_statement
import time
import AxxellClient
from AxxellClient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
AxxellClient.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# AxxellClient.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = AxxellClient.DefaultApi()
store = AxxellClient.Store() # Store | Store

try: 
    api_response = api_instance.auth_store(store)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->auth_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store** | [**Store**](Store.md)| Store | 

### Return type

[**Store**](Store.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_events**
> Event delete_all_events(storeid)



Delete all events

### Example 
```python
from __future__ import print_statement
import time
import AxxellClient
from AxxellClient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
AxxellClient.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# AxxellClient.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = AxxellClient.DefaultApi()
storeid = 'storeid_example' # str | Store identifier

try: 
    api_response = api_instance.delete_all_events(storeid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_all_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeid** | **str**| Store identifier | 

### Return type

[**Event**](Event.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_items**
> Item delete_all_items(storeid)



Delete all items

### Example 
```python
from __future__ import print_statement
import time
import AxxellClient
from AxxellClient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
AxxellClient.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# AxxellClient.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = AxxellClient.DefaultApi()
storeid = 'storeid_example' # str | Store identifier

try: 
    api_response = api_instance.delete_all_items(storeid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_all_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeid** | **str**| Store identifier | 

### Return type

[**Item**](Item.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_item**
> Item delete_item(storeid, itemid)



Delete existing item

### Example 
```python
from __future__ import print_statement
import time
import AxxellClient
from AxxellClient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
AxxellClient.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# AxxellClient.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = AxxellClient.DefaultApi()
storeid = 'storeid_example' # str | Store identifier
itemid = 'itemid_example' # str | Item identifier

try: 
    api_response = api_instance.delete_item(storeid, itemid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeid** | **str**| Store identifier | 
 **itemid** | **str**| Item identifier | 

### Return type

[**Item**](Item.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommend_interesting**
> list[Item] recommend_interesting(storeid, userid, count=count)



Return list of recommended items

### Example 
```python
from __future__ import print_statement
import time
import AxxellClient
from AxxellClient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
AxxellClient.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# AxxellClient.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = AxxellClient.DefaultApi()
storeid = 'storeid_example' # str | Store identifier
userid = 'userid_example' # str | Interesting items for visitor
count = 1.2 # float | Return exactly this amount of suggestions. Maximum value is 50, default is 5. (optional)

try: 
    api_response = api_instance.recommend_interesting(storeid, userid, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->recommend_interesting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeid** | **str**| Store identifier | 
 **userid** | **str**| Interesting items for visitor | 
 **count** | **float**| Return exactly this amount of suggestions. Maximum value is 50, default is 5. | [optional] 

### Return type

[**list[Item]**](Item.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommend_similar**
> list[Item] recommend_similar(storeid, userid, itemid, count=count)



Return list of recommended items

### Example 
```python
from __future__ import print_statement
import time
import AxxellClient
from AxxellClient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
AxxellClient.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# AxxellClient.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = AxxellClient.DefaultApi()
storeid = 'storeid_example' # str | Store identifier
userid = 'userid_example' # str | User requesting the recommendation
itemid = 'itemid_example' # str | Similar items bought by others
count = 1.2 # float | Return exactly this amount of suggestions. Maximum value is 50, default is 5. (optional)

try: 
    api_response = api_instance.recommend_similar(storeid, userid, itemid, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->recommend_similar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeid** | **str**| Store identifier | 
 **userid** | **str**| User requesting the recommendation | 
 **itemid** | **str**| Similar items bought by others | 
 **count** | **float**| Return exactly this amount of suggestions. Maximum value is 50, default is 5. | [optional] 

### Return type

[**list[Item]**](Item.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_event**
> Event register_event(storeid, event)



Register new event

### Example 
```python
from __future__ import print_statement
import time
import AxxellClient
from AxxellClient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
AxxellClient.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# AxxellClient.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = AxxellClient.DefaultApi()
storeid = 'storeid_example' # str | Store identifier
event = AxxellClient.Event() # Event | Single event to register

try: 
    api_response = api_instance.register_event(storeid, event)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->register_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeid** | **str**| Store identifier | 
 **event** | [**Event**](Event.md)| Single event to register | 

### Return type

[**Event**](Event.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_item**
> Item register_item(storeid, item)



Register new item

### Example 
```python
from __future__ import print_statement
import time
import AxxellClient
from AxxellClient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
AxxellClient.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# AxxellClient.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = AxxellClient.DefaultApi()
storeid = 'storeid_example' # str | Store identifier
item = AxxellClient.Item() # Item | Single item to register

try: 
    api_response = api_instance.register_item(storeid, item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->register_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeid** | **str**| Store identifier | 
 **item** | [**Item**](Item.md)| Single item to register | 

### Return type

[**Item**](Item.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_store**
> Store register_store(store)



Register new Store

### Example 
```python
from __future__ import print_statement
import time
import AxxellClient
from AxxellClient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
AxxellClient.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# AxxellClient.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = AxxellClient.DefaultApi()
store = AxxellClient.Store() # Store | Store

try: 
    api_response = api_instance.register_store(store)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->register_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store** | [**Store**](Store.md)| Store | 

### Return type

[**Store**](Store.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_events**
> list[Event] retrieve_events(storeid)



Get recent events

### Example 
```python
from __future__ import print_statement
import time
import AxxellClient
from AxxellClient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
AxxellClient.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# AxxellClient.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = AxxellClient.DefaultApi()
storeid = 'storeid_example' # str | Store identifier

try: 
    api_response = api_instance.retrieve_events(storeid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeid** | **str**| Store identifier | 

### Return type

[**list[Event]**](Event.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_items**
> list[Item] retrieve_items(storeid)



Get recent items

### Example 
```python
from __future__ import print_statement
import time
import AxxellClient
from AxxellClient.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
AxxellClient.configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# AxxellClient.configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = AxxellClient.DefaultApi()
storeid = 'storeid_example' # str | Store identifier

try: 
    api_response = api_instance.retrieve_items(storeid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->retrieve_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storeid** | **str**| Store identifier | 

### Return type

[**list[Item]**](Item.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

