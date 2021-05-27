import paramiko
import logging


def try_ssh_connect():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('ssh_test_app')
    logging.getLogger("paramiko").setLevel(logging.DEBUG)

    host = '100.68.183.144'
    password = 'calvin'
    username = 'root'
    port = 22

    client = paramiko.SSHClient()

    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    retval = 0

    cmd = 'racadm getsysinfo'
    try:
        client.connect(host, port=port, username=username, password=password, allow_agent=False, look_for_keys=False)
        transport = client.get_transport()

        if not transport.is_authenticated():
            transport.auth_interactive_dumb(username)

        if transport.is_authenticated():
            logger.info('transport is authenticated')
            _stdin, stdout, stderr = client.exec_command(cmd)
            res = stdout.read()
            logger.info('Command {0}:\n{1}'.format(cmd, res))
        else:
            logger.error('transport is not authenticated')

    except paramiko.AuthenticationException:
        logger.error('paramiko.AuthenticationException')
        retval = 1

    except paramiko.BadHostKeyException:
        logger.error('paramiko.BadHostKeyException')
        retval = 1

    except paramiko.SSHException:
        logger.error('paramiko.SSHException')
        retval = 1

    finally:
        transport.close()

    logger.info('Exiting at end of script: exit code {0}'.format(retval))

    exit(retval)


if "__main__" in __name__:
    try_ssh_connect()
    print("Done")