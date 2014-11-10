

class UnitUtils():  

	# is valid values
    TRUE = True;
    FALSE = False;

    # error code values
    # everything ok
    OK_CODE = "1";
    OK_MESSAGE = "";  

    # unexpected
    UNEXPECTED_CODE = "2";
    UNEXPECTED_MESSAGE = "unexpected";  

    @staticmethod
    def SetOKDTO(dto):
        dto.IsValid = BaseUtils.TRUE
        dto.Code = BaseUtils.OK_CODE
        dto.Message = BaseUtils.OK_MESSAGE  
        
    @staticmethod
    def SetUnexpectedErrorDTO(dto):
        dto.IsValid = BaseUtils.FALSE
        dto.Code = BaseUtils.UNEXPECTED_CODE
        dto.Message = BaseUtils.UNEXPECTED_MESSAGE   
