from src.item import Item
import pytest
"""Здесь надо написать тесты с использованием pytest для модуля item."""
item1 = Item("Смартфон", 10000, 20)
def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000

def test_init():
    assert item1.price == 10000
    assert item1.quantity == 20
    assert item1.name == "Смартфон"


def test_name():
    assert len(Item.all) != 5
    item = Item.all[0]
    assert Item.name != "Смартфон"
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

