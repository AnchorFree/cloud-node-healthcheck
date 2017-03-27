import argparser
import digitalocean
import prometheus_client


def prometheus_missing_nodes():
    """
    function to query prometheus to find dead nodes
    inital criteria:
    all the machines which have ever submitted data with all the machines which have submitted data in the last hour

    :return: a list of nodes we have not heard from in a while.
    """

    return []


def digitalocean_restart_nodes(nodes_to_restart):
    """
    Given a list of nodes, connect to the DO API and restart them.

    :param nodes_to_restart: a list of digital ocean nodes which should be restarted
    :return: None
    """

    nodes_to_restart = nodes_to_restart or []

    # connect to DO API

    # restart dead nodes
    for node_to_restart in nodes_to_restart:
        pass

    return None


def taint_with_terraform(nodes_to_taint):
    """
    :param nodes_to_taint: a list of nodes which should be tainted in terraform
    :return: None
    """

    for node_to_taint in nodes_to_taint:
        pass

    return None


def main():
    # parse arguments

    # gather credentials for prometheus / do access

    missing_nodes = prometheus_missing_nodes()
    # maybe log the output?

    digitalocean_restart_nodes(missing_nodes)

    # sleep?

    still_missing_nodes = prometheus_missing_nodes()

    taint_with_terraform(still_missing_nodes)


if '__main__' == __name__:
    main()
