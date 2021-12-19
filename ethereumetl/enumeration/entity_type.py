class EntityType:
    BLOCK = 'block'
    TRANSACTION = 'transaction'
    RECEIPT = 'receipt'
    LOG = 'log'
    TOKEN_TRANSFER = 'token_transfer'
    TOKEN_APPROVAL = 'token_approval'
    CONTRACT = 'contract'
    TOKEN = 'token'

    ALL_FOR_STREAMING = [BLOCK, TRANSACTION, LOG, TOKEN_TRANSFER, TOKEN_APPROVAL, CONTRACT, TOKEN]
