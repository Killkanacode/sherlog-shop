"""Regression test for incident #76: order_total must accept reserved lines."""

from orders.pricing import order_total


def test_order_total_uses_reserved_unit_price_lines():
    lines = [
        {"sku": "A", "qty": 2, "unit_price": 500},
        {"sku": "B", "qty": 1, "unit_price": 250},
    ]
    assert order_total(lines) == 2 * 500 + 250
