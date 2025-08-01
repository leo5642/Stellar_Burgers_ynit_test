import pytest
import sys
from pathlib import Path

# Добавляем корень проекта в пути Python
sys.path.append(str(Path(__file__).parent.parent))

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestBooksCollector2:
    def test_set_bun(self):
        burger = Burger()          
        burger.set_buns("Булка")  
        assert burger.bun == "Булка"
    
    def test_add_ingredient(self):
        burger = Burger()
        ing1 = 'Соус1'
        burger.add_ingredient(ing1)
        assert burger.ingredients[0] == ing1
    
    def test_remove_ingredient(self):
        burger = Burger()
        ing1 = 'Соус1'
        burger.add_ingredient(ing1)
        burger.remove_ingredient(0)
        assert burger.ingredients == []
    
    def test_move_ingridient(self):
        burger = Burger()
        ing1 = 'Соус1'
        ing2 = 'Соус2'
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.move_ingredient(1,0)
        assert burger.ingredients[0] == ing2

    def test_get_price(self):
        burger = Burger()
        name = 'Булка'
        price = 50
        bun = Bun(name, price)
        burger.set_buns(bun)

        ingrident = Ingredient
        ing1 = 'Сацебели'
        price_ing1 = 50
        ing = Ingredient('SAUCE', ing1, price_ing1)
        burger.add_ingredient(ing)

        sum = burger.get_price()
        assert sum == 150

    def test_get_receipt(self):
        burger = Burger()
        name = 'Булка'
        price = 50
        bun = Bun(name, price)
        burger.set_buns(bun)

        ingrident = Ingredient
        ing1 = 'Сацебели'
        price_ing1 = 50
        ing = Ingredient('SAUCE', ing1, price_ing1)
        burger.add_ingredient(ing)

        sum = f"""(==== Булка ====)
        = sauce Сацебели =
        (==== Булка ====)
        Price: 150")"""
        assert name, ing1 in burger.get_receipt()
