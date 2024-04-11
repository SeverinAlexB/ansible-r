from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

# Custom become command

DOCUMENTATION = """
    name: rootsu
    short_description: Substitute User via root
    description:
        - Like normal su but the user is first switched to root and then to the actual user
    author: Severin Alex Bühler @ Redan.ch
    version_added: "0.1"
    options:
        become_user:
            description: User you 'become' to execute the task
            default: root
            ini:
              - section: privilege_escalation
                key: become_user
              - section: su_become_plugin
                key: user
            vars:
              - name: ansible_become_user
              - name: ansible_su_user
            env:
              - name: ANSIBLE_BECOME_USER
              - name: ANSIBLE_SU_USER
            keyword:
              - name: become_user
        become_exe:
            description: Su executable
            default: su
            ini:
              - section: privilege_escalation
                key: become_exe
              - section: su_become_plugin
                key: executable
            vars:
              - name: ansible_become_exe
              - name: ansible_su_exe
            env:
              - name: ANSIBLE_BECOME_EXE
              - name: ANSIBLE_SU_EXE
            keyword:
              - name: become_exe
        become_flags:
            description: Options to pass to su
            default: ''
            ini:
              - section: privilege_escalation
                key: become_flags
              - section: su_become_plugin
                key: flags
            vars:
              - name: ansible_become_flags
              - name: ansible_su_flags
            env:
              - name: ANSIBLE_BECOME_FLAGS
              - name: ANSIBLE_SU_FLAGS
            keyword:
              - name: become_flags
        become_pass:
            description: Password to pass to su
            required: False
            vars:
              - name: ansible_become_password
              - name: ansible_become_pass
              - name: ansible_su_pass
            env:
              - name: ANSIBLE_BECOME_PASS
              - name: ANSIBLE_SU_PASS
            ini:
              - section: su_become_plugin
                key: password
"""

import re
import shlex

from ansible.module_utils._text import to_bytes
from ansible.plugins.become import BecomeBase

class BecomeModule(BecomeBase):
    name = 'rootsu'

    # messages for detecting prompted password issues
    fail = ('Authentication failure',)

    def build_become_command(self, cmd, shell):
        super(BecomeModule, self).build_become_command(cmd, shell)

        if not cmd:
            return cmd

        becomecmd = 'sudo su -c'

        flags = self.get_option('become_flags') or ''

        # Prompt is not supported here.
        # prompt = ''
        # if self.get_option('become_pass'):
        #     self.prompt = '[sudo via ansible, key=%s] password:' % self._id
        #     if flags:  # this could be simplified, but kept as is for now for backwards string matching
        #         reflag = []
        #         for flag in shlex.split(flags):
        #             if flag in ('-n', '--non-interactive'):
        #                 continue
        #             elif not flag.startswith('--'):
        #                 # handle -XnxxX flags only
        #                 flag = re.sub(r'^(-\w*)n(\w*.*)', r'\1\2', flag)
        #             reflag.append(flag)
        #         flags = shlex.join(reflag)

        #     prompt = '-p "%s"' % (self.prompt)

        user = self.get_option('become_user') or ''

        success_cmd = self._build_success_command(cmd, shell).replace("\"", "\'").replace("\"", "\'")
        if user != 'root':
          final_cmd = f'sudo su {flags} -c "su {user} -c {success_cmd}"'
        else:
          final_cmd = f'sudo su {flags} -c "{success_cmd}"'
        

        # final_cmd = ' '.join([becomecmd, flags, prompt, user, self._build_success_command(cmd, shell)])

        # print(f"""
        # becomecmd: {becomecmd}
        # flags: {flags}
        # user: {user}
        # success_command: {self._build_success_command(cmd, shell)}
        # final_cmd: {final_cmd}
        # """)

        return final_cmd