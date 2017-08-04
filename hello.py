def wsgi_application(environ, start_response):
  status = '200 OK'
  headers = [('Content-Type', 'text/plain')]
  qs = environ['QUERY_STRING']
  if '?' in qs:
    qs = qs.split('?')[1]
  body = '\n'.join(qs.split('&'))
  start_response(status, headers)
  return [body]
