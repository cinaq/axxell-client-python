# coding: utf-8

"""
    axxell-api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Item(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, creation_time=None, item_id=None, gid=None, title=None, label=None, categories=None, url=None):
        """
        Item - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'creation_time': 'str',
            'item_id': 'str',
            'gid': 'str',
            'title': 'str',
            'label': 'str',
            'categories': 'list[str]',
            'url': 'str'
        }

        self.attribute_map = {
            'creation_time': 'creationTime',
            'item_id': 'itemId',
            'gid': 'gid',
            'title': 'title',
            'label': 'label',
            'categories': 'categories',
            'url': 'url'
        }

        self._creation_time = creation_time
        self._item_id = item_id
        self._gid = gid
        self._title = title
        self._label = label
        self._categories = categories
        self._url = url


    @property
    def creation_time(self):
        """
        Gets the creation_time of this Item.
        Read-only

        :return: The creation_time of this Item.
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this Item.
        Read-only

        :param creation_time: The creation_time of this Item.
        :type: str
        """

        self._creation_time = creation_time

    @property
    def item_id(self):
        """
        Gets the item_id of this Item.
        This must be your product id used by your own store

        :return: The item_id of this Item.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """
        Sets the item_id of this Item.
        This must be your product id used by your own store

        :param item_id: The item_id of this Item.
        :type: str
        """

        self._item_id = item_id

    @property
    def gid(self):
        """
        Gets the gid of this Item.
        Global identifier of this item/product. Read-only

        :return: The gid of this Item.
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """
        Sets the gid of this Item.
        Global identifier of this item/product. Read-only

        :param gid: The gid of this Item.
        :type: str
        """

        self._gid = gid

    @property
    def title(self):
        """
        Gets the title of this Item.
        Human readable title of the item/product

        :return: The title of this Item.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Item.
        Human readable title of the item/product

        :param title: The title of this Item.
        :type: str
        """

        self._title = title

    @property
    def label(self):
        """
        Gets the label of this Item.
        Sanitized version of title. Read-only

        :return: The label of this Item.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this Item.
        Sanitized version of title. Read-only

        :param label: The label of this Item.
        :type: str
        """

        self._label = label

    @property
    def categories(self):
        """
        Gets the categories of this Item.
        Categories this item belongs to. List of keywords describing the item is also acceptable here.

        :return: The categories of this Item.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this Item.
        Categories this item belongs to. List of keywords describing the item is also acceptable here.

        :param categories: The categories of this Item.
        :type: list[str]
        """

        self._categories = categories

    @property
    def url(self):
        """
        Gets the url of this Item.
        Full URL that links to the product. e.g. http://yourshop.com/product/123

        :return: The url of this Item.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Item.
        Full URL that links to the product. e.g. http://yourshop.com/product/123

        :param url: The url of this Item.
        :type: str
        """

        self._url = url

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
