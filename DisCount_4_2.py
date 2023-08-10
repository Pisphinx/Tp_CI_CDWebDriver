import pytest
def calculate_discount(price, discount_percentage):
    if price <= 0 or discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Invalid input values")
    discount_amount = (discount_percentage / 100) * price
    discounted_price = price - discount_amount
    return discounted_price

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode (without UI)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# 💰 Valid input values test
def test_valid_input_values(driver):
    price = 100
    discount_percentage = 50
    expected_discounted_price = 50

    discounted_price = calculate_discount(price, discount_percentage)
    assert discounted_price == expected_discounted_price
    
# ❌ Price less than or equal to 0 test
def test_price_less_than_or_equal_to_0():
    price = 0
    discount_percentage = 50

    with pytest.raises(ValueError, match="Invalid input values"):
        calculate_discount(price, discount_percentage)

# ❌ Discount percentage less than 0 test
def test_discount_percentage_less_than_0():
    price = 100
    discount_percentage = -50

    with pytest.raises(ValueError, match="Invalid input values"):
        calculate_discount(price, discount_percentage)

# ❌ Discount percentage greater than 100 test
def test_discount_percentage_greater_than_100():
    price = 100
    discount_percentage = 150

    with pytest.raises(ValueError, match="Invalid input values"):
        calculate_discount(price, discount_percentage)
