from models import db
from objects.item import Item

class ItemRepository:
    def __init__(self):
        self.db = db

    def add_items_from_data(self, item_data_list, documento_id):
        """
        Adiciona itens ao banco de dados a partir de uma lista de dicionários.
        :param item_data_list: Lista de dicionários com dados dos itens.
        :param documento_id: ID do documento ao qual os itens estão associados.
        """
        for item_data in item_data_list:
            item = Item(
                nome=item_data.get('ITEM'),  # Nome do item
                descricao=item_data.get('DESCRIÇÃO'),  # Descrição do item
                quantidade=item_data.get('QUANTIDADE'),  # Quantidade
                vlr_unit=item_data.get('PREÇO UNITÁRIO R$'),  # Preço unitário
                vlr_total=item_data.get('PREÇO TOTAL R$'),  # Preço total
                documento_id=documento_id  # Associando ao documento
            )
            self.db.session.add(item)
        
        self.db.session.commit()
