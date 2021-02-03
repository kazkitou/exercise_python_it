class OopsException(Exception) :
    print('class OopsException '+str(Exception))

try :
    raise OopsException('panic')
except OopsException as exc :
    print(exc)
    print('Caught an oops')