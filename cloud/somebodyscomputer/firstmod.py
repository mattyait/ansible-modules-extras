#!/usr/bin/python
# Make coding more python3-ish
from __future__ import (absolute_import, division)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule


def fetch(url):
    raise NotImplementedError


def write(data, dest):
    raise NotImplementedError


def save_data(mod):
    data = fetch(mod.params["url"])

    if write(data, mod.params["dest"]):
        mod.exit_json(msg="Data saved", changed=True)


def main():
    mod = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True),
            dest=dict(required=False, default="/tmp/firstmod")
        )
    )

    save_data(mod)


if __name__ == '__main__':
    main()
