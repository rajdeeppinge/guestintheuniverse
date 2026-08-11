#!/usr/bin/env python3
"""
Test script for UnitConversionService
Run this to validate unit conversions locally
"""

import sys
import os

# Add the parent directory to the path so we can import the service
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from unit_conversion_service import UnitConversionService

def test_conversions():
    """Test various unit conversions"""
    service = UnitConversionService()
    
    test_cases = [
        # Length conversions
        {'category': 'length', 'value': 1000, 'from': 'meters', 'to': 'kilometers', 'expected': 1.0},
        {'category': 'length', 'value': 1, 'from': 'kilometers', 'to': 'meters', 'expected': 1000.0},
        {'category': 'length', 'value': 1, 'from': 'miles', 'to': 'kilometers', 'expected': 1.609344},
        
        # Weight conversions
        {'category': 'weight', 'value': 1, 'from': 'kilograms', 'to': 'grams', 'expected': 1000.0},
        {'category': 'weight', 'value': 1, 'from': 'pounds', 'to': 'kilograms', 'expected': 0.453592},
        
        # Temperature conversions
        {'category': 'temperature', 'value': 0, 'from': 'celsius', 'to': 'fahrenheit', 'expected': 32.0},
        {'category': 'temperature', 'value': 100, 'from': 'celsius', 'to': 'fahrenheit', 'expected': 212.0},
        {'category': 'temperature', 'value': 32, 'from': 'fahrenheit', 'to': 'celsius', 'expected': 0.0},
        {'category': 'temperature', 'value': 0, 'from': 'celsius', 'to': 'kelvin', 'expected': 273.15},
        
        # Volume conversions
        {'category': 'volume', 'value': 1, 'from': 'liters', 'to': 'milliliters', 'expected': 1000.0},
        {'category': 'volume', 'value': 1, 'from': 'gallons', 'to': 'liters', 'expected': 3.78541},
        
        # Area conversions
        {'category': 'area', 'value': 1, 'from': 'square_meters', 'to': 'square_feet', 'expected': 10.7639},
        {'category': 'area', 'value': 1, 'from': 'acres', 'to': 'square_meters', 'expected': 4046.86},
        
        # Speed conversions
        {'category': 'speed', 'value': 100, 'from': 'kilometers_per_hour', 'to': 'meters_per_second', 'expected': 27.7778},
        {'category': 'speed', 'value': 60, 'from': 'miles_per_hour', 'to': 'kilometers_per_hour', 'expected': 96.5606},
    ]
    
    print("Running unit conversion tests...\n")
    passed = 0
    failed = 0
    
    for test in test_cases:
        result = service.convert(
            test['value'], 
            test['from'], 
            test['to'], 
            test['category']
        )
        
        if 'error' in result:
            print(f"[X] FAILED: {test['category']} {test['value']} {test['from']} -> {test['to']}")
            print(f"   Error: {result['error']}\n")
            failed += 1
        else:
            # Check if result is close to expected (allowing for rounding)
            if abs(result['result'] - test['expected']) < 0.01:
                print(f"[OK] PASSED: {test['category']} {test['value']} {test['from']} -> {test['to']}")
                print(f"   Result: {result['result']} (expected: {test['expected']})\n")
                passed += 1
            else:
                print(f"[X] FAILED: {test['category']} {test['value']} {test['from']} -> {test['to']}")
                print(f"   Result: {result['result']} (expected: {test['expected']})\n")
                failed += 1
    
    print(f"\nTest Results: {passed} passed, {failed} failed")
    
    # Test error cases
    print("\nTesting error cases...\n")
    error_cases = [
        {'category': 'length', 'value': 1, 'from': 'meters', 'to': 'invalid_unit', 'desc': 'Invalid to_unit'},
        {'category': 'invalid_category', 'value': 1, 'from': 'meters', 'to': 'kilometers', 'desc': 'Invalid category'},
        {'category': 'length', 'value': 1, 'from': 'invalid_unit', 'to': 'meters', 'desc': 'Invalid from_unit'},
    ]
    
    error_passed = 0
    for test in error_cases:
        result = service.convert(test['value'], test['from'], test['to'], test['category'])
        if 'error' in result:
            print(f"[OK] PASSED: {test['desc']} - Error correctly returned: {result['error']}")
            error_passed += 1
        else:
            print(f"[X] FAILED: {test['desc']} - Should have returned error")
    
    print(f"\nError handling: {error_passed}/{len(error_cases)} passed")
    
    # Test available units
    print("\nTesting available units...\n")
    units = service.get_available_units()
    print(f"Available categories: {list(units.keys())}")
    for category, unit_list in units.items():
        print(f"  {category}: {len(unit_list)} units")
    
    return failed == 0 and error_passed == len(error_cases)

if __name__ == '__main__':
    success = test_conversions()
    sys.exit(0 if success else 1)
