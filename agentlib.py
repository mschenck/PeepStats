"""
Library for 'PeepStats' agent
 
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
 
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
 
"""

class AclException(Exception):
    ''' Exception class for all ACL blocking '''
    def __init__(self,msg):
        self.args = (1,msg)
        self.errmsg = msg

def read_path(path):
    ''' Pull contents from path received or fail gracefully '''
    contents = ''
    try:
        fin = open(path, 'r')
    except BaseException as e:
        contents = str(e)
    else:
        contents = fin.read()
        fin.close()

    return contents

def check_src_acl(REQ):
    src_ip = REQ.env.get('REMOTE_ADDR')
    if src_ip == '127.0.0.1':
        raise AclException("Host %s not allowed" % src_ip)

def check_proc_acl(path):
    if str(path) == "/proc/foo":
        raise AclException("Path %s not allowed" % path)
