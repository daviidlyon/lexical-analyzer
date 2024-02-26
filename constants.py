RESERVED_WORDS_LIST = [
'TextWindow',
'ElseIf',
'EndIf',
'EndWhile',
'EndFor',
'EndSub',
'Goto',
'If',
'Then',
'Else',
'While',
'For',
'Sub',
'And',
'Or',
'Array',
'To',
'Step',
'Stack',
'Program',
]


SPECIAL_SYMBOLS_DICT  = {
'<>':'tkn_diff',
'<=':'tkn_leq',
'>=':'tkn_geq',
}

SYMBOLS_DICT = {
'=': 'tkn_equals',
'.': 'tkn_period',
',': 'tkn_comma',
':': 'tkn_colon',
'[': 'tkn_left_brac',
']': 'tkn_right_brac',
'(': 'tkn_left_paren',
')': 'tkn_right_paren',
'+': 'tkn_plus',
'-': 'tkn_minus',
'*': 'tkn_times',
'/': 'tkn_div',
'<': 'tkn_less',
'>': 'tkn_greater',
}