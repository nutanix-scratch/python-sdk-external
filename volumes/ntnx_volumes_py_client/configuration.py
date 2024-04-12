# coding: utf-8


"""
IGNORE:
    Nutanix Volumes Versioned APIs

    Configure volumes.  # noqa: E501

    OpenAPI spec version: 4.0.1-beta-1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
IGNORE
"""
from __future__ import absolute_import

import os
import copy
import logging
from logging.handlers import TimedRotatingFileHandler
import multiprocessing
import sys
import urllib3

import six
from six.moves import http_client as httplib


class TypeWithDefault(type):
    def __init__(cls, name, bases, dct):
        super(TypeWithDefault, cls).__init__(name, bases, dct)
        cls._default = None

    def __call__(cls):
        if cls._default is None:
            cls._default = type.__call__(cls)
        return copy.copy(cls._default)

    def set_default(cls, default):
        cls._default = copy.copy(default)


class Configuration(six.with_metaclass(TypeWithDefault, object)):
    """A class for the configuration of :class:`~ntnx_volumes_py_client.api_client.ApiClient`.

    This class contains certain configuration methods and data required by the api client.

    :param scheme: (:attr:`scheme`) URI scheme for connecting to the cluster (HTTP or HTTPS using SSL/TLS) (**Default** https)
    :type scheme: :class:`str`
    :param host: (:attr:`host`) A host name to connect which can be either IPv4, IPv6 or FQDN (**Default** localhost)
    :type host: :class:`str`, required
    :param port: (:attr:`port`) A port number to connect (**Default** 9440)
    :type port: :class:`int`
    :param username: (:attr:`username`) A username for HTTP basic authentication
    :type username: :class:`str`, required
    :param password: (:attr:`password`) A password for HTTP basic authentication
    :type password: :class:`str`, required
    :param debug: (:attr:`debug`) Runs the client in debug mode by enabling/disabling debug logging (**Default** False)
    :type debug: :class:`bool`
    :param verify_ssl: (:attr:`verify_ssl`) Verify SSL certificate of cluster the client will connect to (**Default** True)
    :type verify_ssl: :class:`bool`
    :param max_retry_attempts: (:attr:`max_retry_attempts`) Maximum retry attempts to be made in case of status codes [408, 503, 504] (**Default** 5)
    :type max_retry_attempts: :class:`int`
    :param backoff_factor: (:attr:`backoff_factor`) Backoff factor by which the retry request is delayed with specific number of seconds (**Default** 3).

        This is calculated by the following formula: ::

        {backoff_factor} * (2 * ({number of retries so far} - 1))
    :type backoff_factor: :class:`float`
    :param logger_file: (:attr:`logger_file`) File location to which logs are written to
    :type logger_file: :class:`str`
    :param connect_timeout: (:attr:`connect_timeout`) Connection timeout in milliseconds for all operations (**Default** 30000)
    :type connect_timeout: :class:`int`
    :param read_timeout: (:attr:`read_timeout`) Read timeout in milliseconds for all operations (**Default** 30000)
    :type read_timeout: :class:`int`
    :param download_directory: (:attr:`download_directory`) Directory location on local for files to download
    :type download_directory: :class:`str`
    :param download_chunk_size: (:attr:`download_chunk_size`) Chunk size in bytes for files to download (**Default** 8*1024 bytes)
    :type download_chunk_size: :class:`int`
    """  # noqa: E501

    def __init__(self):

        """Constructor"""
        self.__scheme = "https"

        # Default host name
        self.__host = "localhost"

        # Default port number
        self.__port = 9440

        # Maximum number of allowed retries for a HTTP call
        self.__max_retry_attempts = 5

        # Backoff factor by which the retry request is delayed with specific number of seconds.
        self.__backoff_factor = 3

        self.__user_agent = 'Nutanix-ntnx_volumes_py_client/4.0.1b1'

        # Directory path for downloading files
        self.__download_directory = os.path.abspath(os.getcwd())
        # Chunk size for downloading files
        self.__download_chunk_size = 8*1024

        # Authentication Settings
        # HTTP Basic Auth
        self.__username = None
        self.__password = None

        # API Key authentication (NOTE: SDK currently supports basic auth only)
        # Dictionary to store API key(s)
        self.api_key = {}
        # Dictionary to store API prefix (e.g. Bearer)
        self.api_key_prefix = {}

        # Logging Settings
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("ntnx_volumes_py_client")
        # Log format
        self.logger_format = '%(asctime)s %(levelname)s [%(threadName)s:%(name)s:%(lineno)d] %(message)s'
        # Log stream handler
        self.logger_stream_handler = None
        # Log file handler
        self.logger_file_handler = None
        # Debug file location
        self.logger_file = None

        # Debug switch
        self.__debug = False

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate received from the https server when calling API
        self.__verify_ssl = True

        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = None
        # client certificate file
        self.cert_file = None
        # client key file
        self.key_file = None
        # Set this to True/False to enable/disable SSL hostname verification.
        self.assert_hostname = None

        # urllib3 connection pool's maximum number of connections saved
        # per pool. urllib3 uses 1 connection as default value, but this is
        # not the best value when you are making a lot of possibly parallel
        # requests to the same host, which is often the case here.
        # cpu_count * 5 is used as default value to increase performance.
        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5

        # Proxy Parameters
        self.__proxy_scheme = None
        self.__proxy_host = None
        self.__proxy_port = None
        self.__proxy_username = None
        self.__proxy_password = None

        # Safe chars for path_param
        self.safe_chars_for_path_param = ''

        # Request timeout in milliseconds
        self.__default_connect_timeout = 30000
        self.__default_read_timeout = 30000
        self.__connect_timeout = None
        self.__read_timeout = None

    @property
    def scheme(self):
        """URI scheme for connecting to the cluster (HTTP or HTTPS using SSL/TLS) (**Default** https).

        :type: :class:`str`
        """
        return self.__scheme

    @scheme.setter
    def scheme(self, value):
        self.__scheme = value

    @property
    def host(self):
        """Host name to connect which can be either IPv4, IPv6 or FQDN (**Default** localhost).

        :type: :class:`str`
        """
        return self.__host

    @host.setter
    def host(self, value):
        self.__host = value

    @property
    def port(self):
        """Port number to connect (**Default** 9440).

        :type: :class:`int`
        """
        return self.__port

    @port.setter
    def port(self, value):
        self.__port = value

    @property
    def download_directory(self):
        """Directory path for downloading files (**Default** current directory).

        :type: :class:`str`
        """
        return self.__download_directory

    @download_directory.setter
    def download_directory(self, value):
        self.__download_directory = value

    @property
    def download_chunk_size(self):
        """Chunk size for downloading files (**Default** 8*1024 bytes).

        :type: :class:`int`
        """
        return self.__download_chunk_size

    @download_chunk_size.setter
    def download_chunk_size(self, value):
        self.__download_chunk_size = value

    @property
    def max_retry_attempts(self):
        """Maximum allowed retry attempts for a HTTP call in case of response status codes [408, 503, 504] (**Default** 5).

        :type: :class:`int`
        """
        return self.__max_retry_attempts

    @max_retry_attempts.setter
    def max_retry_attempts(self, value):
        self.__max_retry_attempts = value

    @property
    def backoff_factor(self):
        """Backoff factor by which the retry request is delayed with specific number of seconds (**Default** 3).

        This is calculated by the following formula: ::

            {backoff_factor} * (2 * ({number of retries so far} - 1))

        :type: :class:`float`
        """
        return self.__backoff_factor

    @backoff_factor.setter
    def backoff_factor(self, value):
        self.__backoff_factor = value

    @property
    def user_agent(self):
        """Value for User-Agent header.

        :type: :class:`str`
        """
        return self.__user_agent

    @property
    def username(self):
        """Username to connect to a cluster.

        :type: :class:`str`
        """
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        """Password to connect to a cluster.

        :type: :class:`str`
        """
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def verify_ssl(self):
        """A flag to enable/disable verification the SSL certificate of target cluster.

        :type: :class:`bool`
        """
        return self.__verify_ssl

    @verify_ssl.setter
    def verify_ssl(self, value):
        self.__verify_ssl = value

    @property
    def proxy_scheme(self):
        """Scheme for the proxy URI.

        :type: :class:`str`
        """
        return self.__proxy_scheme

    @proxy_scheme.setter
    def proxy_scheme(self, value):
        self.__proxy_scheme = value

    @property
    def proxy_host(self):
        """Host for the proxy URI.

        :type: :class:`str`
        """
        return self.__proxy_host

    @proxy_host.setter
    def proxy_host(self, value):
        self.__proxy_host = value

    @property
    def proxy_port(self):
        """Port number for the proxy URI.

        :type: :class:`int`
        """
        return self.__proxy_port

    @proxy_port.setter
    def proxy_port(self, value):
        self.__proxy_port = value

    @property
    def proxy_username(self):
        """Username for the proxy authentication.

        :type: :class:`str`
        """
        return self.__proxy_username

    @proxy_username.setter
    def proxy_username(self, value):
        self.__proxy_username = value

    @property
    def proxy_password(self):
        """Password for the proxy authentication.

        :type: :class:`str`
        """
        return self.__proxy_password

    @proxy_password.setter
    def proxy_password(self, value):
        self.__proxy_password = value

    @property
    def logger_file(self):
        """File location to which debug logs are written to.

        If the logger_file is None, then a  logger is configured with a console stream handler and all the file
        handlers are removed.
        Otherwise, a logger is configured with a file handler and stream handlers are removed.

        Configured file handlers are time based handlers which are rotated everyday at midnight.

        :type: :class:`str`
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.handlers.TimedRotatingFileHandler(self.__logger_file, 'midnight', 1)
            self.logger_file_handler.suffix = "%Y-%m-%d"
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)
                if self.logger_stream_handler:
                    logger.removeHandler(self.logger_stream_handler)
        else:
            # If not set logging file,
            # then add stream handler and remove file handler.
            self.logger_stream_handler = logging.StreamHandler()
            self.logger_stream_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_stream_handler)
                if self.logger_file_handler:
                    logger.removeHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Runs the client in debug mode by enabling/disabling debug logging (**Default** False).

        Default logging level is INFO and all associated loggers' levels are toggled between INFO and DEBUG by this flag.

        :type: :class:`bool`
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.INFO`
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.INFO)

    @property
    def logger_format(self):
        """The log format for file or stream log handler.

        :type: :class:`str`
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    @property
    def default_connect_timeout(self):
        """Default connection timeout in milliseconds for a HTTP request (**Default** 30000).

        :type: :class:`int`
        """

        return self.__default_connect_timeout

    @property
    def default_read_timeout(self):
        """Default read timeout in milliseconds for a HTTP request (**Default** 30000).

        :type: :class:`int`
        """

        return self.__default_read_timeout

    @property
    def connect_timeout(self):
        """Connect timeout for an operation in milliseconds.

        :type: :class:`int`
        """

        return self.__connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, value):
        self.__connect_timeout = value

    @property
    def read_timeout(self):
        """Read timeout for an operation in milliseconds.

        :type: :class:`int`
        """
        return self.__read_timeout

    @read_timeout.setter
    def read_timeout(self, value):
        self.__read_timeout = value

    def _get_api_key_with_prefix(self, identifier):
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey
        :type identifier: :class:`str`
        ...
        :return: A token for api key authentication
        :rtype: :class:`str`
        """
        if (self.api_key.get(identifier) and
                self.api_key_prefix.get(identifier)):
            return self.api_key_prefix[identifier] + ' ' + self.api_key[identifier]  # noqa: E501
        elif self.api_key.get(identifier):
            return self.api_key[identifier]

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: A token for basic HTTP authentication.
        :rtype: :class:`str`
        """
        if self.__username and self.__password:
            return urllib3.util.make_headers(
                basic_auth=self.__username + ':' + self.__password
            ).get('authorization')

    def _auth_settings(self):
        """Gets Auth Settings configuration.
        """
        return {
            'basicAuthScheme':
                {
                    'type': 'basic',
                    'in': 'header',
                    'key': 'Authorization',
                    'value': self.get_basic_auth_token()
                },
        }

    def to_debug_report(self):
        """Prints the information about current OS, Python, API and SDK versions for debugging purposes
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 4.0.1-beta-1\n"\
               "SDK Package Version: 4.0.1b1".\
               format(env=sys.platform, pyversion=sys.version)