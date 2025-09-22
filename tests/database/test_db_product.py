import pytest
import sqlite3
from modules.common.database import Database


@pytest.mark.database           #Тест на вставку некоректного типу даних
def test_insert_invalid_data_type():
    db = Database()
    with pytest.raises(sqlite3.OperationalError):
        db.insert_product(5, 'помилка', 'тип', 'не число')  # qnt має бути числом

@pytest.mark.database          #Тест на обробку нульового значення
def test_insert_null_quantity():
    db = Database()
    db.insert_product(6, 'нуль', 'тест', 0)
    qnt = db.select_product_qnt_by_id(6)
    assert qnt[0][0] == 0

@pytest.mark.database          #Тест на оновлення кількості товару кілька разів
def test_multiple_quantity_updates():
    db = Database()
    db.insert_product(7, 'мульти', 'оновлення', 10)
    db.update_product_qnt_by_id(7, 20)
    db.update_product_qnt_by_id(7, 30)
    qnt = db.select_product_qnt_by_id(7)
    assert qnt[0][0] == 30

@pytest.mark.database         #Тест на отримання адреси неіснуючого користувача 
def test_get_address_nonexistent_user():
    db = Database()
    result = db.get_user_address_by_name('Невідомий')
    assert result == [] or result is None

@pytest.mark.database          #Тест на видалення неіснуючого продукту
def test_delete_nonexistent_product():
    db = Database()
    db.delete_product_by_id(9999)
    result = db.select_product_qnt_by_id(9999)
    assert result == [] or result is None

@pytest.mark.database      #Тест на вставку продукту з довгим описом    
def test_insert_long_description():
    db = Database()
    long_desc = 'a' * 500
    db.insert_product(8, 'довгий', long_desc, 5)
    qnt = db.select_product_qnt_by_id(8)
    assert qnt[0][0] == 5

@pytest.mark.database      #Тест на коректність дати замовлення 
def test_order_date_format():
    db = Database()
    orders = db.get_detailed_orders()
    for order in orders:
        date = order[4]
        assert isinstance(date, str)
        assert ':' in date  # базова перевірка часу



