'''all custom exceptions should go here'''


class P2THImportFailed(Exception):
    '''Importing of PeerAssets P2TH privkeys failed.'''


class InvalidDeckIssueModeCombo(Exception):
    '''When verfiying deck issue_mode combinations.'''


class UnsupportedNetwork(Exception):
    '''This network is not suppored by pypeerassets.'''


class InvalidDeckSpawn(Exception):
    '''Invalid deck_spawn, deck is not properly tagged.'''


class InvalidDeckMetainfo(Exception):
    '''Deck metainfo incomplete, deck must have a name.'''


class InvalidDeckVersion(Exception):
    '''Deck version mistmatch.'''


class InvalidDeckIssueMode(Exception):
    '''Deck Issue mode is wrong.'''


class InvalidCardTransferP2TH(Exception):
    '''card_transfer does not pay to deck p2th in vout[0]'''


class CardVersionMistmatch(Exception):
    '''card_transfers version must match deck.version'''


class CardNumberOfDecimalsMismatch(Exception):
    '''card_tranfer number of decimals does not match deck rules.'''


class InsufficientFunds(Exception):
    '''this address does not have enough assigned UTXOs'''
