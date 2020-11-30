promos = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order):
    """Select best discount available"""
    return max(promo(order) for promo in promos)
    
    
Order(joe, banana_cart, fidelity_promo)
Order(joe, banana_cart, bulk_item_promo)
Order(joe, banana_cart, large_order_promo)
best_promo(Order(joe, banana_cart))
