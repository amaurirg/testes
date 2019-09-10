"""
from collections import namedtuple
n_t = namedtuple('Register', ['Details', 'Name', 'Type', 'From-To', 'Null', 'Description'])
n_t = namedtuple('Register', ['Details', 'Name', 'Type', 'From_To', 'Null', 'Description'])
r1 = n_t('identity/LineItemId', 'str', '-', 'Não', 'ID que identifica todos os itens da linha (É importante para identificar itens em outros CSVs)')
r1 = n_t('Identity - Campos Estáticos', 'identity/LineItemId', 'str', '-', 'Não', 'ID que identifica todos os itens da linha (É importante para identificar itens em outros CSVs)')

r1.Details
'Identity - Campos Estáticos'
r1.Description
'ID que identifica todos os itens da linha (É importante para identificar itens em outros CSVs)'

"""
