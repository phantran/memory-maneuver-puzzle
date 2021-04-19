from src.strategies.strategy_two import StrategyTwo


def test_execute():
    numbers_list = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    strategy_two = StrategyTwo()
    assert strategy_two.execute(numbers_list)[0] == {"sum_meta": 138, "root_value": 66}
