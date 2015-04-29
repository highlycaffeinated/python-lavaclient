import logging
import six
from figgis import Config, ListField

from lavaclient2.api import resource
from lavaclient2 import constants
from lavaclient2.api.response import Node
from lavaclient2.util import command, display_table, CommandLine

LOG = logging.getLogger(constants.LOGGER_NAME)


######################################################################
# API Responses
######################################################################

class NodesResponse(Config):

    """Response from /clusters/<cluster_id>/nodes"""

    nodes = ListField(Node, required=True)


######################################################################
# API Resource
######################################################################

@six.add_metaclass(CommandLine)
class Resource(resource.Resource):

    """Nodes API methods"""
    @command
    @display_table(Node)
    def list(self, cluster_id):
        """
        List clusters that belong to the tenant specified in the client

        :returns: List of Node objects
        """
        return self._parse_response(
            self._client._get('clusters/{0}/nodes'.format(cluster_id)),
            NodesResponse,
            wrapper='nodes')