#!/usr/local/bin/python2.6

"""
agent for 'PeepStats' resource monitoring protocol
 
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

import web
import sys
from agentlib import read_path,check_src_acl,check_proc_acl

urls = (
  '/proc/(.*)', 'proc_get',
  '/(.*)', 'index',
)

class proc_get:
    '''Pulls data from proc
	- (will) support a blocked path list
    '''
    def GET(self, path_str):
        ''' Return PROC data '''
        check_src_acl(web.ctx)

	path = '/proc/' + path_str
        check_proc_acl(web.ctx)

	data = read_path(path)
        return data 


class index:
    def GET(self,path_str):
        ''' Handle GET requests for all else
            - Catch all
            - Node detail reporting
        '''
        check_src_acl(web.ctx)

        data = ''

        if path_str == 'platform':
            data = sys.platform
        else:
            data = "Hello @ /"

        return data



if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = False
    app.run()

