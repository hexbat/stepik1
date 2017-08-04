def wsgi_application(environ, start_response):
  status = '200 OK'
  qs = environ['QUERY_STRING']
  if '?' in qs:
    qs = qs.split('?')[1]
  body = '\n'.join(qs.split('&'))
  headers = [('Content-type','text/plain'),
        ('Content-Length', str(len(body))]         
  start_response(status, headers)
  return [body]
