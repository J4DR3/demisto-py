# coding: utf-8

"""
    Demisto API

    This is the public REST API to integrate with the demisto server. HTTP request can be sent using any HTTP-client.  For an example dedicated client take a look at: https://github.com/demisto/demisto-py.  Requests must include API-key that can be generated in the Demisto web client under 'Settings' -> 'Integrations' -> 'API keys'   Optimistic Locking and Versioning\\:  When using Demisto REST API, you will need to make sure to work on the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you to override a newer item). In addition, you can pass 'version\\: -1' to force data override (make sure that other users data might be lost).  Assume that Alice and Bob both read the same data from Demisto server, then they both changed the data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s? To solve this, each data item in Demisto has a numeric incremental version. If Alice saved an item with version 4 and Bob trying to save the same item with version 3, Demisto will rollback Bob request and returns a DB version conflict error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using 'curl'\\:  ``` curl 'https://hostname:443/incidents/search' -H 'content-type: application/json' -H 'accept: application/json' -H 'Authorization: <API Key goes here>' --data-binary '{\"filter\":{\"query\":\"-status:closed -category:job\",\"period\":{\"by\":\"day\",\"fromValue\":7}}}' --compressed ```  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from demisto_client.demisto_api.models.period import Period  # noqa: F401,E501
from demisto_client.demisto_api.models.widget_cells import WidgetCells  # noqa: F401,E501


class Dashboard(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'commit_message': 'str',
        'from_date': 'datetime',
        'from_date_license': 'datetime',
        'id': 'str',
        'is_common': 'bool',
        'layout': 'WidgetCells',
        'modified': 'datetime',
        'name': 'str',
        'owner': 'str',
        'period': 'Period',
        'prev_name': 'str',
        'shared': 'bool',
        'should_commit': 'bool',
        'sort_values': 'list[str]',
        'system': 'bool',
        'to_date': 'datetime',
        'vc_should_ignore': 'bool',
        'version': 'int'
    }

    attribute_map = {
        'commit_message': 'commitMessage',
        'from_date': 'fromDate',
        'from_date_license': 'fromDateLicense',
        'id': 'id',
        'is_common': 'isCommon',
        'layout': 'layout',
        'modified': 'modified',
        'name': 'name',
        'owner': 'owner',
        'period': 'period',
        'prev_name': 'prevName',
        'shared': 'shared',
        'should_commit': 'shouldCommit',
        'sort_values': 'sortValues',
        'system': 'system',
        'to_date': 'toDate',
        'vc_should_ignore': 'vcShouldIgnore',
        'version': 'version'
    }

    def __init__(self, commit_message=None, from_date=None, from_date_license=None, id=None, is_common=None, layout=None, modified=None, name=None, owner=None, period=None, prev_name=None, shared=None, should_commit=None, sort_values=None, system=None, to_date=None, vc_should_ignore=None, version=None):  # noqa: E501
        """Dashboard - a model defined in Swagger"""  # noqa: E501

        self._commit_message = None
        self._from_date = None
        self._from_date_license = None
        self._id = None
        self._is_common = None
        self._layout = None
        self._modified = None
        self._name = None
        self._owner = None
        self._period = None
        self._prev_name = None
        self._shared = None
        self._should_commit = None
        self._sort_values = None
        self._system = None
        self._to_date = None
        self._vc_should_ignore = None
        self._version = None
        self.discriminator = None

        if commit_message is not None:
            self.commit_message = commit_message
        if from_date is not None:
            self.from_date = from_date
        if from_date_license is not None:
            self.from_date_license = from_date_license
        if id is not None:
            self.id = id
        if is_common is not None:
            self.is_common = is_common
        if layout is not None:
            self.layout = layout
        if modified is not None:
            self.modified = modified
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if period is not None:
            self.period = period
        if prev_name is not None:
            self.prev_name = prev_name
        if shared is not None:
            self.shared = shared
        if should_commit is not None:
            self.should_commit = should_commit
        if sort_values is not None:
            self.sort_values = sort_values
        if system is not None:
            self.system = system
        if to_date is not None:
            self.to_date = to_date
        if vc_should_ignore is not None:
            self.vc_should_ignore = vc_should_ignore
        if version is not None:
            self.version = version

    @property
    def commit_message(self):
        """Gets the commit_message of this Dashboard.  # noqa: E501


        :return: The commit_message of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        """Sets the commit_message of this Dashboard.


        :param commit_message: The commit_message of this Dashboard.  # noqa: E501
        :type: str
        """

        self._commit_message = commit_message

    @property
    def from_date(self):
        """Gets the from_date of this Dashboard.  # noqa: E501


        :return: The from_date of this Dashboard.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this Dashboard.


        :param from_date: The from_date of this Dashboard.  # noqa: E501
        :type: datetime
        """

        self._from_date = from_date

    @property
    def from_date_license(self):
        """Gets the from_date_license of this Dashboard.  # noqa: E501


        :return: The from_date_license of this Dashboard.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date_license

    @from_date_license.setter
    def from_date_license(self, from_date_license):
        """Sets the from_date_license of this Dashboard.


        :param from_date_license: The from_date_license of this Dashboard.  # noqa: E501
        :type: datetime
        """

        self._from_date_license = from_date_license

    @property
    def id(self):
        """Gets the id of this Dashboard.  # noqa: E501


        :return: The id of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Dashboard.


        :param id: The id of this Dashboard.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_common(self):
        """Gets the is_common of this Dashboard.  # noqa: E501


        :return: The is_common of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._is_common

    @is_common.setter
    def is_common(self, is_common):
        """Sets the is_common of this Dashboard.


        :param is_common: The is_common of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._is_common = is_common

    @property
    def layout(self):
        """Gets the layout of this Dashboard.  # noqa: E501


        :return: The layout of this Dashboard.  # noqa: E501
        :rtype: WidgetCells
        """
        return self._layout

    @layout.setter
    def layout(self, layout):
        """Sets the layout of this Dashboard.


        :param layout: The layout of this Dashboard.  # noqa: E501
        :type: WidgetCells
        """

        self._layout = layout

    @property
    def modified(self):
        """Gets the modified of this Dashboard.  # noqa: E501


        :return: The modified of this Dashboard.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Dashboard.


        :param modified: The modified of this Dashboard.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this Dashboard.  # noqa: E501


        :return: The name of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Dashboard.


        :param name: The name of this Dashboard.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this Dashboard.  # noqa: E501


        :return: The owner of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Dashboard.


        :param owner: The owner of this Dashboard.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def period(self):
        """Gets the period of this Dashboard.  # noqa: E501


        :return: The period of this Dashboard.  # noqa: E501
        :rtype: Period
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Dashboard.


        :param period: The period of this Dashboard.  # noqa: E501
        :type: Period
        """

        self._period = period

    @property
    def prev_name(self):
        """Gets the prev_name of this Dashboard.  # noqa: E501


        :return: The prev_name of this Dashboard.  # noqa: E501
        :rtype: str
        """
        return self._prev_name

    @prev_name.setter
    def prev_name(self, prev_name):
        """Sets the prev_name of this Dashboard.


        :param prev_name: The prev_name of this Dashboard.  # noqa: E501
        :type: str
        """

        self._prev_name = prev_name

    @property
    def shared(self):
        """Gets the shared of this Dashboard.  # noqa: E501


        :return: The shared of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this Dashboard.


        :param shared: The shared of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._shared = shared

    @property
    def should_commit(self):
        """Gets the should_commit of this Dashboard.  # noqa: E501


        :return: The should_commit of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._should_commit

    @should_commit.setter
    def should_commit(self, should_commit):
        """Sets the should_commit of this Dashboard.


        :param should_commit: The should_commit of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._should_commit = should_commit

    @property
    def sort_values(self):
        """Gets the sort_values of this Dashboard.  # noqa: E501


        :return: The sort_values of this Dashboard.  # noqa: E501
        :rtype: list[str]
        """
        return self._sort_values

    @sort_values.setter
    def sort_values(self, sort_values):
        """Sets the sort_values of this Dashboard.


        :param sort_values: The sort_values of this Dashboard.  # noqa: E501
        :type: list[str]
        """

        self._sort_values = sort_values

    @property
    def system(self):
        """Gets the system of this Dashboard.  # noqa: E501


        :return: The system of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this Dashboard.


        :param system: The system of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def to_date(self):
        """Gets the to_date of this Dashboard.  # noqa: E501


        :return: The to_date of this Dashboard.  # noqa: E501
        :rtype: datetime
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this Dashboard.


        :param to_date: The to_date of this Dashboard.  # noqa: E501
        :type: datetime
        """

        self._to_date = to_date

    @property
    def vc_should_ignore(self):
        """Gets the vc_should_ignore of this Dashboard.  # noqa: E501


        :return: The vc_should_ignore of this Dashboard.  # noqa: E501
        :rtype: bool
        """
        return self._vc_should_ignore

    @vc_should_ignore.setter
    def vc_should_ignore(self, vc_should_ignore):
        """Sets the vc_should_ignore of this Dashboard.


        :param vc_should_ignore: The vc_should_ignore of this Dashboard.  # noqa: E501
        :type: bool
        """

        self._vc_should_ignore = vc_should_ignore

    @property
    def version(self):
        """Gets the version of this Dashboard.  # noqa: E501


        :return: The version of this Dashboard.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Dashboard.


        :param version: The version of this Dashboard.  # noqa: E501
        :type: int
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Dashboard, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Dashboard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
