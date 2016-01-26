#!/usr/bin/env python
import os
from helloflask import app as application
#
if __name__ == '__main__':
    
    virtenv= os.path.join(os.environ.get('OPENSHIFT_PYTHON_DIR', '.'), 'virtenv')
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.serve_forever()
