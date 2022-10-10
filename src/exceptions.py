class AppException(Exception):
    pass

class TemplateParameterException(AppException):
    pass

class ParserArgumentException(AppException):
    pass

class MalformedUploadedFileException(AppException):
    pass
