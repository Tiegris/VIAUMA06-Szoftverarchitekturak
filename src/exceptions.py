class ManagedException(Exception):
    pass

class ArgumentParsingError(ManagedException):
    pass

class ParserEngineError(ManagedException):
    pass

class MalformedUploadedFileError(ManagedException):
    pass
