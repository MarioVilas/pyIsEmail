from pyisemail.diagnosis import BaseDiagnosis


class CFWSDiagnosis(BaseDiagnosis):
    DESCRIPTION = ("Address is valid within the message "
                   "but cannot be used unmodified for the envelope.")
    MESSAGES = {
        'COMMENT': "Address contains messages",
        'FWS': "Address contains Folding White Space",
    }

    REFERENCES = {
        'COMMENT': ['dot-atom'],
        'FWS': ['local-part'],
    }
