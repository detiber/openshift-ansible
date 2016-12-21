# pylint: disable=invalid-name,protected-access,import-error,line-too-long,attribute-defined-outside-init

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""This file is a stdout callback plugin for OpenShift Diagnostics"""

from __future__ import (absolute_import, print_function)
import sys
from ansible import constants as C
from ansible.plugins.callback import CallbackBase
from ansible.utils.color import colorize, hostcolor, stringc


class CallbackModule(CallbackBase):
    """
    Ansible callback plugin
    """
    CALLBACK_VERSION = 2.2
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'openshift_diag'
    CALLBACK_NEEDS_WHITELIST = False

    def banner(self, msg, color=None):
        '''Prints a header-looking line with stars taking up to 80 columns
        of width (3 columns, minimum)

        Overrides the upstream banner method so that display is called
        with log_only=True
        '''
        msg = msg.strip()
        star_len = (79 - len(msg))
        if star_len < 0:
            star_len = 3
        stars = "*" * star_len
        self._display.display("\n%s %s" % (msg, stars), color=color, log_only=True)

    def v2_playbook_on_start(self, playbook):
        """This is basically the start of it all"""
        self.errors = []
        self.warnings = []

    def v2_runner_on_ok(self, result):
        """This prints out task results in a fancy format"""
        self._display.display('v2_runner_on_ok', screen_only=True)
#        delegated_vars = result._result.get('_ansible_delegated_vars', None)
#        self._clean_results(result._result, result._task.action)
#        if result._task.action in ('include', 'include_role'):
#            return
#        elif result._result.get('changed', False):
#            if delegated_vars:
#                msg = "changed: [%s -> %s]" % (result._host.get_name(), delegated_vars['ansible_host'])
#            else:
#                msg = "changed: [%s]" % result._host.get_name()
#            color = C.COLOR_CHANGED
#        else:
#            if delegated_vars:
#                msg = "ok: [%s -> %s]" % (result._host.get_name(), delegated_vars['ansible_host'])
#            else:
#                msg = "ok: [%s]" % result._host.get_name()
#            color = C.COLOR_OK
#
#        if result._task.loop and 'results' in result._result:
#            self._process_items(result)
#        else:
#
#            if (self._display.verbosity > 0 or '_ansible_verbose_always' in result._result) and '_ansible_verbose_override' not in result._result:
#                msg += " => %s" % (self._dump_results(result._result),)
#            self._display.display(msg, color=color, log_only=True)
#
#        self._handle_warnings(result._result)

    def v2_runner_item_on_ok(self, result):
        """Print out task results for items you're iterating over"""
        print('v2_runner_item_on_ok')
#        delegated_vars = result._result.get('_ansible_delegated_vars', None)
#        if result._task.action in ('include', 'include_role'):
#            return
#        elif result._result.get('changed', False):
#            msg = 'changed'
#            color = C.COLOR_CHANGED
#        else:
#            msg = 'ok'
#            color = C.COLOR_OK
#
#        if delegated_vars:
#            msg += ": [%s -> %s]" % (result._host.get_name(), delegated_vars['ansible_host'])
#        else:
#            msg += ": [%s]" % result._host.get_name()
#
#        msg += " => (item=%s)" % (self._get_item(result._result),)
#
#        if (self._display.verbosity > 0 or '_ansible_verbose_always' in result._result) and '_ansible_verbose_override' not in result._result:
#            msg += " => %s" % self._dump_results(result._result)
#        self._display.display(msg, color=color, log_only=True)
#
    def v2_playbook_on_stats(self, stats):
        """Print the final playbook run stats"""
        self._display.display("", screen_only=True)
        self.banner("DIAGNOSTICS REPORT")

        hosts = sorted(stats.processed.keys())
        for h in hosts:
            t = stats.summarize(h)

            self._display.display("{0}:\n{1}:\n{2}\n{3}:\n{2}\n".format(
                hostcolor(h, t),
                colorize('warnings', len(self.warnings), C.COLOR_WARN),
                stringc(self.warnings, C.COLOR_WARN),
                colorize('errors', len(self.errors), C.COLOR_ERROR),
                stringc(self.errors, C.COLOR_ERROR)
            ))

        self._display.display("", screen_only=True)
        self._display.display("", screen_only=True)
